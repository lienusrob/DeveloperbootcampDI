// //"I am finding Nemo !" ➞ "I found Nemo at 4!"
// //You’re given a string of words. You need to find the word “Nemo”, and return a string like this: “I found Nemo at [the order of the word you find nemo]!”.
// //Bonus : If you can’t find Nemo, console.log “I can’t find Nemo :(“. 
// //Hint : use an if/else statement

// var sentence= "i am finding Nemo!"
// sentence= sentence.toLowerCase()
// var position= sentence.search(nemo)
// var nemo= sentence.split(" ")
// var position= nemo.indexOf("nemo")

// console.log("i found Nemo at " + position)

var string = "i am not a fish  !";
var split = string.split(" ");
var n = split.indexOf("Nemo");
    if(n>0){
        console.log("I found Nemo at" + " " + n + "!");
    }
    else{
        console.log("Nemo is not here")
    }
