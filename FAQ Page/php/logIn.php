<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../style.css" />
    <title>Log In</title>
  </head>
  <body>

<!--PHP element that runs a if statement that checks if the user have privileges, 
    if the user does, then they are deleted-->

  <?php
  session_start();
    if(isset($_SESSION['privileges'])){
      unset($_SESSION['privileges']);
    }
?>

<!--HTML elements that creates the menu at the top of the page-->

    <div id="menumain">
      <div class="innermenu">
        <a href="faq.php">FAQ</a>
      </div>

      <div class="innermenu">
        <a href="index.php">
          <img src="../Pictures/Snake.svg" height="100" alt="Enrique Logo" />
        </a>
      </div>

      <div class="innermenu">
        <a href="logIn.php"><span class="ColoredText">Log in</span></a>
      </div>
    </div>

    <div class="menuunderline"></div>

<!--HTML elements that are made to give you the option to log into the page, You do that
    by placing in info to a user and then press the sumbit button-->

    <div class="container">
    <h3>Please Log In</h3>
    <form method="post" id="form">
      <label for="Username">Username:</label>
      <input type="text" name="Username" /><br />
      <label for="Password">Password:</label>
      <input type="Password" name="Password" /><br />
      <button type="submit" value="Log in" name="submit" class="loginSubmit">Submit</button>
    </form>
    </div>

<!--PHP elements that first connects to the database by including the "connect" document,
    Afterwards it listens for a "submit", if it finds it, then it turns the data you wrote in the log in
    and turns it into variables. After that, it gets all the information from the table "WebUsers" and sees
    if what you put in matches with what exists in the database. If it connect at all to the database, it gives
    up, if what you wrote in does match with a existing user, then you get a incorrect string, if you have connection
    and what you put in is correct, then you log in and are sent to the admin page-->

    <?php
      include 'connect.php';

      if(isset($_POST['submit'])){
        
        $usrn = mysqli_real_escape_string($conn, $_POST['Username']);
        $pwd = mysqli_real_escape_string($conn, $_POST['Password']);

        $sql = "SELECT * FROM WebUsers where Username='$usrn'";

        $result = mysqli_query($conn, $sql)
          or die('Error connecting to database.');

        if (mysqli_num_rows($result) > 0 ) {
          while($row = mysqli_fetch_assoc($result)) {
            if ($row["Password"] == $pwd) {
              $_SESSION["privileges"] = $row["Privileges"];
              header("Location: admin.php");
            } else {
              echo '<p>feil brukernavn eller passord</p>';
            }
          }
        } else {
          echo '<p>feil brukernavn eller passord</p>';
        }
      }
    ?>

  </body>
</html>
