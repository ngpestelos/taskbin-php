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
        $("#q").focus();
      });
    </script>
    <title>Welcome | taskbin</title>
    <style>
      #nav { text-align: right; }
      #nav ul { list-style: none; }
      #nav li { display: inline; }
      #q_form { margin-top: 48px; }
      #q_search { margin-left: 8px; margin-right: 4px; }
    </style> 
  </head>
  <body>
    <div class="container">
      <?php include("nav.php"); ?>
      <div id="q_form" class="span-14 push-5">
        <form method="post" action="taskbin.php">
          <fieldset>
            <legend>taskbin</legend>
            <input type="text" name="q" id="q" size="47" maxlength="57" />
            <input id="q_search" name="q_button" type="submit" value="Search" />
            <input id="q_new" name="q_button" type="submit" value="New Task" />
          </fieldset>
        </form>
      </div>
      <?php include("tags.php"); ?>
    </div>
  </body>
</html>
