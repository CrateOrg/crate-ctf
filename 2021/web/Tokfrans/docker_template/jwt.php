<?
require __DIR__ . '/vendor/autoload.php';

use Ahc\Jwt\JWT;

// implicit HS256, 1h timeout, 0 leeway
$jwt = new JWT('queenoftherabbitkillers');

function verify_jwt($token) {
    global $jwt;
    try {
        $jwt->decode($token);
        return true;
    } catch (\Throwable $th) {
        return false;
    }
}

function is_admin($token) {
    global $jwt;

    // if $scope contains "admin" return true
    $payload = $jwt->decode($token);

    if (in_array("admin", $payload["scopes"])) {
        return true;
    }

    return false;
}

function get_user($token) {
    global $jwt;

    // if $scope contains "admin" return true
    $payload = $jwt->decode($token);
    
    return $payload["user"];
}

function create_jwt($username) {
    global $jwt;

    $scopes = [ "user" ];
   
    if ($username === "admin") {
        array_push($scope, "admin");
    }

    $token = $jwt->encode(
        ['user'   => $username,
        'scopes' => $scopes,
        'speed'  => 9000,
        'groy' => "b9bIAW1FlyKcQGyefuDL3F4or1zh0sRPF93R7n09"
        ]
    );

    return $token;
}



?>
