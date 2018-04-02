function rvsWords(str, i=str.length){
// var nstr;
if (i < 0 ){
    return "";
}

while(str[i] != " "){
    nstr= str[i];
    i++;
}
i++;
return  rvsWords(str,i)+ nstr;






}                        

console.log("cat dog person")