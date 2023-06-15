
<!--PHP elements that first connect to the database by including the "connect" document, 
    then listen for the submit buttons from both the index page and the admin page. 
    If it detects a submit from any of these places, it takes the data or information
    you have entered on these pages and inserts it into one of the tables in the database. 
    If it fails to connect to the database, it displays "error" along with the MySQL error. 
    If it connects but does not detect a submit, it simply redirects you to the main page.-->

<?php
    include 'connect.php';

    if (isset($_POST["submit"])){
        $dbTable = mysqli_real_escape_string($conn, $_POST["dbTable"]);

        if($dbTable == "faq")
        {
        $location = "Location: index.php";
        $qName = mysqli_real_escape_string($conn, $_POST['qName']);
        $qTitle = mysqli_real_escape_string($conn, $_POST['qTitle']);
        $question = mysqli_real_escape_string($conn, $_POST['question']);

        $sql = "INSERT INTO FAQ (Name, QuestionTitle, Question) VALUES ('$qName', '$qTitle', '$question');";
        }

        if($dbTable == "WebUsers")
        {
        $location = "Location: admin.php";
        $username = mysqli_real_escape_string($conn, $_POST['Username']);
        $password = mysqli_real_escape_string($conn, $_POST['Password']);
        $privileges = mysqli_real_escape_string($conn, $_POST['Privileges']);

        $sql = "INSERT INTO WebUsers (Username, Password, Privileges) VALUES ('$username', '".password_hash($password, PASSWORD_DEFAULT)."', '$privileges');";
        }


        if(mysqli_multi_query($conn, $sql)){
            header($location);
        } else {
            echo "Error: " . $sql . "<br>" . mysqli_error($conn);
        }
    
    }else {
        header("Location: index.php");
    }

?>
