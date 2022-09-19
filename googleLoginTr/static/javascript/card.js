const YesButton = document.getElementsByClassName('yes')[0]
const form = document.querySelector('form')
const formId = document.querySelector('#formId')
const formRedirect = document.querySelector('#formRedirect')
const formSubmit = document.querySelector('#formSubmit')
let IdsToSubmit = ""
let IdsSubmitted = 0;
let UpFirst = false;
let startNumber =9;
let cardsDismissed =0
formRedirect.value=""

const NoButton = document.querySelector('.no')
let total = -1;

class Card {
	constructor({ id,imageUrl,name,sights,mapUrl, onDismiss, onLike, onDislike,description,width, total }) {
		this.id = id;
		this.imageUrl = imageUrl;
		this.name = name;
		this.sights = sights;
		this.mapUrl = mapUrl;
		this.onDismiss = onDismiss;
		this.onLike = onLike;
		this.onDislike = onDislike;
		this.description = description;
		this.width = width;
		this.total = total;

		this.#init();
	}



	// private properties
	#startPoint;
	#offsetX;
	#offsetY;

	#isTouchDevice = () => {
		return (
			"ontouchstart" in window ||
			navigator.maxTouchPoints > 0 ||
			navigator.msMaxTouchPoints > 0
		);
	};

	#init = () => {

		const card = document.createElement("div");
		card.classList.add("card");
		card.setAttribute("value" , this.id)

		
		//going into cardGreet
		const cardGreet = document.createElement("div");
		cardGreet.classList.add("card-greet");

		card.append(cardGreet)
		
		const GreetContent = document.createElement("div");
		GreetContent.classList.add("content");

		cardGreet.append(GreetContent)

		const GreetContentPic0 = document.createElement("div");
		GreetContentPic0.classList.add("pic");
		GreetContentPic0.classList.add("pic0");
		GreetContentPic0.classList.add("visible");
		GreetContentPic0.style.backgroundImage = `url(${this.imageUrl[0]})` ;

		const GreetContentPic1 = document.createElement("div");
		GreetContentPic1.classList.add("pic");
		GreetContentPic1.classList.add("pic1");
		GreetContentPic1.style.backgroundImage = `url(${this.imageUrl[1]})` ;

		const GreetContentPic2 = document.createElement("div");
		GreetContentPic2.classList.add("pic");
		GreetContentPic2.classList.add("pic2");
		GreetContentPic2.style.backgroundImage = `url(${this.imageUrl[2]})` ;

		const GreetContentName = document.createElement("div");
		GreetContentName.classList.add("name");
		GreetContentName.textContent = this.name;

		const moreInfoButton = document.createElement("div");
		moreInfoButton.classList.add("more-info-button");

		const moreInfoButtonSpan = document.createElement("span");
		moreInfoButtonSpan.classList.add("material-symbols-outlined");
		moreInfoButtonSpan.innerText= "info";
		moreInfoButtonSpan.innerHTML=  "\n                            info";
		this.cardFlip1 = moreInfoButtonSpan;

		moreInfoButton.append(moreInfoButtonSpan)

		GreetContent.append(GreetContentPic0)
		GreetContent.append(GreetContentPic1)
		GreetContent.append(GreetContentPic2)
		GreetContent.append(GreetContentName)
		GreetContent.append(moreInfoButton)


		//going into cardInfo
		const cardInfo = document.createElement("div");
		cardInfo.classList.add("card-info");
		cardGreet.classList.add("visible");

		card.append(cardInfo)

		const InfoContent = document.createElement("div");
		InfoContent.classList.add("content-info"); //come back here

		cardInfo.append(InfoContent)

		const InfoPic0 = document.createElement("div");
		InfoPic0.classList.add("pic-info");
		InfoPic0.classList.add("pic-info0");
		InfoPic0.classList.add("visible");
		InfoPic0.style.backgroundImage = `url(${this.imageUrl[0]})` ;

		const InfoPic1 = document.createElement("div");
		InfoPic1.classList.add("pic-info");
		InfoPic1.classList.add("pic-info1");
		InfoPic1.style.backgroundImage = `url(${this.imageUrl[1]})` ;

		const InfoPic2 = document.createElement("div");
		InfoPic2.classList.add("pic-info");
		InfoPic2.classList.add("pic-info2");
		InfoPic2.style.backgroundImage = `url(${this.imageUrl[2]})` ;


		InfoContent.append(InfoPic0)
		InfoContent.append(InfoPic1)
		InfoContent.append(InfoPic2)

		const InfoDestination = document.createElement("div");
		InfoDestination.classList.add("destination-info");

		const InfoName = document.createElement("div");
		InfoName.classList.add("name-info");

		const InfoNameLink = document.createElement("a");
		InfoNameLink.href=this.mapUrl;
		InfoNameLink.textContent = this.name;

		const InfoBack = document.createElement("span");
		InfoBack.classList.add("material-symbols-outlined");
		InfoBack.classList.add("back-info-button");
		InfoBack.innerText="keyboard_return";

		this.cardFlip2 = InfoBack;

		InfoName.append(InfoNameLink)
		InfoName.append(InfoBack)

		InfoDestination.append(InfoName)

		const InfoDescription = document.createElement("div");
		InfoDescription.classList.add("description-info");
		InfoDescription.textContent = this.description;

		InfoDestination.append(InfoDescription)

		const InfoHr = document.createElement("hr");
		InfoHr.classList.add("style-six");

		InfoDestination.append(InfoHr)

		const InfoSights = document.createElement("div");
		InfoSights.classList.add("sights-info");

		const InfoSightstext = document.createElement("div");
		InfoSightstext.innerText="Sights";
		InfoSightstext.innerHTML="Sights";

		const InfoSightsUl = document.createElement("ul");

		for (let i=0 ; i<10; i++){
			if (this.sights[i] != undefined){
				let  InfoSightsLi = document.createElement("li");
				InfoSightsLi.textContent = this.sights[i]
				InfoSightsUl.append(InfoSightsLi)
			}
		}

		InfoSights.append(InfoSightstext)
		InfoSights.append(InfoSightsUl)

		InfoDestination.append(InfoSights)
		InfoContent.append(InfoDestination)

		const InfoEmpty = document.createElement("div");
		InfoEmpty.classList.add("emptyspace-info");

		InfoDestination.append(InfoEmpty)

		InfoDestination.append(InfoEmpty)

		const nopeStamp = document.createElement("div");
		nopeStamp.classList.add("nopeStamp");
		nopeStamp.textContent = "NOPE"

		card.append(nopeStamp)

		const yesStamp = document.createElement("div");
		yesStamp.classList.add("yesStamp");
		yesStamp.textContent = "YES"

		card.append(yesStamp)
		card.style.zIndex = -1 * this.total;
		card.setAttribute("name", -1 * this.total)



		


		this.element = card;
		this.CardYes = yesStamp;
		this.CardNope = nopeStamp;
		this.cardFront = cardGreet;
		this.cardBack = cardInfo;
		this.EntireCard = card;
		this.placeNameGreet = GreetContentName;

		if (this.#isTouchDevice()) {
			this.#listenToTouchEvents();
			this.#listenToMouseEvents();
			
		} else {
			this.#listenToMouseEvents();
		}
	};

	#listenToTouchEvents = () => {
		this.element.addEventListener("touchstart", (e) => {
			const touch = e.changedTouches[0];
			if (!touch) return;
			const { clientX, clientY } = touch;
			this.#startPoint = { x: clientX, y: clientY };
			document.addEventListener("touchmove", this.#handleTouchMove);
			this.element.style.transition = "transform 0s";
		});

		document.addEventListener("touchend", this.#handleTouchEnd);
		document.addEventListener("cancel", this.#handleTouchEnd);
	};

	#listenToMouseEvents = () => {
		this.element.addEventListener("mousedown", (e) => {
			const { clientX, clientY } = e;
			this.#startPoint = { x: clientX, y: clientY };
			document.addEventListener("mousemove", this.#handleMouseMove);
			this.element.style.transition = "transform 0s";
		});


		document.addEventListener("mouseup", this.#handleMoveUp);

	
		// prevent card from being dragged
		this.element.addEventListener("dragstart", (e) => {
			e.preventDefault();
		});


	};


	#handleMove = (x, y) => {
		this.#offsetX = x - this.#startPoint.x;
		this.#offsetY = y - this.#startPoint.y;
		const rotate = this.#offsetX * 0.1;
		this.element.style.transform = `translate(${this.#offsetX}px, ${
			this.#offsetY
		}px) rotate(${rotate}deg)`;


		
		// dismiss card
		if (Math.abs(this.#offsetX) > this.element.clientWidth * 0.7) {
			this.#dismiss(this.#offsetX > 0 ? 1 : -1);
		}

		 this.WasOffsetX = this.#offsetX

		
		
		if (this.#offsetX < 0){
			this.CardNope.classList.add("visible")
			this.CardYes.classList.remove("visible")

	
		} else if(this.#offsetX >0) {
			this.CardYes.classList.add("visible")
			this.CardNope.classList.remove("visible")


		}

	};

	// mouse event handlers
	#handleMouseMove = (e) => {
		e.preventDefault();
		if (!this.#startPoint) return;
		const { clientX, clientY } = e;
		this.#handleMove(clientX, clientY);
	};

	#handleMoveUp = () => {
		// this.#startPoint = null;
		document.removeEventListener("mousemove", this.#handleMouseMove);
		this.element.style.transform = "";


		if(this.WasOffsetX <0){
			this.CardNope.classList.remove("visible")

		}else if (this.WasOffsetX >0){
			this.CardYes.classList.remove("visible")

		}

		
	};

	// touch event handlers
	#handleTouchMove = (e) => {
		if (!this.#startPoint) return;
		const touch = e.changedTouches[0];
		if (!touch) return;
		const { clientX, clientY } = touch;
		this.#handleMove(clientX, clientY);
	};

	#handleTouchEnd = () => {
		this.#startPoint = null;
		document.removeEventListener("touchmove", this.#handleTouchMove);
		this.element.style.transform = "";

		
		
	};

	#dismiss = (direction , source ="not") => {
		
		
		this.#startPoint = null;
		document.removeEventListener('mouseup', this.#handleMoveUp);
		document.removeEventListener('mousemove', this.#handleMouseMove);
		document.removeEventListener('touchend', this.#handleTouchEnd);
		document.removeEventListener('touchmove', this.#handleTouchMove);
		this.element.style.transition = 'transform 1s';
		this.element.style.transform = `translate(${direction * window.innerWidth}px, ${this.#offsetY}px) rotate(${90 * direction}deg)`;
		this.element.classList.add('dismissing');
		setTimeout(() => {
		  this.element.remove();
		}, 200);

		IdsSubmitted++
		if(IdsSubmitted ==10){
			
			
			form.submit()
		}

		UpFirst = true;

		if(source != "button"){
			if (typeof this.onDismiss === 'function') {
				this.onDismiss();
			  }
			  if (typeof this.onLike === 'function' && direction === 1) {
				console.log("like")

				IdsToSubmit += "/" + this.id
				formId.value = IdsToSubmit
				

				

				this.onLike();
			  }
			  if (typeof this.onDislike === 'function' && direction === -1) {
				this.onDislike();
			  }
		}else{
			if (typeof this.onDismiss === 'function') {
				this.onDismiss();
			}
			  
			  if ( direction == 1) {
				this.onLike();

				

				console.log("like")
			  }
			  if ( direction == -1) {
				this.onDislike();
		}


		
	location.reload()
		
	};

	



	
	
}


}
