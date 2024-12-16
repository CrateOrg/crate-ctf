<?php
include_once("db.php");
include_once("checkauth.php");

$dbhandle->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$ACTION_REMOVE = "remove";
$ACTION_CHANGE = "change";
$ACTION_ADD    = "add";

// Do the stuff directly 
if (isset($_POST['changeaction'])) {
  switch($_POST['changeaction']) {
  case $ACTION_REMOVE:
    if (isset($_POST['queryid'])) {
      $removeq = "DELETE FROM queries WHERE id='" . $_POST['queryid'] . "'";
      try {
        $foo = $dbhandle->query($removeq);
      }
      catch (PDOException $e) {
        echo $e->getMessage();
        echo "oops!!";
      }
    }
    break;

  case $ACTION_CHANGE;
    $maxprice = isset($_POST['f_maxprice']) ? $_POST['f_maxprice'] : "0";
    $isenabled = isset($_POST['activebox']) ? "1" : "0";
    $updateq = "";
    if (isset($_POST['f_url'])) {
      $updateq = "UPDATE queries SET 
                    fullurl='" .$_POST['f_url'] ."',
                    enabled='" . $isenabled ."',
                    maxprice='$maxprice'
                  WHERE id='" .$_POST['queryid']. "'";
    }
    else if (isset($_POST['f_q']) &&
        isset($_POST['f_r']) && 
        isset($_POST['f_ag']) && 
        isset($_POST['f_st']) && 
        isset($_POST['f_f']) && 
        isset($_POST['f_cg']) && 
        isset($_POST['queryid'])) {
      $maxprice = isset($_POST['f_maxprice']) ? $_POST['f_maxprice'] : "0";
      $updateq = "UPDATE queries SET 
                    query='" .$_POST['f_q'] ."',
                    r='" .$_POST['f_r'] ."',
                    ag='" .$_POST['f_ag'] ."',
                    st='" .$_POST['f_st'] ."',
                    f='" .$_POST['f_f'] ."',
                    cg='" .$_POST['f_cg'] ."',
                    enabled='" . $isenabled ."',
                    maxprice='$maxprice'
                  WHERE id='" .$_POST['queryid']. "'";
    }
    try {
      $foo = $dbhandle->query($updateq);
    }
    catch (PDOException $e) {
      echo $e->getMessage();
    }
    break;

  case $ACTION_ADD;
    $maxprice = isset($_POST['f_maxprice']) ? $_POST['f_maxprice'] : "0";
    $updateq = "foo";
    if (isset($_POST['f_url']) && strlen($_POST['f_url']) > 0) {
      $updateq = "INSERT INTO queries 
                    (owner, fullurl, maxprice, enabled, lastid)
                  VALUES(
                    '" .$_SESSION['currentuid'] ."',
                    '" .$_POST['f_url'] ."',
                    '$maxprice',
                    '1',
                    'new'
                  )";
    }
    else if (isset($_POST['f_q']) &&
        isset($_POST['f_r']) && 
        isset($_POST['f_ag']) && 
        isset($_POST['f_st']) && 
        isset($_POST['f_f']) && 
        isset($_POST['f_cg'])) {
      $maxprice = isset($_POST['f_maxprice']) ? $_POST['f_maxprice'] : "0";
      $updateq = "INSERT INTO queries 
                    (owner, query, r, ag, st, f, cg, maxprice, enabled, lastid)
                  VALUES(
                    '" .$_SESSION['currentuid'] ."',
                    '" .$_POST['f_q'] ."',
                    '" .$_POST['f_r'] ."',
                    '" .$_POST['f_ag'] ."',
                    '" .$_POST['f_st'] ."',
                    '" .$_POST['f_f'] ."',
                    '" .$_POST['f_cg'] ."',
                    '$maxprice',
                    '1',
                    'new'
                  )";
    }
    try {
      $foo = $dbhandle->query($updateq);
    }
    catch (PDOException $e) {
      echo $e->getMessage();
    }
    break;
  }
}

$title = "Hantera bevakningar";
include_once("header.php");
?>

<?php
include_once("adguard_data.php");


$queriesq = 'SELECT * from queries WHERE owner=' . $_SESSION['currentuid'];
$countqq = 'SELECT COUNT(*) from queries WHERE owner=' . $_SESSION['currentuid'];

$numrows = $dbhandle->query($countqq)->fetchColumn();

echo "<br><h1>Bevakningar</h1>";

if ($numrows == 0) {
  echo "inga bevakningar";
}
else {
  $rows = $dbhandle->query($queriesq);
  while ($row = $rows->fetch()) {
    if (strlen($row["fullurl"]) > 0) $typeurl = true;
    else $typeurl = false;
echo '<form action="" method="post" name="changequery'.$row["id"] . '" id="changequery'.$row["id"].'">';
echo '<table align="left" border="0" cellpadding="1" cellspacing="1">';
echo '          <tr>';
echo '            <td>';
  if ($typeurl)    print("<input name=\"f_url\" type=\"text\" size=\"132\" value=\"$row[fullurl]\"/>");
  else             print("<input name=\"f_q\" type=\"text\" value=\"$row[query]\"/>");
echo '            </td>';
echo '            <td>';
                    print("<input name=\"f_maxprice\" type=\"text\" size=\"10\" maxlength=\"8\"");
                    if ($row['maxprice'] == 0) {
                      print("placeholder=\"max pris\">");
                    }
                    else {
                      print("value=\"$row[maxprice]\"/>");
                    }
echo '            </td>';
if (!$typeurl) {
echo '            <td>';
echo '              <select name="f_r" size="1">';
                      foreach ($data_r as $r=>$lan) {
                        print("<option value=\"$r\"");
                        if ($r == $row["r"]) {
                          print("selected=\"selected\"");
                        }
                        print(">$lan</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_ag" size="1">';
                      foreach ($data_ag as $key=>$desc) {
                        print("<option value=\"$key\"");
                        if ($key == $row["ag"]) {
                          print("selected=\"selected\"");
                        }
                        print(">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_st" size="1">';
                      foreach ($data_st as $key=>$desc) {
                        print("<option value=\"$key\"");
                        if ($key == $row["st"]) {
                          print("selected=\"selected\"");
                        }
                        print(">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_f" size="1">';
                      foreach ($data_f as $key=>$desc) {
                        print("<option value=\"$key\"");
                        if ($key == $row["f"]) {
                          print("selected=\"selected\"");
                        }
                        print(">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_cg" size="1">';
                      foreach ($data_cg as $key=>$desc) {
                        print("<option value=\"$key\"");
                        if ($key == $row["cg"]) {
                          print("selected=\"selected\"");
                        }
                        print(">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
} // if ($typeurl)
echo '            <td>';
                      print("<input name=\"activebox\" type=\"checkbox\" value=\"$row[enabled]\"");
                      if ($row["enabled"] == 1) {
                        print('checked="checked"');
                      }
                      print("/>Aktiv ");
echo '            </td>';
echo '            <td>';
print("             <input name=\"queryid\" type=\"hidden\" value=\"$row[id]\">");
print("             <input name=\"changeaction\" type=\"hidden\" value=\"$ACTION_CHANGE\">");
echo '              <input name="addbutton" type="submit" value="Spara" /></td>';
echo '          </tr>';
echo '</table>';
echo '</form>';

echo '<form action="" method="post" name="removequery" id="removequery">';
echo '<table align="left" border="0" cellpadding="1" cellspacing="1">';
echo '<tr>';
echo '  <td>';
echo '    <input name="removebutton" type="submit" value="Radera" />';
print("   <input name=\"queryid\" type=\"hidden\" value=\"$row[id]\">");
print("   <input name=\"changeaction\" type=\"hidden\" value=\"$ACTION_REMOVE\">");
echo '  </td>';
echo '</tr>';
echo '</table>';
echo '</form>';
echo '<br><br>';

  } // while
}

// New query
echo '<br><br><br><h3>Ny bevakning</h3>';
echo '<form action="" method="post" name="addquery" id="addquery">';
echo '<table align="left" border="0" cellpadding="1" cellspacing="1">';
echo '        <tbody>';
echo '          <tr>';
echo '            <td>';
echo '              <input name="f_q" type="text" placeholder="S&ouml;kning" /></td>';
echo '            <td>';
                    print("<input name=\"f_maxprice\" type=\"text\" size=\"10\" maxlength=\"8\"");
                    print("placeholder=\"max pris\">");
echo '            </td>';
echo '            <td>';
echo '              <select name="f_r" size="1">';
                      foreach ($data_r as $r=>$lan) {
                        print("<option value=\"$r\"");
                        if ($r == "14") {
                          print("selected=\"selected\"");
                        }
                        print(">$lan</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_ag" size="1">';
                      foreach ($data_ag as $key=>$desc) {
                       print("<option value=\"$key\">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_st" size="1">';
                      foreach ($data_st as $key=>$desc) {
                       print("<option value=\"$key\">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_f" size="1">';
                      foreach ($data_f as $key=>$desc) {
                       print("<option value=\"$key\">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '            <td>';
echo '              <select name="f_cg" size="1">';
                      foreach ($data_cg as $key=>$desc) {
                       print("<option value=\"$key\">$desc</option>\n");
                      }
echo '              </select>';
echo '            </td>';
echo '          </tr>';
echo '        </tbody>';
echo '      </table>';
echo '<br><br>eller klistra in full ad URL nedan...<br>';
echo '<table align="left" border="0" cellpadding="1" cellspacing="1">';
echo '        <tbody>';
echo '          <tr>';
echo '            <td>';
echo '              <input name="f_url" type="text" size="132" placeholder="Full url" />';
echo '            </td>';
echo '            <td>';
                    print("<input name=\"f_maxprice\" type=\"text\" size=\"10\" maxlength=\"8\"");
                    print("placeholder=\"max pris\">");
echo '            </td>';
echo '          </tr>';
echo '        </tbody>';
echo '      </table>';
echo '<br><br>';
echo '              <input name="addbutton" type="submit" value="L&auml;gg till" />';
print("             <input name=\"changeaction\" type=\"hidden\" value=\"$ACTION_ADD\">");
echo '</form>';

?>

</body>
</html>

