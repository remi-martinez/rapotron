<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Rapotron</title>
  <link rel="icon" href="img/micro.png"/>
  <link rel="stylesheet" href="style_rapotron.css">
  <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
  <link href="https://fonts.googleapis.com/css?family=Lato|Roboto|Roboto+Condensed|Roboto+Mono|Roboto+Slab&display=swap" rel="stylesheet">
  <script src="main.js"></script>
</head>
<body>
  <div class="container" style="display:none;">
    <div class="center">
      <div id='punchline'>
        <blockquote></blockquote>
      </div>
      <div id='auteurs'></div>

      <div id='generer_button'>
        <div class="leftchoice">
          <img id="lDamso" src="img/damso.png" class="selected">
          <img id="lOrelsan" src="img/orelsan.png">
          <img id="lNekfeu" src="img/nekfeu.png" style="width:100px">
        </div>
        <div class="btn">Générer</div>
        <div class="rightchoice">
          <img id="rDamso" class="imgflip" src="img/damso.png">
          <img id="rOrelsan" class="imgflip selected" src="img/orelsan.png">
          <img id="rNekfeu" class="imgflip" src="img/nekfeu.png" style="width:100px">
        </div>
      </div>
    </div>
  </div>
  <footer>&copy;2020 - Antoine & Rémi</footer>
</body>
</html>