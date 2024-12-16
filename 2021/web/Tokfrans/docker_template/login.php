<?
    include_once("jwt.php");

    // Get username + password sent as POST
    $username = $_POST["username"] ?? "";
    $password = $_POST["password"] ?? "";

    if ($username === "zeke") {
        if ($password === "irule42") {
            login("zeke");
        }
        else {
            dbg_header("invalid password");
            redirect_to("index");
        }
    }
    else if ($username === "admin") {
        if ($password === "Kb82ehaAaTUfRVVhKHux") {
            login("admin");
        }
        else {
            dbg_header("invalid password");
            redirect_to("index");
        }
    } 
    else {
        // Unknown user
        dbg_header ("invalid user");
        redirect_to("index");
    }

    function dbg_header($str) {
        // header('dbg: ' . $str);
    }

    function login($username) {
        $token = create_jwt($username);
        setcookie("s", $token);
        dbg_header("logged in as ". $username);
        redirect_to("manage");
    }

    function redirect_to($page) {
        header('Location: ' . $page . '.php');
        die();
    }
?>