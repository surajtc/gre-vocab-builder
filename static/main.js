const FolderPath = "Decks/"
const MaxDeckNumber = 5

var Deck = {}
var DeckNumber = 01

function updateStats() {
  stats = document.querySelector(".stats")
  // console.log(stats)

  cards = document.getElementById("cards").querySelectorAll(".cards__card")
  var newWord = 0
  var knownWord = 0
  var unknownWord = 0
  var know
  for (var i = 0; i < cards.length; i++) {
    know = parseInt(cards[i].querySelector("span").innerHTML)

    if (know === -1) {
      newWord++
    } else if (know === 0) {
      unknownWord++
    } else if (know === 1) {
      knownWord++
    }
  }
  // console.log(newWord, knownWord, unknownWord)
  stats.children[0].innerHTML = String(newWord).padStart(2, "0")
  stats.children[1].innerHTML = String(knownWord).padStart(2, "0")
  stats.children[2].innerHTML = String(unknownWord).padStart(2, "0")
}

function show(elem, color, know) {
  parent = elem.parentElement.parentElement
  parent.querySelector(".cards__card__context").style.borderColor = color
  parent.querySelector("h3").style.color = color

  parent.querySelector("p").style.display = "block"

  parent.querySelector("span").innerHTML = know

  updateStats()
}

function hide(elem) {
  elem.style.display = "none"
}

function deckPath(number) {
  return FolderPath + "Deck" + String(number).padStart(2, "0") + ".csv"
}

function changeDeck(pos = 0) {
  DeckNumber = DeckNumber + pos

  document.querySelector(".deck__name").innerHTML =
    "DECK " + String(DeckNumber).padStart(2, "0")

  if (DeckNumber === 1) {
    document.querySelector(".btn-left").style.visibility = "hidden"
  } else if (DeckNumber === MaxDeckNumber) {
    document.querySelector(".btn-right").style.visibility = "hidden"
  } else {
    document.querySelector(".btn-left").style.visibility = "visible"
    document.querySelector(".btn-right").style.visibility = "visible"
  }

  statsWrap = document.querySelector(".stats")
  stats = statsWrap.querySelectorAll("h4")
  for (var i = 0; i < stats.length; i++) {
    stats[i].innerHTML = "00"
  }

  Deck = {}

  cardsWrap = document.querySelector("#cards")
  cards = cardsWrap.querySelectorAll(".cards__card")
  for (var i = 0; i < cards.length; i++) {
    cards[i].remove()
  }

  fetch(deckPath(DeckNumber))
    .then((response) => response.text())
    .then((csv) => {
      function createDeck(line) {
        let [word, ...meaning] = line.split(",")
        meaning = meaning
          .join(",")
          .trim()
          .replace(/^\"+|\"+$/g, "")

        Deck[word] = meaning
      }

      const lines = csv.split("\n")
      lines.forEach(createDeck)

      cardTemplate = document.querySelector(".cards__card")
      cards = document.querySelector("#cards")
      // console.log(cardTemplate)
      let count = 1
      // console.log(statsWrap.children[1], Object.keys(Deck).length)
      statsWrap.firstElementChild.innerHTML = Object.keys(Deck).length
      statsWrap.lastElementChild.innerHTML = Object.keys(Deck).length
      for (var item in Deck) {
        // console.log(item, "---", Deck[item])
        card = cardTemplate.querySelector(".cards__card__context")
        number = card.querySelector("h4")
        word = card.querySelector("h3")
        meaning = card.querySelector("p")
        number.innerHTML = String(count++).padStart(2, "0")
        word.innerHTML = item
        meaning.innerHTML = Deck[item]
        cards.appendChild(cardTemplate.cloneNode(true))
      }
      // cardTemplate.style.display = "none"
    })
}

changeDeck()
// var fs = require("fs")
// list = fs.readdir("/resources")
// console.log(list)

// var fileInput = document.getElementById("myfiles")
// console.log(fileInput.files[0])
// fileInput.addEventListener("change", function (event) {
//   var input = event.target

//   for (var i = 0; i < input.files.length; i++) {
//     console.log(input.files[i].name)
//   }
// })
