const coverImages1 = document.getElementsByClassName("pic-info1")
const coverImages2 = document.getElementsByClassName("pic-info2")
const coverImages3 = document.getElementsByClassName("pic-info3")

// set image url for fav cards

for (let image of coverImages1){
    let url = image.getAttribute("value")
   let imageLoad =`url("${url}")`
    image.style.backgroundImage = imageLoad;    
}

for (let image of coverImages2){
    let url = image.getAttribute("value")
   let imageLoad =`url("${url}")`
    image.style.backgroundImage = imageLoad;    
}

for (let image of coverImages3){
    let url = image.getAttribute("value")
   let imageLoad =`url("${url}")`
    image.style.backgroundImage = imageLoad;    
}

const favCards= document.getElementsByClassName("card-info")



