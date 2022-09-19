const searchResults = document.querySelector(".searchResults")
const Infopic1 = document.getElementsByClassName("pic-info1");
const Infopic2 = document.getElementsByClassName("pic-info2");
const Infopic3 = document.getElementsByClassName("pic-info3");
const AllFavCards = document.getElementsByClassName("card-info");

const navbrand = document.querySelector("#navbrand");
const navswipe = document.querySelector("#navswipe");
const navfav = document.querySelector("#navfav");
const navlogout = document.querySelector("#navlogout");



// nav bar click redirects
navbrand.addEventListener("click" , function(){
  console.log("brand")
  window.location.href = "/"
  })
  
  navswipe.addEventListener("click" , function(){
      console.log("swiper")

  window.location.href = "/"
  })
  
  navfav.addEventListener("click" , function(){
      console.log("fav")

      window.location.href = "/favourites"
  
  })
  
  navlogout.addEventListener("click" , function(){
      console.log("logout")

      window.location.href = "/logout"
  
  })

// adding data to the fav cards

let firsthtml = '';
for (let fav of array) {

//start to add thing from card
  firsthtml += '<div class="card-info visible " value="'+fav[0]['id']+'">'
  firsthtml += '<div class="content-info">'
  let image1 = fav[0]['images'].split("'original': '")[1].split("', 'is_product' ")[0].split("'")[0]
  if (image1 ==undefined){
    image1 = "https://uxdesign.cc/how-to-design-a-404-error-page-that-keeps-users-on-your-site-f3443a980ece"
  }
  let image2 = fav[0]['images'].split("'original': '")[2].split("', 'is_product' ")[0].split("'")[0]
  if (image2 ==undefined){
    image2 = "https://uxdesign.cc/how-to-design-a-404-error-page-that-keeps-users-on-your-site-f3443a980ece"
  }
  let image3 = fav[0]['images'].split("'original': '")[3].split("', 'is_product' ")[0].split("'")[0]
  if (image3 ==undefined){
    image3 = "https://uxdesign.cc/how-to-design-a-404-error-page-that-keeps-users-on-your-site-f3443a980ece"
  }
  firsthtml += '<div value="'+image1+'" class="pic-info1"></div>'
  firsthtml += '<div value="'+image2+'" class="pic-info2 invisible"></div>'
  firsthtml += '<div value="'+image3+'" class="pic-info3 invisible"></div>'
 
  firsthtml += '<div class="destination-info">'
  firsthtml += '<div class="name-info">'
  firsthtml += '<a href="'+fav[0]['map']+'">'+fav[0]['name']+'</a>'
  firsthtml += '</div>'
  firsthtml += '<div class="description-info">'+fav[0]['description']+'</div>'
  firsthtml += '<hr class="style-six">'
  firsthtml += '<div class="sights-info">'
  firsthtml += '<div>Sights</div>'
  firsthtml += '<ul>'

  // put in all the sights in the li , different locations have differnent numbers of sights
    for (let i=0; i<10 ; i++){
    
      if( fav[0]['sights']== undefined){
        }
      else if( fav[0]['sights'].split("},")[i]== undefined){
        }
      else if( fav[0]['sights'].split("},")[i].split("{'title': '")[1]== undefined){
      }else{
        sight = fav[0]['sights'].split("},")[i].split("{'title': '")[1].split("', 'link':")[0]
        firsthtml += '<li>'+sight+'</li>'
      }
    
  }
  
  firsthtml += '</ul></div>'
  firsthtml += '<div class="emptyspace-info"></div>'
  firsthtml += '</div></div></div>'

  }

searchResults.innerHTML = firsthtml;
let cardsWithInfo = searchResults.getElementsByClassName("card-info")

let input = document.querySelector('input');


// look for change in the input and set it a value
input.addEventListener("input", e => {
  const value = e.target.value.toLowerCase()

  if(value == ""){
    
  for (let favCard of favCards){
    
      favCard.style.display ="grid"
    }
  for (let card of cardsWithInfo){
  card.style.display= "grid"   
}

  } 
  else{
    let results = array.filter( (fav) => {
   
      return fav[0]['name'].toLowerCase().includes(value)
      
    })
    for (let card of cardsWithInfo){
      card.setAttribute("in","no");
    }
    
      for (let card of cardsWithInfo){
        for (let result of results) {

          console.log( card.getAttribute('value') + "  : " + result[0]['id'] + " " + result[0]['name'] )
          
          // if value is no, it gets skipped over since it was already done and proven to not have the value in it
          if(card.getAttribute('value') == result[0]['id'] || card.getAttribute("in") == "yes"){
            card.style.display= "grid"
            card.setAttribute("in","yes");
            
          } else{
            card.style.display= "none"
          }
      
       
      } 
    }
  }

})

// on click change the image shown

  for (let i = 0; i < AllFavCards.length; i++) {

    Infopic1[i].addEventListener("click", function(){
      console.log("tocu")
      Infopic1[i].classList.toggle("invisible")
      Infopic2[i].classList.toggle("invisible")

  })

  Infopic2[i].addEventListener("click", function(){
    Infopic2[i].classList.toggle("invisible")
    Infopic3[i].classList.toggle("invisible")
})

Infopic3[i].addEventListener("click", function(){
  
  Infopic3[i].classList.toggle("invisible")
  Infopic1[i].classList.toggle("invisible")
})
  }



  
function delay (URL) {
  setTimeout( function() { window.location = URL }, 300 );
}
