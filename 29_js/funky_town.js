/*
 Team Awoooo - Jeffrey Wu and Britni Canale
 SoftDev1 pd6
 K28 - Sequential Progression
 2018-12-19
*/


//functions
var fibonacci = function(n) {
    if(n <2){
      return n;
    }
    else{
      return fibonacci(n-1) + fibonacci(n-2);
    }
};

var gcd = function(a,b){
    if (a == b){
        return a;
    }
    else if (a > b){
      return gcd(b,a-b);
    }
    else{
      return gcd(a,b-a);
    }
};

var students = ['Jeffrey','Britni','Thomas', 'Tim','Damian'];
var randomStudent = function(){
    return students[Math.floor(Math.random()*students.length)]
}



//RETRIEVERS

//gcd
var gcdClick = document.getElementById("gcd");
var getGCD = function(){
  console.log(gcd(Math.floor(Math.random()*30), Math.floor(Math.random()*30)));
  document.getElementById("gcd");
};
gcdClick.addEventListener('click', getGCD);

//fib
var fibClick = document.getElementById("fib");
var getFib = function(){
  console.log(fibonacci(Math.floor(Math.random()*15)));
  document.getElementById("fib");
};
fibClick.addEventListener('click', getFib);

//random student
var randClick = document.getElementById("randStu");
var getRand = function(){
  console.log(randomStudent());
  document.getElementById("randStu");
};
randClick.addEventListener('click', getRand);
