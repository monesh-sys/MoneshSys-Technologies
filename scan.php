<?php
if (!isset($_SERVER['HTTP_X_MONESHSYS_SCANNER'])) {
  http_response_code(403);
  exit("Unauthorized scanner");
}

$token = $_GET['t'] ?? "";
$data = json_decode(file_get_contents("tokens.json"), true);

if (!isset($data[$token])) {
  http_response_code(400);
  exit("Invalid QR");
}

$record = $data[$token];
if ($record['status'] !== "active" || strtotime($record['expiry']) < time()) {
  http_response_code(400);
  exit("Expired QR");
}

echo json_encode([
  "type" => $record['type'],
  "id" => $record['linked_id'],
  "status" => "Valid",
  "company" => "MoneshSys Technologies"
]);
