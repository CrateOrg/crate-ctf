<?php
header("Content-Type: application/json");
if (!isset($_POST) || !isset($_POST["pos"])) {
  echo "{\n    \"error\": \"Invalid input\"\n}";
} else {
  $cmd = "python3 /var/www/cpos.py " . escapeshellarg($_POST["pos"]);
  $output = shell_exec($cmd);
  echo $output;
}
?>
