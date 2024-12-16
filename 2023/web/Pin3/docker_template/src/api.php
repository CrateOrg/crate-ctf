<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");


$correctPin = "12945";
$authData = "ol5khuib3SADFn3k4Fo389l12j2";
$flag = "#REPLACE_FLAG#";

function Success($vars) {
    $result = array(
        "result" => "success"
    );
    $result = array_merge($result, $vars);

    http_response_code(200);
    echo (json_encode($result));
    die();
}

function ErrorCustom($error)
{
    $result = array(
        "result" => "error",
        "error" => $error
    );
    http_response_code(401);
    echo (json_encode($result));
    die();
}
    
function ErrorBadRequest() {
    $result = array(
        "result" => "error",
        "error" => "bad request"
    );
    http_response_code(400);
    echo (json_encode($result));
    die();
}

try {
    $p1 = explode("/", explode("api", $_SERVER['REQUEST_URI'])[1])[1];
} catch (Throwable $th) {
    ErrorBadRequest();
}

if ($p1 === "checkpin") {
    $pin = $_POST["pin"] ?? "";
    if ($pin === $correctPin) {
        $authArray = array(
            "auth" => $authData
        );
        Success($authArray);
    }
    else {
        ErrorCustom("Invalid pin");
    }
}
else if ($p1 === "getflag") {
    $headers = getallheaders();
    $authHeader = $headers["auth"] ?? $headers["Auth"] ?? "";
    $pin = $_POST["pin"] ?? "";
    if ($authHeader === $authData) {
        $flagArray = array(
            "flag" => $flag
        );
        Success($flagArray);
    }
    else {
        ErrorCustom("Invalid auth");
    }
}
else {
    ErrorBadRequest();
}

?>
