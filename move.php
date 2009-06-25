<?php

require_once ("couchdb.php");
$db = new CouchDB('taskbin2');
$id = $_GET['id'];
$result = $db->get_item($id);
$rev  = json_encode($result->getBody(true)->_rev);
$task = json_encode($result->getBody(true)->task);
$tags = json_encode($result->getBody(true)->tags);
$type = json_encode($_GET['type']);
$posted = json_encode($result->getBody(true)->posted);
$updated = json_encode(date('c'));
$doc  = '{' . '"_id" : ' . json_encode($id) . ', "_rev" : ' 
  . $rev . ', "task" : ' . $task . ', "tags" : ' . $tags . ', "type" : '
  . $type . ', "updated" : ' . $updated . ', "posted" : ' . $posted . '}';

$db->update($id, $doc);

$redirect = "/replacement";

header ("Location: $redirect");

?>
