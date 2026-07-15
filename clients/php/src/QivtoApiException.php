<?php

declare(strict_types=1);

namespace Qivto\Api;

final class QivtoApiException extends \RuntimeException
{
    public function __construct(string $message, public readonly int $status, public readonly array $headers = [], public readonly array $response = [])
    {
        parent::__construct($message, $status);
    }
}
