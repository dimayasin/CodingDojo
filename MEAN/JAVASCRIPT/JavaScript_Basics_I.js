console.log("==================");
console.log("=====Basic 1======");
console.log("==================");
var x =[]
x.push('Coding');
console.log(x);
x.push('dojo');
console.log(x);
x.push('rocks');
console.log(x);
x.pop();
console.log(x);
x.pop();
console.log(x);
x.pop();
console.log(x);
console.log();


console.log("==================");
console.log("=====Basic 2======");
console.log("==================");

const y=[];
y.push(88);
console.log(y);
console.log();

console.log("==================");
console.log("=====Basic 3======");
console.log("==================");

var z=[9,10,6,5,-1,20,13,2];
console.log(z);
for (var i=0; i<z.length-1;i++)
console.log(z[i]);

console.log();
console.log("==================");
console.log("=====Basic 4======");
console.log("==================");

var names=['Kadie', 'Joe', 'Fritz', 'Pierre', 'Alphonso'];

for (var i=0; i<names.length;i++)
console.log(names[i].length);

console.log();
console.log("==================");
console.log("=====Basic 5======");
console.log("==================");

function yell(string){
    return string.toUpperCase();
}
console.log('Converting "hello there" to all upper case: '+yell('hello there'));

