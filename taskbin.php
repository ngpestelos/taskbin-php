<?

require_once("couchdb.php");


/*
try {
  $result = $db->get_item('_design/taskbin/_view/next');
} catch (CouchDBException $e) {
  die($e->errorMessage()."\n");
}

$all_docs = $result->getBody(true);
//print_r($all_docs->rows);
foreach ($all_docs->rows as $next) {
  print_r($next->value) . "<br />";
}*/

function get_tasks($type) {
  try {
    $db = new CouchDB('taskbin');
    $result = $db->get_item('_design/taskbin/_view/' . $type);
  } catch (CouchDBException $e) {
    die($e->errorMessage() . "\n");
  }

  $all_docs = $result->getBody(true);
  print_r($all_docs);
}

?>
