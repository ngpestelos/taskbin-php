<?php

require_once ("couchdb.php");

function get_task($id) {
  $db = new CouchDB('taskbin');
  $response = $db->get_item($id);
  return $response->getBody(true) ? $response->getBody(true) : array();
}

$task = get_task($_GET['id']);

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
    <title>Task Details | taskbin</title>
  </head>
  <body>
    <div class="container">
      <?php include ("nav.php"); ?>
      <div id="tasks" class="span-16 push-1 append-7">
        <h3>Task Details</h3>
        <p><?php echo $task->task . " (" . $task->type . ")"; ?></p>
        <p><?php echo $task->updated; ?></p>
        <p><?php echo $task->posted; ?></p>
        <p><?php print_r($task); ?></p>
        <p>
          Tags
          <ul>

          </ul>
        </p>
      </div>
      <?php include ("tags.php"); ?>
    </div>
  </body>
</html>
