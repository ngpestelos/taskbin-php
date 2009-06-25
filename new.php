<?php

$tags = explode(',', $_POST['new_tags']);
$stripped = array();
foreach ($tags as $t) {
  $stripped[] = trim($t);
}

$task = json_encode($_POST['task']);
$tags = json_encode($stripped);
$type = json_encode($_POST['type']);
$posted = json_encode(date('D M j G:i:s Y'));
$updated = $posted;
$doc  = '{' . '"task" : ' . $task . ', "tags" : ' . $tags 
  . ', "type" : ' . $type . ', "posted" : ' . $posted
  . ', "updated" : ' . $updated . '}';

require_once ("couchdb.php");
$db = new CouchDB('taskbin');
$db->create($doc);

$redirect = "/replacement";

header("Location: $redirect"); 

?>
