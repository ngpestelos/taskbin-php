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
      echo '<a href="details.php?id=' . $r->value->_id . '">';
      echo stripslashes($r->value->task);
      echo "</a>" . " (" . $r->value->type . ")";
      echo "</li>";
    }
  ?>
</ul>
<a href=".">Home</a>
