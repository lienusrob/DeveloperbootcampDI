// let para = document.getElementsByTagName("p")
// let article = document.querySelector("article")
// console.log(para)
​
​
// for (var i = 0; i < para.length; i++) {
// 	para[i].setAttribute("class", "para_article")
// }
​
// article.removeChild(para[3])
​
// let h2 = document.querySelector("h2")
​
// h2.addEventListener("click", function() {
// 	h2.remove()
// })
​
// let h1 = document.querySelector("h1")
// h1.style.fontSize = Math.floor(Math.random() * 101) + "px";
​
// para[0].addEventListener("click", function(){
// 	para[0].style.display = "none"
// })
​
// para[1].addEventListener("click", function(){
// para[1].style.opacity = "0.2"
// para[1].style.transitionDuration = "2000ms"
// })
​
// let form = document.querySelector("form")
​
// let input = document.querySelectorAll("input")[0]
// let input2 = document.querySelectorAll("input")[1]
​
​
// var x = document.createElement("INPUT");
// x.setAttribute("type", "submit");
// x.setAttribute("class", "formvalue");
// form.appendChild(x);
​
​
​
// x.addEventListener("click", function(){
// 	event.preventDefault();
// 	let value = input.value 
// 	let value2 = input2.value
// 	let div = document.createElement("div")
// 	div.setAttribute("class", "tbl")
// 	document.body.appendChild(div)
// 	div.innerHTML = "<table border = '1'>" + 
// 	"<tr>" + 
// 	"<th>Name</th>" + 
// 	"<th>Answer</th>" +
// 	"</tr>" +
// 	"<tr>" +
// 	"<td>" + value + "</td>" +
// 	"<td>" + value2 + "</td>" +
// 	"</tr>"
// })
​
​
​
// Exercie 2
​
// let para_new = document.querySelector("p")
// let bold;
​
​
​
// function getBold_items() {
// 	 bold = para_new.querySelectorAll("strong")
// }
​
// getBold_items()
​
​
// function highlight() {
// 	for (var i = 0; i < bold.length; i++) {
// 		bold[i].style.color = "blue"
// 	}
// }
​
// function return_normal() {
// 	for (var i = 0; i < bold.length; i++) {
// 		bold[i].style.color = "black"
// 	}
// }
​
// para_new.addEventListener("mouseover", highlight);
​
// para_new.addEventListener("mouseout", return_normal);
​
​
// Exercise 3
​
​
function calculation() {
	event.preventDefault(); // stops submit from refreshing page
	let radius = document.getElementById("radius").value; 
	radius = Math.abs(radius); //making number absolute
	let volume = document.getElementById("volume").value;
	volume = (4/3) * Math.PI * Math.pow(radius, 3);
	volume = volume.toFixed(2) // up to 2 decimal points
	let please = document.getElementById("volume") // selects input of volume
	please.setAttribute("value", volume) // sets the value of attribute
}
​
let submit = document.getElementById("submit")
submit.addEventListener("click", calculation)
​
//exercise bonus 4
​
submit.addEventListener("mouseover", function(){
	submit.style.color = "blue"
})
​
submit.addEventListener("mouseout", function(){
	submit.style.border = "4px dashed green"
})
​
​
​
​
​
