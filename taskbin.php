<?

require_once("couchdb.php");

function get_task($id) {
  $db = new CouchDB('taskbin');
  $response = $db->get_item($id);
  return $response->getBody(true) ? $response->getBody(true)->rows : array();
}

?>
