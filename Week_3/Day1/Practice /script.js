// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?

// 2. The ul DOM node?

// 3. The second li (with Pete)?
// Accessing nodes with methods

// element.getElementById()
// element.getElementsByClassName()
// element.getElementsByTagName()
// element.querySelector()
// document
// var div=document.getElementsByTagName("div");
// console.log(div[0]);
// var div1=document.querySelector("div")
// console.log(div1);

// var ul=document.getElementsByTagName("ul");
// console.log(ul[0]);
// var ul1=document.querySelector("ul")
// console.log(ul1);
// var body = document.querySelector("body")

// var ul = document.children[1]
// console.log(ul);

// var li=document.getElementsByTagName("li");
// console.log(li);

// var li1=document.getElementsByTagName("li");
// console.log(li1[1]);

// In the div above, change the value of the identity attribute (id) from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new li to the ul.
// First, create a new li tag (use the createElement method)
// Then create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstChild and the lastChild properties to retrieve the first and last li elements under the parent ul node. Display the text of each link.(Hint: nodeValue property).

let div = document.getElementById("navBar")
div.setAttribute("id", "socialNetworkNavigation")
