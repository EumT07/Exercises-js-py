"use strict"

class Person {
    constructor(name,lastname){
        this.name = name;
        this.lastname = lastname;
    };
};
let last_name = "cage"
// const person1 = new Person("Luke","Cage");
const person1 = new Person("Luke", last_name);

console.log(person1);

//Method

class Car {
    constructor(model,year,tires,colors = []){
        this.model = model;
        this.year = year;
        this.tires = tires;
        this.colors = colors;
    }

    getCarInfo(){
        let model = ` ${this.model} One of the best model what we have for the moment, this car was made this year ${this.year} it has ${this.tires} and you cand have one of this in our diferents colors:  `
        this.colors.forEach((color)=>{
            model += `${color}`
        });
        return model;
    }
}

let mustang = new Car("mustang", 1968, 4, ["black","white","red","blue"]);
let ferrari = new Car("Ferrari",2020,4,["red","black","yellow"])
console.log(mustang);
console.log(ferrari);


