
// Exercise 1 : My Book List

// Look at this link to help you : here
// The point of this challenge is to display a list of two books on the page. 
// You only have to write code in a js file. It has to be dynamic.
// The body of your html page has to be empty.

// Create an array called allBooks. This array contain objects. Each object is a book that has 4 keys : title, author,image(a url) and alreadyRead which is a boolean.
// Initiate the array with 2 books of your choice.
// Requirements: 
// On the page you have to render the books inside a table.
// For each book :
// You have to display the book’s title then “written by” and then the book’s author (Ex: HarryPotter written by JKRolling)
// The width of the image has to be set to 100.
// If the book is already read. Set the color of the book details to red

var allBooks = [
    {
    title: "Mistborn",
    author: "Bradon Sanderson",
    image: "https://www.graphicaudiointernational.net/media/catalog/product/cache/497477d0e0dc180e58442c8ff7cc7a66/v/i/vin_graphic-audio_alexallen_finished_2.jpg"
},{
    title: "IT",
    author: "Steephen King",
    image:"https://www.graphicaudiointernational.net/media/catalog/product/cache/497477d0e0dc180e58442c8ff7cc7a66/v/i/vin_graphic-audio_alexallen_finished_2.jpg"
}
   ]