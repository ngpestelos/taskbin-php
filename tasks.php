<?php

$type = $_GET['type'];

require_once ("couchdb.php");
$db = new CouchDB('taskbin2');
$result = $db->get_item('_design/t/_view/' . $type);
$total_rows = $result->getBody(true)->total_rows;
$rows = $result->getBody(true)->rows;

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
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <div id="tasks" class="span-14 push-1">
        <h3>
          <?php
            if ($total_rows == 0)
              echo "Found 0 items";
            else if ($total_rows == 1)
              echo "Found 1 item";
            else
              echo "Found " . $total_rows . " items";
          ?>
        </h3>
        <?php
          if ($total_rows > 0) {
            echo "<ol>";
            foreach ($rows as $r) {
              echo "<li>";
              echo $r->value->task;
              echo "</li>";
            }
            echo "</ol>";
          }
        ?>
      </div>
      <?php include("tags.php"); ?>
      <?php include("footer.php"); ?>
    </div>
  </body>
</html>
