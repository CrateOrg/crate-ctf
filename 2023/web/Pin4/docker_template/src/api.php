<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

$flag = "#REPLACE_FLAG#";
$authData = "wJrl9eDEHW21MDptlgDXxXxOSbNF3VS4UD9TcaJe";

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
    $output = null;
    $result = null;
    exec("./verifypin.sh $pin", $output, $result);
    
    if ($result === 0) {
        $output["auth"] = $output["0"];
        unset($output["0"]);
        Success($output);
    } else {
        ErrorCustom("Invalid pin");
    }
} else if ($p1 === "getflag") {
    $headers = getallheaders();
    $authHeader = $headers["auth"] ?? $headers["Auth"] ?? "";
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
