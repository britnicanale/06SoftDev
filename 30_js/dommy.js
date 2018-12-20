var fibonacci = function(n) {
    if(n <2){
      return n;
    }
    else{
      return fibonacci(n-1) + fibonacci(n-2);
    }
};

var heading = document.getElementById("h");
var list = document.getElementById("thelist");
list.addEventListener('mouseover', function(e){
  console.log(e);
  heading.innerHTML = e['target'].innerHTML;
});
list.addEventListener('mouseout', function(e){
  console.log(e);
  heading.innerHTML = "Hello World";
});
