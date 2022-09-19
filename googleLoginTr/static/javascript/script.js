const swiper = document.querySelector("#swiper");
const like = document.querySelector("#like");
const dislike = document.querySelector("#dislike");





// function for random integer between two numbers
function randomIntFromInterval(min, max) { // min and max included 
	return Math.floor(Math.random() * (max - min + 1) + min)
}

// initialising rndInt
let rndInt = 3

// variables
let cardCount = 0;

// functions
function appendNewCard(rndInt ,name, id, map, description,images,sights , width, total) {
	const card = new Card({ 

		imageUrl: images,
		id: id,
		name: name,
		mapUrl: map,
		description: description,
		sights: sights,
		width: width,
		total: total,
		
		onDismiss: cardInfo,
		
		onLike: () => {
			like.style.animationPlayState = "running";
			like.classList.toggle("trigger");
		},
		onDislike: () => {
			dislike.style.animationPlayState = "running";
			dislike.classList.toggle("trigger");
		},
	});
	swiper.append(card.element);

	cardCount++;

	const cards = swiper.querySelectorAll(".card:not(.dismissing)");
	cards.forEach((card, index) => {
		card.style.setProperty("--i", 0);
	});
}

// first X cards
for (let i = 0; i < startNumber; i++) {
	total = total +1
	rndInt = randomIntFromInterval(0, 49);

	let images =[]
	let sights =[]



		let name = destinations[rndInt]['name']



		let id = destinations[rndInt]['id']


		let map = destinations[rndInt]['map']
	


		let description = destinations[rndInt]['description']



	//try catch for images of destination
	try {
		 images = [
			JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['images'])).split("},")).split("original':")[1].split("'")[1],
			JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['images'])).split("},")).split("original':")[2].split("'")[1],
			JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['images'])).split("},")).split("original':")[3].split("'")[1]
		]
	  }
	  catch(err) {
		 images = ["https://i.pinimg.com/736x/69/90/0e/69900e95e2d9e2ca0956a126155bbc31--photography-people-portrait-faces-photography.jpg",
					"https://images.unsplash.com/photo-1624711517157-25991163e537?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cG9ydHJhaXQlMjBwaG90b2dyYXBoeXxlbnwwfHwwfHw%3D&w=1000&q=80",
					"https://burst.shopifycdn.com/photos/fashion-model-in-fur.jpg?width=1200&format=pjpg&exif=1&iptc=1"
					 ]
	}

	//try catch for sights of destination
try{
	if (destinations[rndInt]['sights'] != ''){
		
		 sights =[]
		let length = JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['sights'])).split("},")).split("title':").length
		for (let i = 1; i < length; i++) {
			sights.push(JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['sights'])).split("},")).split("title':")[i].split("'")[1])
		  }
	}
	}catch{
		 sights = [] 
	}

	appendNewCard(rndInt ,name, id, map, description,images,sights, $(window).width() , total);

}


function cardInfo(){
	total =total +1;
	rndInt = randomIntFromInterval(0, 49);

	let images =[]
	let sights =[]


		let name = destinations[rndInt]['name']

		let id = destinations[rndInt]['id']

		let map = destinations[rndInt]['map']


		let description = destinations[rndInt]['description']



	//try catch for images of destination
	try {
		 images = [
			JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['images'])).split("},")).split("original':")[1].split("'")[1],
			JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['images'])).split("},")).split("original':")[2].split("'")[1],
			JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['images'])).split("},")).split("original':")[3].split("'")[1]
		]
	  }
	  catch(err) {
		 images = ["https://i.pinimg.com/736x/69/90/0e/69900e95e2d9e2ca0956a126155bbc31--photography-people-portrait-faces-photography.jpg",
					"https://images.unsplash.com/photo-1624711517157-25991163e537?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cG9ydHJhaXQlMjBwaG90b2dyYXBoeXxlbnwwfHwwfHw%3D&w=1000&q=80",
					"https://burst.shopifycdn.com/photos/fashion-model-in-fur.jpg?width=1200&format=pjpg&exif=1&iptc=1"
					 ]
	}

	//try catch for sights of destination
try{
	if (destinations[rndInt]['sights'] != ''){
		
		 sights =[]
		let length = JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['sights'])).split("},")).split("title':").length
		for (let i = 1; i < length; i++) {
			sights.push(JSON.stringify(JSON.parse(JSON.stringify(destinations[rndInt]['sights'])).split("},")).split("title':")[i].split("'")[1])
		  }
	}
	}catch{
		 sights = [] 
	}

	appendNewCard(rndInt ,name, id, map, description,images,sights, $(window).width(), total);
}



