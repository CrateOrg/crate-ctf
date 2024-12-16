<?php
if (isset($_GET['fetch'])) {
  $path=$_GET['fetch'];
  $content="";
  if (is_file($path)) {
    $content=file_get_contents($path);
  }
  else if (is_dir($path)) {
    $content = join("\n", scandir($path));
  }
  echo($content);
  die();
}
?>
<!doctype html>
<html lang="sv">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<!--
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns" crossorigin="anonymous"></script>
-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <link rel="stylesheet" href="chall.css">
    <script src="func.js"></script>
    <title>Fetch, Pluto. Fetch!</title>

</head>
<body onload="start();">
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        <a class="navbar-brand">Fetch, Pluto. Fetch!</a>
        <button class="navbar-toggler" data-target="#my-nav" data-toggle="collapse" aria-controls="my-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
    </nav>

    <br><br><br><br>
<div id="pagecontent">
<input type="text" id="filePath" name="filePath" placeholder="/path/to/file" size="30" autofocus required onkeypress="if(event.key == 'Enter') {fetchButton.click()}"/>
<button type="button" id="fetchButton" name="fetchButton">Fetch!</button>
<br><br>
<div id="output"></div>
</div>
</body>
</html>
