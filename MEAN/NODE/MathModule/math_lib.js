module.exports = function (){
    return {
      add: function(num1, num2) { 
        console.log(num1,"+",num2,"=", num1+num2);
      },
      multiply: function(num1, num2) {
        console.log(num1,"*",num2,"=", num1*num2 );
      },
      square: function(num) {
           console.log("the square of",num,"=",num*num);
      },
      random: function(num1, num2) {
           console.log("A random number between",num1,"and",num2,"is:",Math.floor(Math.random(num1, num2+1)));
      }
    }
  };