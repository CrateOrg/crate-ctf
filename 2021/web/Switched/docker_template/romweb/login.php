<html>
  <head>
    <title>FOI ROMS</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link href="site.css" type="text/css" rel="stylesheet">
  </head>
  <body>
<div class="body">
<center>
<font size="20"><h1>Welcome to FOI-ROMS!</h1></font>
<h3>The place to get switched!</h3>
</center>
<?php
include_once("config.php");
if (array_key_exists("username", $_POST)&&
    array_key_exists("password", $_POST)) {
    echo("<font color='red'>Login failed.<br><br></font>");
}
?>
<form action="login.php" method="post">
  <div class="elem-group">
    <label for="username">username</label>
    <input type="text" id="username" name="username" placeholder="username" pattern=[A-Z\sa-z]{3,20} required>
  </div>
  <div class="elem-group">
    <label for="password">password</label>
    <input type="password" id="password" name="password" required>
  </div>
  <button type="submit">Login</button>
</form>

