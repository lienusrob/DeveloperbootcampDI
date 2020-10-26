//let str1 = 'mix', let str2 = 'pod' 
//let newWord should be equal to 'pox mid'
let str1 = “mix”;
let str2 = “pod”;
let newWord = str2.slice(0,2) + str1.slice(2,3) + ” ” + str1.slice(0,2) + str2.slice(2,3);
console.log(newWord);
//let newWord should be equal to "pox mid"