<?php

require_once("couchdb.php");
$db = new CouchDB('taskbin');
$result = $db->get_item('_design/tags/_view/count?group=true');
$rows = $result->getBody(true)->rows;

?>
<ul>
<?php
  foreach ($rows as $r) {
    echo "<li>";
    echo "<a href=\"tagdetail.php?id=" . urlencode($r->key) . "\">" . $r->key . "</a>";
    echo "</li>";
  }
?>  
</ul>
