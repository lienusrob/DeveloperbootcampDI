let calcDisplay = document.getElementById("display")
console.log(calcDisplay.innerHTML)

let calcstr = ""
function my_f(btn){
    calcstr = calcstr + btn;
    calcDisplay.innerHTML=calcstr;
    console.log(calcDisplay);
}
function result(){
    let calcreslut = eval(calcstr);
    calcDisplay.innerHTML = calcreslut;
    console.log(calcreslut);
}

function reset(){
    calcstr ="0"
    calcDisplay.innerHTML = 0;
 
    // calcstr - calcreslut; 
    // calcDisplay.innerHTML = calclear;
}

// function hello (){
//   if    (calcDisplay.innerHTML> 1 {
//         calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0,-1)
//   } else { calcDisplay.innerHTML  = 0; 
// } 

// }}