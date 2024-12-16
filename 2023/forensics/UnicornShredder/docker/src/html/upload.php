<?php
header("Content-Type: application/json");
if($_FILES["file"]["error"] != UPLOAD_ERR_OK) {
  echo "{\n    \"error\": \"Upload error, probably file size\"\n}";
}
else {
  $cmd = "python3 /var/www/shred.py " . $_FILES["file"]['tmp_name'];
  $output = shell_exec($cmd);
  echo $output;
}
?>
