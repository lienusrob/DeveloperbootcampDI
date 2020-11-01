
//excersise 1 

// function checkDriverAge(age) {
//     let age= prompt("")
	
// 	if (Number(age1) < 18) {
// 		alert( 'Sorry, you are too young to drive the car. Powering off')
// 	} else if (Number(age1) > 18) {
//         alert('Powering On. Enjoy the ride!');
// 	} else if (Number(age1) === 18) {
//         alert('Congratulations on your first year of driving. Enjoy the ride!');
// 	}
// }
//


// //Exercise 2 

// // Write a program to check whether a string is blank or not.

// function is_Blank(mylist){ //creating a functiton and the parameters mylist 
//     if (mylist.length == 0) {  //checking if mylist has 0 character 
//         return true             //since we cant use console log in this case we are using. due to local and global etc. console log would giive us a syntax error 
//     } else {
//         return false  // //since we cant use console log in this case we are using. due to local and global etc. console log would giive us a syntax error 
//     }
    
// }

// function pushingToArray(newlist){ // function inside a function starting once the is_blank function has a true or false statment. 
//     if (is_Blank(newlist) == true) {// if statment is true "a " will be addred to the array. 
//         newlist.push("a")
//     } else {                        //if statment is not true console log will display newlist which is empty but it will also push pink and yellow in the array thereforre 2 values are in the array after the 2 functions . 
//         console.log(newlist)
//     }
// }
// pushingToArray(["pink", "yellow"])

//Exercise

// Write a JavaScript function to convert a string in abbreviated form.

// console.log(abbrev_name("Robin Singh")); --> "Robin S."

// abbrev_name = function (str) {
//     var names = str.trim().split(" ");
//     if (names.length > 1) {
//         return (names[0] + " " + names[1].charAt(0) + ".");
//     }
//     return names[0];
// };
// console.log(abbrev_name("Robin Singh"));

// Exercise 4 : SwapCase

// Write a JavaScript function which accept a string as input and swap the case of each character. 
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.

// let statment = ("The Fox is Browon")


// let statment = ("The Fox is Brown")
// var Letterswap = function (letters )

// {
//     var newLetters = "";
//     for(var i = 0; i<letters.length; i++){
//         if(letters[i] === letters[i].toLowerCase()){
//             newLetters += letters[i].toUpperCase();
//         }else {
//             newLetters += letters[i].toLowerCase();
//         }
//     }
//     console.log(newLetters);
//     return newLetters;
// }

// var text = 'The Fox is Brown';

// var swappedText = Letterswap(text); // "sO, TODAY WE HAVE really GOOD DAY"


// Exercise 5 : Amazon Shopping
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }
// Create a function called checkBasket().
// It should:
// ask the user for the item he wants
// and let him know if it’s in the basket or not
// Hint: Use the in keyword inside the conditional


// let amazonBasket = {
//         glasses: 1,
//          books: 2,
//         floss: 100
// }

// function checkbasket(){
//     let add = prompt("what do you wish to buy")
//     for (let item in amazonBasket) {
//         if (add == item) {
//             console.log(" sorry" + add + " is allready in the basket " + amazonBasket[item]  );
//         } else if (!add == item) {
//             console.log("added to the baseket");}
//     }
// }
// checkbasket.call()

// Exercise 6 : What’s In My Wallet ?
// Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.5
// Pennies = 0.1
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// Examples

// changeEnough([2, 100, 0, 0], 14.11) ➞ false
// changeEnough([0, 0, 20, 5], 0.75) ➞ true

// Exercise 7 : Shopping List
let shoppingList =["banana", "orange", "apple"]
 let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
function myBill(){
    
}
// Create an array called shoppingList with the values “banana”, “orange”, and “apple”.
// Copy these two above objects into your js file
// Create a function called myBill() that takes no argument.
// Depending on the list of items that you have in your array shoppingList and the prices listed in the prices object,
// return the price spent on shopping.
// Call the function myBill()
// Bonus: In the function above, only add the price if the item is in stock (use the stock object).
// If the item is in stock, decrease the item’s stock by 1
