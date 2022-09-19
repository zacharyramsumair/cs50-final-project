const favCardTemplate = document.querySelector("[data-fav-template]")
const favCardContainer = document.querySelector("[data-fav-cards-container]")
const searchResults = document.querySelector(".searchResults")
let favs = []


// get the input into the form on the favourites page and check each card there if they contain the input entered

let input = document.querySelector('input');

input.addEventListener("input", e => {

  const value = e.target.value.toLowerCase()

  let results = array.filter( (fav) => {
   
    return fav[0]['name'].toLowerCase().includes(value)
    
  })

  favs = results.map(fav => {
    const card = favCardTemplate.content.cloneNode(true).children[0]
    const header = card.querySelector("[data-header]")
    const body = card.querySelector("[data-body]")
    
    header.textContent = fav[0]['name']
    body.textContent = fav[0]['description']
    favCardContainer.append(card)
    return { name: fav.name, email: fav.description, element: card }
  })

})



