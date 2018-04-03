function Ninja(name){
    this.name= name;
    this.health=100;
    const speed=3;
    const strength =3;

    this.sayName=function()
    {
        console.log("My ninja name is "+name);
    }

    this.showStatus=function()
    {
        // console.log("Name: ",name, ", Health: ", health, ", Speed: ",speed,", Strength: ",strength);
        console.log("Name: "+this.name+ ", Health: "+this.health+ ", Speed: "+speed+", Strength: "+strength);
        // return "Name: "+name+ ", Health: "+health+ ", Speed: "+speed+", Strength: "+strength;
    }
   this.UpdateHealth=function(){
        this.health +=10;
    }
    this.drinkSake=function(){
        this.UpdateHealth();
        this.showStatus();

    }

}

const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// console.log(ninja1.showStats());
// console.log(ninja1.drinkSake());
ninja1.showStatus();
ninja1.drinkSake();
