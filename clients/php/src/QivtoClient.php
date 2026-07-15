<?php

declare(strict_types=1);

namespace Qivto\Api;

final class QivtoClient
{
    public function __construct(private string $baseUrl = 'https://qivto.com/api/v1')
    {
        $this->baseUrl = rtrim($this->baseUrl, '/');
    }

    public function tools(string $language = 'en'): array
    {
        return $this->request('GET', '/tools?lang=' . ($language === 'lt' ? 'lt' : 'en'));
    }

    public function uuid(int $count = 1): array
    {
        return $this->request('POST', '/uuid', ['count' => max(1, min(100, $count))]);
    }

    public function hash(string $text, string $algorithm = 'sha256'): array
    {
        return $this->request('POST', '/hash', compact('text', 'algorithm'));
    }

    public function formatJson(array|string $json): array
    {
        return $this->request('POST', '/json-format', compact('json'));
    }

    public function status(): array
    {
        return $this->request('GET', '/status');
    }

    private function request(string $method, string $path, ?array $body = null): array
    {
        if (!function_exists('curl_init')) throw new \RuntimeException('The PHP cURL extension is required.');
        $headers = [];
        $ch = curl_init($this->baseUrl . $path);
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CUSTOMREQUEST => $method,
            CURLOPT_TIMEOUT => 20,
            CURLOPT_HTTPHEADER => ['Accept: application/json', 'Content-Type: application/json'],
            CURLOPT_HEADERFUNCTION => static function ($handle, string $line) use (&$headers): int {
                if (str_contains($line, ':')) { [$name, $value] = explode(':', $line, 2); $headers[strtolower(trim($name))] = trim($value); }
                return strlen($line);
            },
        ]);
        if ($body !== null) curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body, JSON_THROW_ON_ERROR));
        $raw = curl_exec($ch);
        $error = curl_error($ch);
        $status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
        curl_close($ch);
        if ($error !== '') throw new \RuntimeException($error);
        $data = json_decode((string) $raw, true);
        if (!is_array($data)) throw new \RuntimeException('QIVTO returned invalid JSON.');
        if ($status >= 400) throw new QivtoApiException((string) ($data['error'] ?? 'API request failed.'), $status, $headers, $data);
        return $data;
    }
}
