// Exercise 1 : Your Favorite Colors

// Create an array to hold your top colors.
// For each choice, console.log a string like: “My #1 choice is blue”

// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.
// Hint : create an array of suffix to do the Bonus

// var choices = ['Blue', 'Green', 'Red', 'yellow', "pink"];
// for (var i = 0; i < choices.length; i++) {
//     console.log('My fav color  ' + (i + 1) + ' choice is ' + choices[i]);
// }

// for (let favcolours = ["blue", "Green", "Red", "Navy "]; 
//favcolours.length<=4; favcolours++ ) {   
//     ;  console.log(favcolours[1]+ " is my fav colours");
//       }
// Exercise 2 : Secret Group



// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their firstnames, sorted in alphabetical order.
// Console.log the name of their secret society.

//i am lost how to get rid of the commas and to sort the string. 
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// let sec = names.chatAt(0)
// let sec1 = sec.order()
// console.log(sec2);
// console.log(sec);

// for (name=0 ; name < names.length; name++){
//  console.log(names[name].charAt(0))
//}  



// Exercise 3 : Repeat The Question

// Ask a number to the user, while the number is smaller than 10, ask him for a new number.
// Tip : Which while loop is more relevant for this situation?


// let number = (prompt("type a number"));
// while (number < 10) {
//     prompt("type a number")
//  if (number <=10) {
//         break;

//     }
// }




// // Exercise 4 : List Of People


// for (var i = 0; i < choices.length; i++)
// let people = ["Greg", "Mary", "Devon", "James"]
// Using a loop, iterate through this array and console.log all of the people.
// Write the command to remove “Greg” from the array.
// Write the command to replace “James” by “Jason” in the array.
// Write the command to add your name to the end of the array.
// Using a loop, iterate through this array and after console.log-ing “Mary”, exit from the loop.
// Write the command to make a copy of the array using slice. The copy should NOT include “Mary” or your name.
// Write the command that gives the indexOf where “Mary” is located.Look on google what indexOfis
// Write the command that gives the indexOf where “Foo” is located (this should return -1).
// Write a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

// var friends = ["Greg", "Mary", "Devon", "James"];

// var friend1 = friends.length;
// friends.shift(0)
// for (var i = 0; i < friend1; i++) {
//     console.log(friends[i]);
//  }
// var names = ["Greg", "Mary", "Devon", "James"];
// var arrayName = names.length;
// for (var i = 0; i < arrayName; i++) {
//     console.log(names[i]);}

//    var names1 = names.shift(0)
//     console.log(names1);

//     names.splice(2,3, "jason")
//     console.log(names1);

//     names.push("lienus")
//     console.log(names);

// for (var i = 1; i < arrayName; i++) {
//      console.log(names[i]);}

// var names1 = names.splice(1,2)
// console.log(names1);

// console.log(names.indexOf('Mary')) // output 0 but it should be 1 since 





// Exercise 5 : Attendance
// Suppose you have a guest list of students and the country they are from, stored as key-value pairs in an object. You have to make the attendance.

// let guestList = {
//   Randy: "Germany",
//   Karla: "France",
//   Wendy: "Japan",
//   Norman: "England",
//   Sam: "Argentina"
// }
// Ask the student for his name :
// If the name is in the object, console.log the name of the student and the country he comes from.
// "Hi! I'm [name], and I'm from [country]."
// If the name is not in the object, console.log :"Hi! I'm a guest."

let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
}

let names = prompt("type in your name")

for (let name in guestList) {
    if (names == name) {
        console.log("Hi i am " + names + "and i am from " + guestList[name] + ".");
    } else if (!names == name) {
        console.log("hi i am a guest");}
}

//Hi i am Randyand i am from undefined. how do i change the undefined.

// let arrayguestlist = Object.entries(guestList)
// console.log(arrayguestlist);
// let arrayguestlist1 = arrayguestlist.length; 
// for(let i=0; i<arrayguestlist1; i++);{
//     let items = guestList[i].length; n++
//     console.log(i, items);
//     for( let n=0; n<items; n++){
//         console.log(arrayguestlist[i][n]);
// }
// } did not work 


//what do i need to do 
//prompt name 
//change oject to array 
//go though the array 
//use the indexof method to find name on guestlist 
// console log Name 



// Exercise 5 : Divisible By Three

// An elementary school’s trick to determine whether or not a number was divisible by three is to add all of the integers in the number together and to divide the resulting sum by three. 
// If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.

// Given a series of numbers as a string, determine if the number represented by the string is divisible by three.
// You can expect all test case arguments to be strings representing values greater than 0.
// Example:
// "123"      -> true
// "8409"     -> true
// "100853"   -> false
// "33333333" -> true
// "7"        -> false
// Exercise 6 : Playing With Numbers

// let age = [20,5,12,43,98,55];
// Requirements : don’t use Javascript methods to answer these questions
// 1. Console.log the sum of all the elements of the array.
// 2. Console.log the largest number of the array.