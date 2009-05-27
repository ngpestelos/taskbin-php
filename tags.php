<?php

require_once ("couchdb.php");

function get_tags() {
  try {
    $db = new CouchDB('taskbin');
    return $db->get_item('_design/taskbin/_view/tags');
  } catch (CouchDBException $e) {
    die($e->errorMessage() . "\n");
  }
}

?>

<div id="tags" class="span-24">
<hr />
<ul>
<?php
$result = get_tags();
foreach ($result->getBody(true)->rows as $tag) {
  echo "<li>";
  echo '<a href="tasks.php?tag=' . urlencode($tag->value->name) . '">';
  echo($tag->value->name);
  echo "</a>";
  echo "</li>";
}
?>
</ul>
</div>
