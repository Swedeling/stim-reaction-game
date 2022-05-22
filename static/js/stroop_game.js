let wordParagraph = document.getElementById(`wordParagraph`)
let startButton = document.getElementById(`startButton`)
let colorButtons = document.getElementsByClassName(`color`)
let counter = document.getElementById(`counter`);
let reactionTime = document.getElementById(`reactionTime`);

let count = 0
let amount = 3
let startTime
let roundStart
let correctAnswers = 0
let wrongAnswers = 0

startButton.addEventListener(`click`, start)

for (let button of colorButtons) {
  button.addEventListener(`click`, selectColor)
}

function start() {
  startButton.style.display = `none`

  for (let button of colorButtons) {
    button.style.display = `inline`
  }

  correctAnswers = 0
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

  if (count <= amount)
  {
    roundStart = Date.now()
    roundTimeout = setTimeout(pickRandomColor, 3000);
  }
  else
  {
    let time = (Date.now() - startTime) / 1000
    wordParagraph.innerHTML = `Time: ${time} seconds. Correct answers: ${correctAnswers}. Wrong answers: ${amount - correctAnswers}.`
    gameOver()
  }

}

function selectColor() {
  if (this.innerHTML == wordParagraph.style.color)
  {
    correctAnswers = correctAnswers + 1
    //dodac do tablicy czas
  }
  else
  {
    //nie dodawać i guess
  }
  reactionTime.innerHTML = `Reaction time: ${(Date.now() - roundStart)/1000} seconds`
  clearTimeout(roundTimeout)
  pickRandomColor()
}

//bedzie do wyrzucenia
function gameOver() {
  wordParagraph.style.color = `black`
  startButton.style.display = `inline`

  clearTimeout(roundTimeout)

  for (let button of colorButtons) {
    button.style.display = `none`
  }
}