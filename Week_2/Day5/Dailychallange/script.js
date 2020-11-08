// Daily Challenge : 99 Bottles Of Beer
// You know the infamous song “99 Bottles of Beer?”

// You need to generate in JavaScript the lyrics to the song 99 Bottles of Beer as an output.

// Ask the user to input a starting number of bottles of beer, and start the bottles falling.
// But instead of 1 falling each time, the number falling goes up by one each time.

// ==============================

// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall
// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammer right…
// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.

// count= prompt("type a number")
// var word = "bottle"
// while (count > 0) {
    
//     }
// }
// var text = "";
// var i = 0;
// while (i < 10) {
//   text += "<br>The number is " + i;
//   i++;

var word = "bottles";
var count =  99

var drink = 1; 
while (count > 0) {
    console.log(count + " " + "bottles of beer on the wall");
    console.log(count + " " + "bottles of beer,");
    console.log( drink + " Take one down, pass it around,");
    //drink = drink +1 
    count = count - drink;
    if (count > 1) {
        console.log(count + " bottles of beer on the wall.");
    } else if(count == 1) {
        console.log(count + " bottle of beer on the wall."); 
    } else {
        console.log("No more more beer.");
    }
}

//solution 
// let beers = parseInt(prompt("Choose a number of beers"));
// ​
// ​
// for (let i = 1; beers > i; i++) {
// ​
//     console.log(beers + " bottles of beer on the wall\n" + beers + " bottles of beer\nTake " + i + " down, pass it arround\n" + (beers - i) + " bottles of beer on the wall");
// ​
//     beers -= i;
// ​
    
// }
// Collapse



