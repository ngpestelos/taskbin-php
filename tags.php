<?php

require_once("couchdb.php");
$db = new CouchDB('taskbin');
$result = $db->get_item('_design/tag_counts/_view/all?group=true');
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
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen, projection" />
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript">
    </script>
    <title>Tags | taskbin</title>
    <style>
      #tags li { margin-bottom: 8px; }
    </style> 
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <div id="tags" class="span-18 push-3 last main_content">
        <div class="pad_24">
          <h3>Tags</h3>
          <ul>
          <?php
            foreach ($rows as $r) {
              echo "<li>";
              echo "<a href=\"tagged.php?id=" . urlencode($r->key) . "\">" . $r->key . "</a>";
              echo "</li>";
            }
          ?>
          </ul> 
        </div>
      </div>
    </div>
  </body>
</html>
