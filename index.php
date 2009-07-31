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
        $("form").submit(function(element) {
          element.preventDefault();
        });
      });
    </script>
    <title>Welcome | taskbin</title>
    <style>
      #send label { font-weight: normal; }
      form p { margin-bottom: 32px; }
      input[type='submit'] { font-size: 12px; }
    </style> 
  </head>
  <body>
    <div class="container">
      <div id="header" class="span-18 push-3 last">
        <h2 class="site_id"><a href="index.php">taskbin</a></h2>
      </div>
      <div id="new" class="span-18 push-3 last main_content">
        <div style="padding: 24px;">
          <form action="new.php" method="post">
            <p>
              <label for="task">New Task</label><br />
              <input type="text" id="task" name="task" class="big" size="48" maxlength="48" />
            </p>
            <p>
              <label for="tags">Tags</label><br />
              <input type="text" id="tags" class="big" size="48" maxlength="48" />
            </p>
            <p class="submit">
              <input type="submit" name="submit" value="Post" />
            </p>
          </div>
        </form>
      </div>
      <div id="footer" class="span-18 push-3 last"></div>
    </div>
  </body>
</html>
