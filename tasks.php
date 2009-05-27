<?php

require_once ("couchdb.php");

function get_tasks($tag) {
  try {
    $db = new CouchDB('taskbin');
    return $db->get_item('_design/taskbin/_view/by_tag?key=' . '"' . $tag . '"');
  } catch (CouchDBException $e) { 
    die($e->errorMessage() . "\n"); 
  }
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
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen, projection" />
    <script type="text/javascript" src="js/jquery.js"></script>
    <title>Tagged Tasks | taskbin</title>
  </head>
  <body>
    <div class="container">
      <?php include ("nav.php"); ?>
      <div id="tasks" class="span-16 push-1">
        <h3>Tasks tagged as <?php echo("'" . $_GET['tag'] . "'"); ?></h3>
        <ol>
        <?php
          $result = get_tasks($_GET['tag']);
          echo "<li>";
          print_r($result->getBody(true));
          echo "</li>";
        ?>
        </ol>
      </div>
      <?php include ("tags.php"); ?>
    </div>
  </body>
</html>
