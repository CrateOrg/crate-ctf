<?
    // "delete" the cookie
    setcookie("s", "", time() - 10000);

    header("Location: index.php");
    die();
?>