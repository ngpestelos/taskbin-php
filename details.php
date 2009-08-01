<?php

$id = $_GET['id'];

require_once("couchdb.php");
$db = new CouchDB('taskbin');
$result = $db->get_item($id);
$task = $result->getBody(true)->task;
$type = $result->getBody(true)->type;
$tags = $result->getBody(true)->tags;

function move($_id, $_type) {
  echo "move.php?id=" . $_id . "&type=" . $_type;
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
    <title>Details | taskbin</title>
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen" />
    <style>
      h5 { font-size: 13px; margin-bottom: 4px; font-weight: normal; font-style: italic; }
    </style>
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <div id="details" class="span-18 push-3 last main_content">
        <div class="pad_24">
          <h5 id="type"><?php echo $type; ?></h5>
          <h3><?php echo str_replace("\'", "'", $task); ?></h3>
          <h4>Tags</h4>
          <ul>
          <?php
            foreach ($tags as $t) {
              echo "<li>";
              echo $t;
              echo "</li>";
            }
          ?>
          </ul>
          <h4>Move</h4>
          <ul>
            <li><a href="<?php move($id, 'next'); ?>">Next</a></li>
            <li><a href="<?php move($id, 'someday'); ?>">Someday</a></li>
            <li><a href="<?php move($id, 'trash'); ?>">Trash</a></li>
          </ul>
        </div>
      </div>
    </div>
  </body>
</html>
