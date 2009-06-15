<?php

$tags = explode(',', $_POST['new_tags']);
$stripped = array();
foreach ($tags as $t) {
  $stripped[] = trim($t);
}

$task = json_encode($_POST['task']);
$tags = json_encode($stripped);
$bin  = json_encode($_POST['bin']);
$doc  = '{' . '"task" : ' . $task . ', "tags" : ' . $tags . ', "bin" : ' . $bin . '}';

require_once ("couchdb.php");
$db = new CouchDB('taskbin2');
$db->create($doc);

$redirect = "/replacement";

header("Location: $redirect"); 

?>
