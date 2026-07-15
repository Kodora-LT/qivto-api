# PHP client

```php
require 'vendor/autoload.php';

$client = new Qivto\Api\QivtoClient();
$result = $client->hash('QIVTO');
echo $result['hash'];
```

Install locally with `composer install`. PHP 8.1+ and the cURL extension are required.
