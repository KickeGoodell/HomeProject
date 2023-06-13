<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../style.css" />
    <title>Spørsmål</title>
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
          <img src="../Pictures/Snake.svg" height="100" alt="Snake Game Bilde" />
        </a>
      </div>

      <div class="innermenu">
        <a href="logIn.php">Log in</a>
      </div>
    </div>

    <div class="menuunderline"></div>

<!--HTML elements that give the user the option to create questions, set their name and title on the question-->

    <div class="container">
      <h3 id="h1">Ask your own question:</h3>
      <form id="form" method="POST" name="" action="save.php">
        <input type="hidden" name="dbTable" value="faq">
        <label>Name:</label>
        <input type='text' name='qName' style='width: 50%' placeholder="Please insert a first name">
        <label>Question title:</label>
        <input type='text' name='qTitle' style='width: 50%' placeholder="Please insert a title for your question">
        <label for='type'>Question:</label>
        <textarea name='question' cols='10' rows='5' style='width: 50%'></textarea>
        <button type="submit" name="submit" style='width: 100px' id="submitBtn">Submit</button>
      </form>
    </div>

    <div>
    <h1>Follow this link to play the game!</h1>
    <a href="github.com/KickeGoodell/HomeProject/SnakeGame/Snake.pyw"></a>
    </div>



<!--JavaScript used to create the functionality on the button, so that when you press it a message shows up-->

    <script>

      const submitBtnEl= document.getElementById("submitBtn")

      submitBtnEl.addEventListener("click", function(){
      alert("Thank you for submitting your question. Someone will reply to it shortly!");
      });

    </script>




  </body>
</html>
