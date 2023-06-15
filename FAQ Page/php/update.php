
<!--PHP elements that first connect to the database by including the "connect" document, 
    then listen for action buttons from the admin page. If it hears an action, 
    it should give you the opportunity to change the data that was previously displayed,
    to what you have edited on the admin page. If it listens for "remove," 
    it should delete all data from the table, then close the database connection and 
    send you back to the page you were on.
    If it listens for update on user, it should update the table WebUser, then close the database
    connection and send you back to the page you were on,
    if it listens for update on faq, it should update the table FAQ, then close the database
    connection and send you back to the page you were on,
    If it fails to do so, 
    it should still close the connection and display an error
    If you mysteriously managed to access this page, it should simply state 
    "You are not supposed to be here."-->

<?php
    include 'connect.php';

    if (isset($_POST["action"])){
        $dbtable = $_POST['dbtable'];
        $id = $_POST['id'];
        if ($dbtable == 'user'){
        $location = "Location: admin.php";
        if ($_POST["action"] == 'update'){
            $username = mysqli_real_escape_string($conn, $_POST['username']);
            $password = mysqli_real_escape_string($conn, $_POST['password']);
            $privileges = mysqli_real_escape_string($conn, $_POST['privileges']);
            if(empty($password)){
                $sql = "UPDATE WebUsers SET Username = '$username' , Privileges = '$privileges' WHERE ID='$id';"; 
            } else {
                $sql = "UPDATE  WebUsers SET Username = '$username' , Password = '".password_hash($password, PASSWORD_DEFAULT)."' , Privileges = '$privileges' WHERE ID='$id';";
            }
        }   
    } else if($dbtable == 'faq'){
        $location = 'Location: manageFaq.php';
        if ($_POST["action"] == 'update'){
            $Name = mysqli_real_escape_string($conn, $_POST['Name']);
            $QuestionTitle = mysqli_real_escape_string($conn, $_POST['QuestionTitle']);
            $Question = mysqli_real_escape_string($conn, $_POST['Question']);
            $Answer = mysqli_real_escape_string($conn, $_POST['Answer']);
            $Visibility = mysqli_real_escape_string($conn, $_POST['Visibility']);
            

            $sql = "UPDATE FAQ SET Name = '$Name', QuestionTitle = '$QuestionTitle', Question = '$Question', Answer = '$Answer', Visibility = '$Visibility' WHERE ID='$id';";
        }
    }
    if ($_POST["action"] == 'remove'){
        if ($dbtable == 'user'){
            $sql = "DELETE FROM WebUsers WHERE ID ='$id';";
        } else if($dbtable == 'faq'){ 
            $sql = "DELETE FROM FAQ WHERE ID ='$id';";
        }
    }
    if (mysqli_query($conn, $sql)){
        mysqli_close($conn);
        header($location);
        } else {
            echo "Error";
            mysqli_close($conn);
        }
} else{
    echo '<p> You are not supposed to be here! </p>';
}
