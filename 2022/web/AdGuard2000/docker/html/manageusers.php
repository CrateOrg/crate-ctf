<?php
include_once("db.php");
include_once("checkauth.php");

if (!isset($_SESSION['currentuid']) || $_SESSION['currentuid'] != 9) {
  echo("Only accessable for admin!");
  die();
}

$title = "Hantera users";
include_once("header.php");
?>
<br><br>
 <form action="manageusers.php" method="get">
  <label for="usersearch">Sök användare:</label>
  <input type="text" id="usersearch" name="usersearch">
  <input type="submit" value="Submit">
</form> 
<?php

if (isset($_GET['usersearch']) && strlen($_GET['usersearch']) > 0) {
  $usersearch = $_GET['usersearch'];
}
else {
  $usersearch = "%";
}

$queriesq = 'SELECT * from users where username like "' . $usersearch . '"';

echo "<br><h1>Users</h1>";

$rows = $dbhandle->query($queriesq);
  echo("<table border=2>"); 
  echo("<tr>");
  echo("<th align='left'>Username</th>");
  echo("<th align='left'>Password</th>");
  echo("<th align='left'>Email</th>");
  echo("<th align='left'>Active queries</th>");
  echo("</tr>");
  while ($row = $rows->fetch()) {
    echo("<tr>");
    echo("<td>" . $row['username'] . "</td>");
    echo("<td>" . $row['password'] . "</td>");
    echo("<td>" . $row['email'] . "</td>");
    echo("<td>");
    $numqueries = $dbhandle->query("select count(*) from queries where owner=" . $row['id'] )->fetchColumn();
    if (intval($numqueries) > 0) {
      echo($numqueries);
    }
    echo("</td>");
    echo("</tr>");
  } // while
  echo("</table>");


?>

</body>
</html>

