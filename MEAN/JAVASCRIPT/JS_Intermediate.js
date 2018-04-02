console.log("===================");
console.log("===== Part 1 ======");
console.log("===================");

function starString(num){
    var starstr="";
    for(var i=0; i<num;i++){
        starstr += "*";
    }
    return starstr;

}

let stars = starString(8);
console.log(stars);

console.log("===================");
console.log("===== Part 2 ======");
console.log("===================");

function drawStars(x){
    var str='';
    for(var i=0;i<x.length;i++){
        for(var j=0;j<x[i];j++){
            str +="*";
        }
        console.log(str);
        str = '';
    }

}
let n1 = [4, 6, 1, 3, 5, 7, 25];
drawStars(n1);

console.log("===================");
console.log("===== Part 3 ======");
console.log("===================");


function draw_Stars(x){
    var str='';
    var z;
    for(var i=0;i<x.length;i++){
        z=x[i];
        if(typeof (z) == "number")
        {
            for(var j=0;j<x[i];j++){
                str +="*";
            }
        }
        // console.log(typeof (x[i]));
        else if (typeof (x[i]) == "strnig")
        {
            var letter= z.slice(0,1);
            // console.log(letter);
            for(var j=0; j<x[i].length;j++)
            {
                str += letter.toLowerCase();
            }
        }
        console.log(str);
        str = '';
    }

}

let str = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"];
draw_Stars(str);