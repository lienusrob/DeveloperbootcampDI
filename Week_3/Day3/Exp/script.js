

var ani = document.getElementById("animate"); 
var left = ani.offsetLeft
var speed = (2); //how fast he box should move 
var left= ani.offsetLeft;
console.log(left);
console.log(ani);



movingbox = function(){ 
   
        if ( (move > 0 && left > 350) || (move < 0 && left < 51) ) {
         clearTimeout(timer);
                timer = setInterval(function() {
                    movingbox(move * -1);  
                }, speed); 
              }
              ani.style.left = left + move + 'px';
            }; 
            var timer = setInterval(
            function() { 
                movingbox(1); 
            }
            , speed);