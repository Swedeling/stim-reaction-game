let wordParagraph = document.getElementById(`wordParagraph`)
let startButton = document.getElementById(`startButton`)
let colorButtons = document.getElementsByClassName(`color`)
let counter = document.getElementById(`counter`);

let count = 0
let startTime
let amount = 10

startButton.addEventListener(`click`, start)

for (let button of colorButtons) {
  button.addEventListener(`click`, selectColor)
}

function start() {
  startButton.style.display = `none`

  for (let button of colorButtons) {
    button.style.display = `inline`
  }

  count = 0
  counter.innerHTML = `Stage: ${count} / ${amount}`
  startTime = Date.now()
  pickRandomColor()
}

function pickRandomColor() {
  //check if word and color can have the same value in real life stroop test
  //add if clause
  //timer for each try
  //startRound - zakosić
  let randomNumber = Math.floor(Math.random() * colorButtons.length)
  wordParagraph.innerHTML = colorButtons[randomNumber].innerHTML

  randomNumber = Math.floor(Math.random() * colorButtons.length)
  wordParagraph.style.color = colorButtons[randomNumber].innerHTML

  count = count + 1
  counter.innerHTML = `Stage: ${count} / ${amount}`
}

function selectColor() {
  if (this.innerHTML == wordParagraph.style.color) {
    if (count < amount) {
      pickRandomColor()
    } else {
      let time = (Date.now() - startTime) / 1000
      wordParagraph.innerHTML = `Time: ${time} seconds`
      gameOver()
    }
  } else {
    wordParagraph.innerHTML = `You lose`
    gameOver()
  }
}

//bedzie do wyrzucenia
function gameOver() {
  wordParagraph.style.color = `black`
  startButton.style.display = `inline`

  for (let button of colorButtons) {
    button.style.display = `none`
  }
}