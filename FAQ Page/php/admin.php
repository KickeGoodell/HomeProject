<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css">
    <title>Admin</title>
</head>
<body>

<!--At the start of the tab, then this php function runs, which checks if the user of the website have priveleges all,  
    if not, then the user will not be able to get in and it'll send you back to the main page-->

<?php
    session_start();
    if($_SESSION["privileges"] != "all" && $_SESSION["privileges"] != "faq"){
        header("Location: index.php");
    }
?>

<!--HTML elements that creates the meny at the top of the page-->

<div id="menumain">
      <div class="innermenu">
        <a href="manageFaq.php">Manage FAQ</a>
      </div>

      <div class="innermenu">
        <a href="accounts.php"><span>Accounts</span>
        </a>
      </div>

      <div class="innermenu">
        <a href="index.php"><span>Log out</span></a>
      </div>
    </div>

    <div class="menuunderline"></div>

</body>
</html>