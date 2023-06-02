<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css" />
    <title>Admin Page</title>
</head>
<body>

<!--At the start of the tab, then this php function runs, which checks if the user of the website have priveleges all,  
    if not, then the user will not be able to get in and it'll send you back to the main page-->

<?php
    session_start();
    if($_SESSION["privileges"] != "all"){
        header("Location: index.php");
    }
?>

<!--HTML elements that creates a menu and title on the page-->

<div id="menumain">
      <div class="innermenu">
        <a href="admin.php">Admin</a>
      </div>

      <div class="innermenu">
        <a href="index.php"><span>Log out</span></a>
      </div>
    </div>

    <div class="menuunderline"></div>

<h1 id="h1">Account information</h1>

<!--PHP elements that first connects to the database by using the include "connect" command,
    where connect is a different document. Afterwards it grabs all the information from the table "WebUsers" in the database,
    and then finally creates html elements that will place all the information it finds in the table-->

  <?php

    include 'connect.php';
    $sql = 'SELECT * FROM WebUsers';
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0){
      echo "<h2>Admin Users</h2>";
      while($row = mysqli_fetch_assoc($result)) {
        echo "
        <form method='POST' name='' action='update.php'>
        <input type='hidden' name='dbtable' value='user'>
        <label for='type'>ID: " . $row["ID"] . "</label>
        <input type='hidden' name='id' value='" . $row["ID"] . "'>
        <label for='type'>Username:</label>
        <input type='text' name='username' style='width: 120px' value='" . $row["Username"] . "'>
        <label for='type'>New Password:</label>
        <input type='text' name='password' style='width: 120px' value=''>
        <label>Privileges:</label>
        <input type='text' name='privileges' style='width: 45px' value='" . $row["Privileges"] . "'>
        <button type='hidden' name='action' value='update'>update</button>
        <button type='submit' name='action' value='remove'>delete</button>
        </form>";
        echo "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------";
      }
    } else {
      echo "0 results";
    }

    mysqli_close($conn);
  ?>

<!--HTML elements that create a form that gives the option to create multiple users in the page-->

  <form method="POST" name="" action="save.php">
    <input type="hidden" name="dbTable" value="WebUsers">
    <label>Username:</label>
    <input type="text" name="Username" style='width: 120px;'>
    <label for="type">Password:</label>
    <input type="text" name="Password" id="password" style='width: 120px'>
    <label>Privileges:</label>
    <input type="text" name="Privileges" style='width: 45px'>
    <button type="submit" name="submit">Save</button>
  </form>

</body>
</html>