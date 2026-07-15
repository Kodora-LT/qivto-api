<?php
$result = null;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $payload = json_encode(['algorithm' => 'sha256', 'text' => (string) ($_POST['text'] ?? '')]);
    $context = stream_context_create(['http' => ['method' => 'POST', 'header' => "Content-Type: application/json\r\n", 'content' => $payload, 'timeout' => 15, 'ignore_errors' => true]]);
    $result = json_decode((string) file_get_contents('https://qivto.com/api/v1/hash', false, $context), true);
}
?><!doctype html><html lang="en"><meta charset="utf-8"><title>QIVTO hash example</title><body><main><h1>SHA-256 with QIVTO</h1><form method="post"><label>Text <input name="text" required></label><button>Hash</button></form><?php if($result):?><pre><?=htmlspecialchars(json_encode($result, JSON_PRETTY_PRINT), ENT_QUOTES, 'UTF-8')?></pre><?php endif;?><p><a href="https://qivto.com/en/api" target="_blank" rel="noopener">Built with QIVTO API</a></p></main></body></html>
