<?php

require_once("couchdb.php");

function get_task($id) {
  $db = new CouchDB('taskbin');
  $response = $db->get_item($id);
  return $response->getBody(true) ? $response->getBody(true) : array();
}

$task = get_task($_GET['id']);

print_r ($task->tags);

?>
