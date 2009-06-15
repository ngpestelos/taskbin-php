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
      body {
        font-family: Verdana, sans-serif;
        color: #22222B;
      }
      #nav { text-align: right; }
      #nav ul { list-style: none; }
      #nav li { display: inline; }
      #header { border-bottom: 1px solid #797979; }
      .site_id { margin-top: 5px; color #797979; }
      #footer { margin-top: 256px; border-top: 1px solid #797979; }
      /*#new { margin-top: 4px; border: 1px solid green; }*/
      #new { margin-top: 24px; }
      #tags { margin-top: 24px; border: 1px solid red; }
      #send span { font-size: 12px; font-weight: bold; }
      #send label { font-weight: normal; }
      .big { font-size: 18px; }
      .mid { font-size: 14px; }
      .submit { margin-top: 36; }
    </style> 
  </head>
  <body>
    <div class="container">
      <?php include("header.php"); ?>
      <div id="new" class="span-14 push-1">
        <form action="new.php" method="post">
          <p>
            <label for="task" class="mid">New Task</label><br />
            <input type="text" id="task" name="task" class="big" 
              size="47" maxlength="47" />
          </p>
          <p>
            <label for="new_tags" class="mid">Tags</label><br />
            <input type="text" id="new_tags" size="36" maxlength="36"
              class="mid" name="new_tags" />
          </p>
          <p id="send">
            <span>Send To</span><br />
            <label for="inbox">
              <input type="radio" id="inbox" name="type" value="inbox" checked />Inbox
            </label>
            <label for="someday">
              <input type="radio" id="someday" name="type" value="someday" />Someday
            </label>
            <label for="next">
              <input type="radio" id="next" name="type" value="next" />Next
            </label>
          </p>
          <p class="submit">
            <input type="submit" name="submit" value="Submit" />
          </p>
        </form>
      </div>
      <?php include("tags.php"); ?>
      <?php include("footer.php"); ?>
    </div>
  </body>
</html>
