//1. 
// In the div above, change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new li to the ul.
// First, create a new li tag (use the createElement method)
// Then create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstChild and the lastChild properties to retrieve the first and last li elements under the parent ul node. Display the text of each link.(Hint: nodeValue property).

// let div = document.getElementById("navBar")//creating a variable and selecting the navBar
// div.setAttribute("id", "socialNetworkNavigation")//addressing selected selecotr navBar -->> change it to social....


// let ul =document.querySelector("ul"); //addresses the ul 
// let listitem= document.createElement("li");// adds a an empty li dot
// let t = document.createTextNode("log out!");//creats the text that should go on the lisdt 
// listitem.appendChild(t) 
// ul.appendChild(listitem)//add text on the list 




// Exercise 2 : Users


// Change the name “Pete” by “Richard”
// Change each first name of the <ul> by your name
// Add at the end of each <ul>, a <li> that says “Hey students”
// Delete the <li> Sarah
// Bonus
// Add a class “student_list” to both of the <ul>
// Add the class “university” and “attendance” to the first <ul>

// let ul2 = document.querySelector("ul");
// let change = ul.lastChild;
// ul2.lastElementChild.innerHTML ="Lienus";
// let ul3 =document.querySelectorAll("ul")[1]; 
// console.log(ul3);
// ul2.firstElementChild.innerHTML ="Tali"; 
// ul3.firstElementChild.innerHTML ="Lea"; 

// let newitem = document.createElement("li")
// let hey = document.createTextNode("Hey students")
// newitem.appendChild(hey)
// ul2.appendChild(newitem)
// le = newitem2 = document.createElement("li")


// //.3 
// let navbar = document.querySelector(".Header")
// navbar.style.backgroundColor = "yellow"



// Exercise 4 : Users And Style


// For the following exercise use this website for assistance: 
// 1. Add a “light blue” background color and some padding to the div above.
// 2. Do not display the first name (John) in the list and add a border to the second name (Pete).
// 3. Change the font size of the whole body.
// 4. Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div)

// let div = document.querySelector("div");
// div.style.backgroundColor = "lightblue";
// div.style.padding = "3em";

// let ul = document.querySelector("ul");
// let John = ul.firstElementChild
// ul.remove.firstElementChild
// ul.removeChild(John)
// let pete = ul.firstElementChild
// pete.style.border = "dashed light blue 4px"
// let body = document.querySelector("body")
// body.style.fontSize ="60px"
// Exercise 2
// let ul2 = document.querySelector("ul");
// console.log(ul2);
// ul2.lastElementChild.innerHTML = "Richard";
// let ul3 = document.querySelectorAll("ul")[1];
// console.log(ul3);
// ul2.firstElementChild.innerHTML = "Tali";
// ul3.firstElementChild.innerHTML = "Lea";
// let newitem = document.createElement("li");
// let hey = document.createTextNode("Hey students");
// newitem.appendChild(hey);
// ul2.appendChild(newitem);
// let newitem2 = document.createElement("li");
// let heyo = document.createTextNode("Hey students");
// newitem2.appendChild(heyo);
// ul3.appendChild(newitem2);
// let sarah = ul3.children[1]
// // ul3.removeChild(sarah);
// sarah.remove();
// ul2.classList.add("student_list");
// ul3.classList.add("student_list");
// ul2.classList.add("university");
// ul2.classList.add("attendance");
//Exercise 3
// let navbar = document.querySelector(".Header")
// navbar.style.backgroundColor = "yellow"
// let name2 = document.querySelector(".user-profile-link")
// name2.innerText = "The Boss!"​
// Exercise 4
// let div = document.querySelector("div")  // locating the element
// div.style.backgroundColor = "lightblue"
// div.style.padding = "2em"
// let ul = document.querySelector("ul")  //parent element
// let john = ul.firstElementChild // first child out of 2
// // ul.removeChild(john)
// let pete = ul.firstElementChild
// pete.style.border = "dashed lightblue 4px"
// let body = document.querySelector("body")
// body.style.fontSize = "60px"​
// let pete2 = ul.lastElementChild
// let x = john.innerHTML
// let y = pete2.innerText
// if (div.style.backgroundColor = "lightblue") {
// 	alert("Helloooooo " + x + " and " + y)
// }
