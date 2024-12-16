<?php
include_once("config.php");
if (array_key_exists("name", $_POST)&&
    array_key_exists("title", $_POST) &&
    array_key_exists("message", $_POST)) {
  $message="from: " . $_POST["name"] . "\nsubject: " . $_POST["title"] . "\nmessage: " . $_POST["message"];
  $written = file_put_contents($all_messages_file, $message.PHP_EOL.PHP_EOL , FILE_APPEND | LOCK_EX);
  $written = file_put_contents($messages_file, $message.PHP_EOL.PHP_EOL , FILE_APPEND | LOCK_EX);
  if ($written) {
    echo("<font color='green'>Message sent! We will get back to you. Might not if you're a lawyer though!<br><br></font>");
  }
  else {
    echo("<font color='red'>Something went wrong with sending the message :(<br><br></font>");
  }
}
?>
<form action="contact.php" method="post">
  <div class="elem-group">
    <label for="name">Your Name</label>
    <input type="text" id="name" name="name" placeholder="John Doe" pattern=[A-Z\sa-z]{3,20} required>
  </div>
  <div class="elem-group">
    <label for="email">Your E-mail</label>
    <input type="email" id="email" name="email" placeholder="john.doe@email.com" required>
  </div>
  <div class="elem-group">
    <label for=role-selection">Choose your role</label>
    <select id="role-selection" name="role" required>
        <option value="">Select a role</option>
        <option value="uploader">Uploader</option>
        <option value="leecher">Leecher</option>
        <option value="lawyer">Lawyer</option>
    </select>
  </div>
  <div class="elem-group">
    <label for="title">Reason For Contacting Us</label>
    <input type="text" id="title" name="title" required placeholder="e.g. rom not found!" pattern=[A-Za-z0-9\s]{8,60}>
  </div>
  <div class="elem-group">
    <label for="message">Write your message</label>
    <textarea id="message" name="message" placeholder="State your business!" required></textarea>
  </div>
  <button type="submit">Send Message</button>
</form>
