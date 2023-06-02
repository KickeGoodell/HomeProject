<!--Sets up the communication to the database server-->

<?php
$IP = "10.2.2.195";                                                          // Creates a variable with the IP address to the server
$username = "enrique";                                                       // Creates a variable with the username to the mysql user I am connecting to 
$password = "d9g[4k/Pphr10w00";                                              // Creates a variable with the password to the mysq user I am connecting to
$database = "Arsoppgave";                                                    // Creates a variable with the name of the database I am connecting to

$conn = mysqli_connect($IP, $username, $password, $database);                // Creates a variable with the mysqli_connect function by using the variables I created above

if (!$conn) {                                                                // If statement that runs if you can't connect
    die("Connection to the database failed") . mysqli_connect_error();       // If it can't connect, then it will stop trying, and then create a string and the mysql erro function
}
?>




