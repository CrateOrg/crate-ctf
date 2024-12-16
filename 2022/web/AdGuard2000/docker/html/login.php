<?php
include_once("db.php");

if (isset($_POST['username']) and isset($_POST['password'])) {
  $currentpass = $_POST['password'];
  $currentuser = $_POST['username'];

  $currentuser = stripslashes($currentuser);
  $currentpass = stripslashes($currentpass);

  $currentuser = $dbhandle->quote($currentuser);
  //$currentpass = $dbhandle->quote($currentpass);

  $numquery = "SELECT COUNT(*) FROM users
               WHERE 
               username=$currentuser
               and
               password='$currentpass'";
  
  $query = "SELECT * FROM users
            WHERE 
            username=$currentuser
            and
            password='$currentpass'";


  $rows = $dbhandle->query($numquery)->fetchColumn();

  if ($rows == 1) {
    //OK, user found!
    //echo "found you!";

    $array = $dbhandle->query($query)->fetch();
    
    $currentuid = $array['id'];

    // Log the event
    $dbhandle->query("INSERT INTO LOGINS VALUES($currentuid, datetime())");

    session_start();
    $_SESSION["currentuser"] = $currentuser;
    $_SESSION["currentpass"] = $currentpass;
    $_SESSION["currentuid"] = $currentuid;
    header("location:manage.php");
  }
  else {
    $errormsg = "User and/or password does not match. Try again.";
  }
}
else {
  $currentuser = "";
}

$title = "Adguard 2000";
include_once("header.php");
?>


<h3>Login</h3>

<?php
  if (isset($errormsg)) {
    echo "<br>";
    echo "<font color=red>";
    echo $errormsg;
    echo "</font>";
  }
?>

<form name="login" method="post" action="">
  <table width="494" border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="227" height="37">Username
        <input name="username" type="text" id="username" maxlength="64" /></td>
      <td width="222">Password      
      <input name="password" type="password" id="password" maxlength="64" /></td>
      <td width="45"><input type="submit" name="button" id="button" value="Login" /></td>
    </tr>
  </table>
</form>
<p>
</p>
</body>
</html>

