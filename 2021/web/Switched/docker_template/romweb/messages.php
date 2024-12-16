<?php
  include_once("config.php");
  $authcookie=$_COOKIE["auth"] ?? "";

  if ($authcookie === $authvalue) {
    echo("reading messages!");
    echo("<pre>");
    if (file_exists($messages_file)) {
      echo(readfile($messages_file));
      unlink($messages_file);
    }
    else {
      echo("No new messages");
    }
    echo("</pre>");

    // delete it
  }
  else {
    echo('<h3><font color="red">Only admin can read messages!</font></h3>');
  }
?>

