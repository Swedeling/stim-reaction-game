let wordParagraph = document.getElementById(`wordParagraph`)
let startButton = document.getElementById(`startButton`)
let colorButtons = document.getElementsByClassName(`color`)
let counter = document.getElementById(`counter`);
let reactionTime = document.getElementById(`reactionTime`);
let instructionButton = document.getElementById(`instructions`)
let title=document.getElementById(`title`)
let summary=document.getElementById(`summary`)
let results=document.getElementById(`results`)

let good_answers=document.getElementById(`good_answers`)
let bad_answers=document.getElementById(`bad_answers`)
let avg_speed=document.getElementById(`avg_speed`)

let submitter=document.getElementById(`submitter`)


let count = 0
let amount = 20
let startTime
let roundStart
let correctAnswers = 0
let wrongAnswers = 0
let reactionsSum = 0


startButton.addEventListener(`click`, start)

for (let button of colorButtons) {
  button.addEventListener(`click`, selectColor)
}

function start() {
  title.style.display=`block`
  summary.style.display=`block`
  counter.style.display=`block`
  reactionTime.style.display=`none`
  wordParagraph.style.display=`block`


  results.style.display = `none`
  startButton.style.display = `none`
  instructionButton.style.display = `none`

  for (let button of colorButtons) {
    button.style.display = `inline`
  }

  correctAnswers = 0
  count = 1
  reactionsSum = 0
  counter.innerHTML = `Stage: ${count} / ${amount}`
  startTime = Date.now()
  pickRandomColor()
}

function pickRandomColor() {
  let randomNumber = Math.floor(Math.random() * colorButtons.length)
  wordParagraph.innerHTML = colorButtons[randomNumber].innerHTML

  randomNumber = Math.floor(Math.random() * colorButtons.length)
  wordParagraph.style.color = colorButtons[randomNumber].innerHTML

  counter.innerHTML = `Stage: ${count} / ${amount}`

  if (count <= amount)
  {
    count = count + 1
    roundStart = Date.now()
    roundTimeout = setTimeout(pickRandomColor, 3000);
  }
  else
  {
    let time = (Date.now() - startTime) / 1000
    wordParagraph.innerHTML = `Time: ${time} seconds. Correct answers: ${correctAnswers}. Wrong answers: ${amount - correctAnswers}.`
    if (correctAnswers == 0) {
    results.innerHTML = `No correct responses.\n Correct answers: ${correctAnswers}.\n Wrong answers: ${amount - correctAnswers}.`

    } else {
    results.innerHTML = `Correct response average time: ${(reactionsSum/correctAnswers).toFixed(2)} seconds.\n Correct answers: ${correctAnswers}.\n Wrong answers: ${amount - correctAnswers}.`
    }
    gameOver()
  }

}

function selectColor() {
  if (this.innerHTML == wordParagraph.style.color)
  {
    correctAnswers = correctAnswers + 1
    reactionsSum = reactionsSum + (Date.now() - roundStart)/1000
  }
  reactionTime.innerHTML = `Reaction time: ${(Date.now() - roundStart)/1000} seconds`
  reactionTime.style.display=`none`

  clearTimeout(roundTimeout)
  pickRandomColor()
}

function gameOver() {
  title.style.display=`none`
  summary.style.display=`none`
  counter.style.display=`none`
  reactionTime.style.display=`none`
  wordParagraph.style.display=`none`

  wrapper.style.display = `block`
  results.style.display = `block`
  startButton.style.display = `inline`
  startButton.innerHTML = `Play again`

  clearTimeout(roundTimeout)

  for (let button of colorButtons) {
    button.style.display = `none`
  }

  good_answers.value = correctAnswers
  bad_answers.value = amount - correctAnswers
  avg_speed.value = reactionsSum/correctAnswers

  submitter.style.display = `block`

}
