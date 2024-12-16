<?php
header('Content-Type: text/plain');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $decoded;
    if (isset($_COOKIE['clicks'])) {
        $cookieValue = $_COOKIE['clicks'];
        $decoded = base64_decode($cookieValue);
    } else {
        $decoded = '0';
    }
    if ($decoded == "1000000000") {
        $response = "cratectf{JagHoppasInteDuKlickadeManuellt!}\n";
    } else {
        $response = "Du måste klicka kakan 1000000000 gånger först!";
    }
    echo $response;
} else {

    http_response_code(405);
    echo 'Only POST requests are allowed.';
}
?>
