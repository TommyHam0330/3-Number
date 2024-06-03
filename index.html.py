<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hangman Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Hangman Game</h1>
    <div id="game-container">
        <p id="word-container"></p>
        <p id="wrong-letters-container"></p>
        <input type="text" id="letter-input" maxlength="1" autofocus>
        <button id="restart-button">Restart Game</button>
    </div>
    <script src="script.js"></script>
</body>
</html>