<?php
ini_set("display_errors", 1);
$dbhandle = new PDO("sqlite:adguard.db");
if (!$dbhandle) {
  echo "oops, can't open the database!";
  die ($error);
}
?>
