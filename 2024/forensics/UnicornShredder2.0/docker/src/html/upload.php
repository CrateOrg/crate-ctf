<?php
header("Content-Type: application/json");
if($_FILES["file"]["error"] != UPLOAD_ERR_OK) {
  echo "{\n    \"error\": \"Upload error, probably file size\"\n}";
}
else if (!isset($_POST) || !isset($_POST["algo"]) || (strcmp($_POST["algo"], "scissor-friendly") && strcmp($_POST["algo"], "ultra-secure"))) {
  echo "{\n    \"error\": \"Invalid shredding algorithm\"\n}";
}
else {
  $cmd = "python3 /var/www/shred.py " . $_POST["algo"] . " " . $_FILES["file"]['tmp_name'];
  $output = shell_exec($cmd);
  echo $output;
}
?>
