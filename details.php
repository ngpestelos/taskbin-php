<?php

$id = $_GET['id'];

require_once("couchdb.php");
$db = new CouchDB('taskbin');
$result = $db->get_item($id);
$task = $result->getBody(true)->task;
$type = $result->getBody(true)->type;
$tags = $result->getBody(true)->tags;

function move_url($_id, $_type) {
  return "move.php?id=" . $_id . "&type=" . $_type;
}

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" href="css/screen.css" type="text/css" media="screen, projection" />
    <link rel="stylesheet" href="css/print.css" type="text/css" media="print" />
    <!--[if IE]><link rel="stylesheet" href="css/ie.css" type="text/css" media="screen, projection" /><![endif]-->
    <title>Task Details | taskbin</title>
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen" />
    <style>
      #send span { font-size: 12px; font-weight: bold; }
      #send label { font-weight: normal; }
    </style>
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <?php include("nav.php"); ?>
      <div id="details" class="main_content span-14 push-1">
        <h3><?php echo $task . " ($type)"; ?></h3>
        <h5>Tags</h5>
        <ul>
          <?php
            foreach ($tags as $t) {
              echo "<li>";
              echo $t;
              echo "</li>";
            }
          ?>
        </ul>
        <h5>Move</h5>
        <ul>
          <li><a href="<?php echo move_url($id, 'next'); ?>">Next</a></li>
          <li><a href="<?php echo move_url($id, 'someday'); ?>">Someday</a></li>
          <li><a href="<?php echo move_url($id, 'trash'); ?>">Trash</a></li>
        </ul>
      </div>
      <?php include("tags.php"); ?>
      <?php include("footer.php"); ?>
    </div>
  </body>
</html>
