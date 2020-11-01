// Daily Challenge : Not Bad

// Create a string that has the word “not” and “bad” inside
// Create another variable that should find the first appearance of the substring “not” and “bad”.
// If the ‘bad’ follows the “not”, then it should replace the whole “not”…”bad” substring with ‘good’ than console.log the result.
// If it doesn’t find “not” and “bad” in the right sequence (or at all), just console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad!', the result is : 'This dinner is good!'
//   Your string is : 'This movie is not so bad!' the result is : 'This movie is good!'
//   Your string is : 'This dinner is bad!' the result is : 'This dinner is bad!'

// var str = "Bad Not";
// var not = str.indexOf("Not");
// var bad = str.indexOf("Bad");
// var n = str.search("Good");

// var string = 'not bad'; 
// var newstring = string.replace(/not bad/, 'good'); 
// console.log(newstring);
  


var str = "its not that Bad Not to code";
var not = str.indexOf("Not");
var bad = str.indexOf("Bad");
var n = str.search("Bad Not");

var newstring = str.replace("Bad Not", 'good'); 
console.log(newstring);



