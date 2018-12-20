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
  let a = Math.floor(Math.random()*30);
  let b = Math.floor(Math.random()*30);
  let result = gcd(a,b);
  console.log(result);
  document.getElementById("gcd");
  var gcdResult = document.getElementById("gcdRes");
  gcdResult.innerHTML = "GCD of " + a + " & " + b + " is " + result;
};
gcdClick.addEventListener('click', getGCD);


//fib
var fibClick = document.getElementById("fib");
var getFib = function(){
  let a = Math.floor(Math.random()*30);
  let result = fibonacci(a);
  console.log(result);
  document.getElementById("fib");
  var fibResult = document.getElementById("fibRes");
  fibResult.innerHTML = "Fibonacci number " + a + " is " + result;
};
fibClick.addEventListener('click', getFib);


//random student
var randClick = document.getElementById("randStu");
var getRand = function(){
  let result = randomStudent()
  console.log(result);
  document.getElementById("randStu");
  var randResult = document.getElementById("randRes");
  randResult.innerHTML = "Random Student:" + result;
};
randClick.addEventListener('click', getRand);
