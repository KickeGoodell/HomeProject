<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="../style.css" />
    <title>FAQ</title>
  </head>
  <body>

<!--HTML elements that creates the menu at the top of the page-->

    <div id="menumain">
      <div class="innermenu">
        <a href="faq.php"><span class="ColoredText">FAQ</span></a>
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

<!--PHP elements that first connects to the database by including the "connect" document,
    afterwards it grabs all the information from the table "FAQ" in the database, then it creates
    the HTML elements that will use the information it found in the table. Finally it creates a button,
    that can be pressed to show answer and title-->

  <?php

  include "connect.php";
  $sql = "SELECT * FROM `FAQ`";
  $result = mysqli_query($conn, $sql);
echo "<div class='questionContainer'>";
  if (mysqli_num_rows($result) > 0){
    while($row = mysqli_fetch_assoc($result)) {
      if ($row["Visibility"] == "yes") {
        echo "
        <div class='contentContainer'>
        <button type='button' class='collapseFaq'>" . $row["QuestionTitle"] . "</button>
        <div class = 'faqContent'>
          <h3>" . $row["Name"] . "</h3>
          <p>" . $row["Question"] . "</p>
          <h4>" . $row["Answer"] . "</h3>
        </div>
        </div>
        ";
      }
    }
  }
  echo "</div>";
?>

<!--JavaScript that is required to make the functionality to the buttons-->

<script>

  var collFaqEl = document.getElementsByClassName("collapseFaq");
  
  for (var i = 0; i < collFaqEl.length; i++) {
    collFaqEl[i].addEventListener("click", function() {
      this.classList.toggle("faqActive");
      var faqContent = this.nextElementSibling;
      if (faqContent.style.display === "block") {
        faqContent.style.display = "none";
      } else {
        faqContent.style.display = "block";
      }
    });
  }
</script>

  </body>
</html>
