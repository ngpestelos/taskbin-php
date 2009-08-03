<?php

require_once("couchdb.php");
$db = new CouchDB('taskbin');
$tasks = $db->get_item('_design/tags/_view/tasks?key="' . $_GET['id'] . '"');
$rows = $tasks->getBody(true)->rows;

# TODO Separate tasks by type
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
    <script type="text/javascript">
    </script>
    <title>Tagged Tasks | taskbin</title>
    <style>
      #tasks li { margin-bottom: 8px; }
    </style> 
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <div id="tasks" class="span-18 push-3 last main_content">
        <div class="pad_24">
          <h3>Tagged as '<?php echo $_GET['id']; ?>'</h3>
          <ul>
          <?php
            foreach ($rows as $r) {
              $task = $r->value->task;
              $type = $r->value->type;
              $url = "details.php?id=" . $r->value->_id;
              echo "<li>";
              echo "<a href='" . $url . "'>" . $task . "</a>";
              echo "</li>";
            }
          ?>
          </ul>
        </div>
      </div>
    </div>
  </body>
</html>
