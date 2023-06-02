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

<!--At the start of the tab, then this php function runs, which checks if the user of the website have priveleges all or faq,  
    if not, then the user will not be able to get in and it'll send you back to the main page-->

<?php
    session_start();
    if($_SESSION["privileges"] != "all" && $_SESSION["privileges"] != "faq"){
        header("Location: index.php");
    }
?>

<!--HTML elements that creates the menu and a title at the top of the page-->

<div id="menumain">
      <div class="innermenu">
        <a href="admin.php">Admin</a>
      </div>

      <div class="innermenu">
        <a href="index.php"><span>Log out</span></a>
      </div>
    </div>

    <div class="menuunderline"></div>

<h1 id="h1">FAQ Homepage</h1>

<!--PHP elements that first connects to the database by including the "connect" document,
    Afterwards gets all the information from the table "FAQ" and sees if whats in there has the visibility yes,
    if so, then it runs an if statement that creates HTML elements that display and show the content in the table,
    by using forms and inputs, if the visibility is no, it does the same thing, but in a different form. If it can't
    find anything in the table, it prints a string with 0 results-->   

<?php

    include 'connect.php';
    $sql = "SELECT * FROM FAQ WHERE Visibility = 'yes'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0){
        echo "<h2>Answered Questions</h2>";
        while($row = mysqli_fetch_assoc($result)) {
            echo "
            <form method='POST' name='' action='update.php'>
            <input type='hidden' name='dbtable' value='faq'>
            <label for='type'>ID: " . $row["ID"] . "</label>
            <input type='hidden' name='id' value='" . $row["ID"] . "'>
            <label for='type'>Name</label>
            <input type='text' name='Name' style='width: 120px' value='" . $row["Name"] . "'>
            <label for='type'>Question Title</label>
            <input type='text' name='QuestionTitle' style='width: 120px' value='" . $row["QuestionTitle"] . "'>
            <label for='type'>Question</label>
            <input type='text' name='Question' style='width: 120px' value='" . $row["Question"] . "'>
            <label for='type'>Answer</label>
            <input type='text' name='Answer' style='width: 120px' value='" . $row["Answer"] . "'>
            <label for='type'>Visibility</label>
            <input type='text' name='Visibility' style='width: 120px' value='" . $row["Visibility"] . "'>
            <button type='hidden' name='action' value='update'>update</button>
            <button type='submit' name='action' value='remove'>delete</button>
            </form>";
            echo "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------";
        }
    }else {
        echo "0 results";
    }

    $sql = "SELECT * FROM FAQ WHERE Visibility = 'no'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0){
        echo "<h2>Unanswered Questions</h2>";
        while($row = mysqli_fetch_assoc($result)) {
            echo "
            <form method='POST' name='' action='update.php'>
            <input type='hidden' name='dbtable' value='faq'>
            <label for='type'>ID: " . $row["ID"] . "</label>
            <input type='hidden' name='id' value='" . $row["ID"] . "'>
            <label for='type'>Name</label>
            <input type='text' name='Name' style='width: 120px' value='" . $row["Name"] . "'>
            <label for='type'>Question Title</label>
            <input type='text' name='QuestionTitle' style='width: 120px' value='" . $row["QuestionTitle"] . "'>
            <label for='type'>Question</label>
            <input type='text' name='Question' style='width: 120px' value='" . $row["Question"] . "'>
            <label for='type'>Answer</label>
            <input type='text' name='Answer' style='width: 120px' value='" . $row["Answer"] . "'>
            <label for='type'>Visibility</label>
            <input type='text' name='Visibility' style='width: 120px' value='" . $row["Visibility"] . "'>
            <button type='hidden' name='action' value='update'>update</button>
            <button type='submit' name='action' value='remove'>delete</button>
            </form>";
            echo "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------";
        }
    }else {
        echo "0 results";
    }

    mysqli_close($conn);
  ?>

</body>
</html>