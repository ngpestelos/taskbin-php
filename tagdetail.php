<?php

// id is URL encoded

$key = json_encode(urlencode($_GET['id']));

require_once ("couchdb.php");
$db = new CouchDB('taskbin');
$result = $db->get_item('_design/tags/_view/tasks?key=' . $key);
//print_r($result);
$rows = $result->getBody(true)->rows;

?>
<h2>Tagged as '<?php echo($_GET['id']); ?>'</h2>
<ul>
  <?php
    foreach ($rows as $r) {
      echo "<li>";
      echo $r->value->task;
      echo "</li>";
    }
  ?>
</ul>
<a href=".">Home</a>
