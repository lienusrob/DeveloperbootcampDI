// Exercise 1 : Select A Kind Of Music

// <select id="genres">
//   <option value="rock">Rock</option>
//   <option value="blues" selected>Blues</option>
// </select>
// Show the value and the text of the selected option.
// Add an option: <option value="classic">Classic</option>.
// Make it selected.
let choice = document.querySelectorAll("select")
let selectedop = choice.options[choice.selectedIndex].value; 
console.log(selectedop);
