let cardNumber = 0;
let currentcardNumber = 0;
let YesNoRemoved =0;

const moreInfoButton = document.getElementsByClassName("more-info-button");
const backButton = document.getElementsByClassName("back-info-button");
const cardFront = document.getElementsByClassName("card-greet");
const cardBack = document.getElementsByClassName("card-info");
const cardWhole = document.getElementsByClassName("card");
const Greetpic0 = document.getElementsByClassName("pic0");
const Greetpic1 = document.getElementsByClassName("pic1");
const Greetpic2 = document.getElementsByClassName("pic2");

const Infopic0 = document.getElementsByClassName("pic-info0");
const Infopic1 = document.getElementsByClassName("pic-info1");
const Infopic2 = document.getElementsByClassName("pic-info2");


const navbrand = document.querySelector("#navbrand");
const navswipe = document.querySelector("#navswipe");
const navfav = document.querySelector("#navfav");
const navlogout = document.querySelector("#navlogout");
IdsToSubmit =""


// yes button, add card id to the form and if a certain amount added submit the form or if a certain amount of cards swiped submit the form

     YesButton.addEventListener("click", function(e){

        IdsToSubmit += "/" + cardWhole[currentcardNumber].getAttribute("value")
        console.log(cardWhole[currentcardNumber].getAttribute("value"))
        formId.value = IdsToSubmit
        IdsSubmitted++
       
        


        YesNoRemoved++;
        cardWhole[currentcardNumber].style.transition = 'transform 1s';
        cardWhole[currentcardNumber].style.transform = `translate(${1 * window.innerWidth}px, ${0}px) rotate(${90 * 1}deg)`;
       
        cardWhole[currentcardNumber].classList.add('dismissing');
        currentcardNumber = currentcardNumber +1;


        setTimeout(() => {
            Greetpic0[cardNumber].style.backgroundImage =""
            cardWhole[cardNumber].classList.add('dismissed');
            if(cardWhole[cardNumber].classList.contains('visible') ){
                cardWhole[cardNumber].style.display = "none"
            }

            cardWhole[cardNumber].remove();
            
            cardNumber = 0;
           
           

        }, 200);

        currentcardNumber = 0;

        if(YesNoRemoved == startNumber -1 ){

            form.submit()
          
        }


        if(IdsSubmitted ==10 -1){
            form.submit()
        }

        
        
    
    })


    // no button, add card id to the form and if a certain amount added submit the form or if a certain amount of cards swiped submit the form

    NoButton.addEventListener("click", function(){
        YesNoRemoved++;
        cardWhole[currentcardNumber].style.transition = 'transform 1s';
        cardWhole[currentcardNumber].style.transform = `translate(${-1 * window.innerWidth}px, ${0}px) rotate(${90 * -1}deg)`;
        cardWhole[currentcardNumber].classList.add('dismissing');
        currentcardNumber = currentcardNumber + 1;
        
        setTimeout(() => {
            Greetpic0[cardNumber].style.backgroundImage =""
            cardWhole[cardNumber].classList.add('dismissed');
            if(cardWhole[cardNumber].classList.contains('visible') ){
                cardWhole[cardNumber].style.display = "none"
            }

            cardWhole[cardNumber].remove();
            
           
            cardNumber = 0;

            
           
           

        }, 200);

        currentcardNumber = 0;

        if(YesNoRemoved == startNumber -1){
            form.submit()
           

        }
        

        if(IdsSubmitted ==10 -1){
            console.log(IdsToSubmit)
            
            form.submit()
        }

       
        
    })


   



//when clicked the image changes for greet card and info card
for (let i = 0; i < startNumber; i++) {
    moreInfoButton[i].addEventListener("click", function(){
        cardFront[0].classList.toggle("visible");
        cardBack[0].classList.toggle("visible");
        console.log(i)
        console.log('clicked')
    })
    
    backButton[i].addEventListener("click", function(){
        cardFront[0].classList.toggle("visible");
        cardBack[0].classList.toggle("visible");
    })


    Greetpic0[i].addEventListener("click", function(){
        Greetpic0[0].classList.toggle("visible")
        Greetpic1[0].classList.toggle("visible")
        console.log("backgorund image")
        console.log(Greetpic0[i].style.backgroundImage)
    
      
        
    })
    Infopic0[currentcardNumber].addEventListener("click", function(){
        Infopic0[0].classList.toggle("visible")
        Infopic1[0].classList.toggle("visible")
    })
    
    Greetpic1[i].addEventListener("click", function(){
        Greetpic1[0].classList.toggle("visible")
        Greetpic2[0].classList.toggle("visible")
    })
    Infopic1[i].addEventListener("click", function(){
        Infopic1[0].classList.toggle("visible")
        Infopic2[0].classList.toggle("visible")
    })
    
    Greetpic2[i].addEventListener("click", function(){
        Greetpic2[0].classList.toggle("visible")
        Greetpic0[0].classList.toggle("visible")
    })
    Infopic2[i].addEventListener("click", function(){
        Infopic2[0].classList.toggle("visible")
        Infopic0[0].classList.toggle("visible")
    })
    

//check if tab is active and if not , submit the form
      document.addEventListener("visibilitychange", (event) => {
        if (document.visibilityState == "visible" &&  formId.value != "") {
          console.log("tab is active")
          form.submit()
        } else {
          console.log("tab is inactive")
        }
      });



//redirects and form submit for the nav bar clicks
navbrand.addEventListener("click" , function(){
form.submit()
})

navswipe.addEventListener("click" , function(){
form.submit()
})

navfav.addEventListener("click" , function(){
formRedirect.value="favourites"
form.submit()

})

navlogout.addEventListener("click" , function(){
formRedirect.value="logout"
form.submit()

})



    
