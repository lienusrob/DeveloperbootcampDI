
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
​
    let table = document.body.firstElementChild;
    let allBooks = [{
        Title: "Harry Potter",
        Author: "J.K Rowling",
        img: "https://images-na.ssl-images-amazon.com/images/I/815v2OuIHXL._AC_SL1500_.jpg",
        alreadyRead: false
    },
    {   Title: "Legacy of Ashes",
        Author: "Tim Wiener",
        img: "https://images-na.ssl-images-amazon.com/images/I/81QBEaG64PL.jpg",
        alreadyRead: true}
    ]
​
    let div = document.createElement("div");
    div.setAttribute("id", "tbl");
    div.style.marginTop = "50px";
    document.body.appendChild(div);
​
    document.getElementById("tbl").innerHTML = "<table border = '1'>" +
    "<thead>"+"<tr>" + "<th>Title</th>" + "<th>Author</th>" + "<th>Image</th>" + "<th>Read?</th>" + "</tr>"+ "</thead>"
    + "<tbody>" + "</tbody>";
​
    let tableBody = document.querySelector("tbody");
    let isRead = "";
    let a = "<tbody>";
​
    for(i = 0; i<allBooks.length; i++){
        let read = allBooks[i].alreadyRead;
​
        if(read===true){
            isRead = "Yes";
        }
        else{
            isRead = "No";
        }
​
        a = a + "<tr>";
        a = a + "<td>" + allBooks[i].Title + "</td>";
        a = a + "<td>" + allBooks[i].Author + "</td>";
        a = a + "<td>" + '<img width = 100 src = "'+allBooks[i].img + '">' + "</td>";
        a = a + "<td>" + isRead + "</td>";
        a = a + "</tr>";
        
​
    }
    a = a + "</tbody>"
    tableBody.innerHTML = a;
​
    let tableData = document.querySelectorAll("td");
    
    for(j = 0; j<tableData.length; j++){
​
        if(tableData[j].innerHTML==="Yes"){
            tableData[j].style.color = "red";
        }
    }
