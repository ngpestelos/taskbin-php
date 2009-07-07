<?php

require_once("couchdb.php");

$db = new CouchDB('taskbin');
$tasks = $db->get_item('_design/tags/_view/tasks?key=' . '"' . $_GET['tag'] . '"');
$rows = $tasks->getBody(true)->rows;

# TODO Separate tasks by type
?>
<ul>
<?php
  foreach ($rows as $r) {
    $task = $r->value->task;
    $type = $r->value->type;
    $url = "details.php?id=" . $r->value->_id;
    echo "<li>";
    echo "<a href=\"" . $url . "\">" . $task . "</a>" . " (" . $type . ")";
    echo "</li>";
  }
?>
</ul>
