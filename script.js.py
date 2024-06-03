// script.js
const wordContainer = document.getElementById('word-container');
const wrongLettersContainer = document.getElementById('wrong-letters-container');
const letterInput = document.getElementById('letter-input');
const restartButton = document.getElementById('restart-button');

const words = ['python', 'javascript', 'hangman', 'developer', 'programming'];
let selectedWord = '';
let correctLetters = [];
let wrongLetters = [];

function selectRandomWord() {
    selectedWord = words[Math.floor(Math.random() * words.length)];
}

function displayWord() {
    wordContainer.innerHTML = selectedWord
        .split('')
        .map(letter => (correctLetters.includes(letter) ? letter : '_'))
        .join(' ');
}

function updateWrongLetters() {
    wrongLettersContainer.textContent = `Wrong Letters: ${wrongLetters.join(', ')}`;
}

function checkGameStatus() {
    if (!wordContainer.textContent.includes('_')) {
        setTimeout(() => alert('Congratulations! You won!'), 100);
    } else if (wrongLetters.length >= 6) {
        setTimeout(() => alert(`Sorry! You lost! The word was '${selectedWord}'`), 100);
    }
}

letterInput.addEventListener('input', () => {
    const letter = letterInput.value.toLowerCase();
    if (selectedWord.includes(letter)) {
        if (!correctLetters.includes(letter)) {
            correctLetters.push(letter);
        }
    } else {
        if (!wrongLetters.includes(letter)) {
            wrongLetters.push(letter);
        }
    }
    letterInput.value = '';
    displayWord();
    updateWrongLetters();
    checkGameStatus();
});

restartButton.addEventListener('click', () => {
    correctLetters = [];
    wrongLetters = [];
    selectRandomWord();
    displayWord();
    updateWrongLetters();
    letterInput.focus();
});

selectRandomWord();
displayWord();
letterInput.focus();