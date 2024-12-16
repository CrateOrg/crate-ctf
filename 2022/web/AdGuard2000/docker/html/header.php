<?php
echo '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">';
echo '';
echo '<html>';
echo '<head>';
echo '';
echo '<title>';
echo $title;
echo '</title>';
echo '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">';
echo '<link href="style.css" rel="stylesheet" type="text/css"/>';
echo '<body>';
echo '<div class="Header">';
echo 'Adguard 2000';
echo '</div>';

echo '<div class="Menu">';

if (isset($_SESSION['currentuser'])) {
  if ($_SESSION['currentuid'] == 9) {
    // The administrator has logged in.
    echo '<a class="Menu" href="manageusers.php">Hantera users</a>';
    echo " | ";
  }
  else {
    // Regular user logged in.
    echo '<!-- will only be activated when admin is logged in <a class="Menu" href="manageusers.php">Hantera users</a> | -->';
  }

  echo '<a class="Menu" href="manage.php">Hantera bevakningar</a>';
  echo "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
  echo '<a class="Menu" href="logout.php">Logout ' .$_SESSION['currentuser']. '</a>';
}

echo '</div>';
?>
