<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" href="css/screen.css" type="text/css" media="screen, projection" />
    <link rel="stylesheet" href="css/print.css" type="text/css" media="print" />
    <!--[if IE]><link rel="stylesheet" href="css/ie.css" type="text/css" media="screen, projection" /><![endif]-->
    <link rel="stylesheet" href="css/main.css" type="text/css" media="screen, projection" />
    <script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript">
      $(document).ready(function() {  
        $("#task").focus();
      });
    </script>
    <title>Welcome | taskbin</title>
    <style>
      #send span { font-size: 12px; font-weight: bold; }
      #send label { font-weight: normal; }
      .submit { margin-top: 36px; }
    </style> 
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <?php include("nav.php"); ?>
      <div id="new" class="main_content span-16 push-3">
        <form action="new.php" method="post">
          <p>
            <label for="task" class="mid">New Task</label><br />
            <input type="text" id="task" name="task" class="big" 
              size="48" maxlength="48" />
          </p>
          <p>
            <label for="new_tags" class="mid">Tags</label><br />
            <input type="text" id="new_tags" size="24" maxlength="24"
              class="big" name="new_tags" />
          </p>
          <p id="send">
            <span>Send To</span><br />
            <label for="inbox">
              <input type="radio" id="inbox" name="type" value="inbox" checked />Inbox
            </label>
            <label for="next">
              <input type="radio" id="next" name="type" value="next" />Next
            </label>
            <label for="someday">
              <input type="radio" id="someday" name="type" value="someday" />Someday
            </label>
          </p>
          <p class="submit">
            <input type="submit" name="submit" value="Submit" />
          </p>
        </form>
      </div>
      <div id="tags" class="span-4 last">
        <h4>Tags</h4>
        <?php include("tags.php"); ?>
      </div>
      <?php include("footer.php"); ?>
    </div>
  </body>
</html>
