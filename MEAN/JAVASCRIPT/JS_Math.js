console.log("===================");
console.log("===== Math 1 ======");
console.log("===================");

function zero_negativity(array){
    var flag = true;
    for (var i=0;i<array.length; i++){
        if(array[i]<0)
        {
            flag = false;
            break;
        }
    }
    return flag;
}

// var x=[1, 3, 8, -3, 10];
var x=[1, 3, 8, 9, 10];
console.log(zero_negativity(x));


console.log("===================");
console.log("===== Math 2 ======");
console.log("===================");

function is_even(number){
    if(number %2 == 0)
    return true;
    else
    return false;
}
console.log(is_even(20));
console.log(is_even(17));

console.log("===================");
console.log("===== Math 3 ======");
console.log("===================");

function how_many_even(array){
    var evens=0;
    for(var i=0;i<array.length;i++){
        if(is_even(array[i]))
        evens++;
    }
    return evens;
}

var y=[1, 3, 8, 9, 10, 22,42];
console.log(how_many_even(y));

console.log("===================");
console.log("===== Math 4 ======");
console.log("===================");

function create_dummy_array(n, x){
    for(var i=0;i<x; i++)
        n.push(Math.floor(Math.random()*10));
    return n;
}
var array =[];
console.log("Create dummy array: ")
console.log(create_dummy_array(array,10));

console.log("===================");
console.log("===== Math 5 ======");
console.log("===================");

function random_choice(array){
    return array[Math.floor(Math.random()*array.length)];

}

var num=[1, 3, 8, 9, 10, 22,42];
console.log(random_choice(num));



