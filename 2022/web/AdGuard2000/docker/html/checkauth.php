<?php
function curPageName() {
  return substr($_SERVER["SCRIPT_NAME"],strrpos($_SERVER["SCRIPT_NAME"],"/")+1);
}

session_start();
if (!isset($_SESSION['currentuser'])) {
  header("location:login.php");
  die();
}
else if (curPageName() == "index.php") {
  header("location:manage.php");
}
?>

