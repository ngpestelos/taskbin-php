<?php

$type = $_GET['type'];
$tag  = $_GET['tag'];

require_once ("couchdb.php");
$db = new CouchDB('taskbin');
$result = $db->get_item('_design/tasks/_view/' . $type);

$total_rows = $result->getBody(true)->total_rows;
$rows = $result->getBody(true)->rows;
$rows = array_reverse($rows);
$title = isset($type) ? $type : $tag;
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" href="css/screen.css" type="text/css" media="screen, projection" />
    <link rel="stylesheet" href="css/print.css" type="text/css" media="print" />
    <!--[if IE]><link rel="stylesheet" href="css/ie.css" type="text/css" media="screen, projection" /><![endif]-->
    <title>Tasks | taskbin</title>
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen" />
    <style>
      #tasks li { margin-bottom: 8px; }
    </style>
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <div id="tasks" class="span-18 push-3 last main_content">
        <div class="pad_24">
          <h3><?php echo ucfirst($title) . " ($total_rows)"; ?></h3>
          <?php
            if ($total_rows > 0) {
              echo "<ol>";
              foreach ($rows as $r) {
                echo "<li>";
                $task = str_replace("\'", "'", $r->value->task);
                echo "<a href=\"details.php?id=" . $r->value->_id . "\">" . $task . "</a>";
                echo "</li>";
              }
              echo "</ol>";
            }
          ?>
        </div>
      </div>
    </div>
  </body>
</html>
