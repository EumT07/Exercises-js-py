"use strict"
//Object POO: Object Oriented  Programming Oriented 

// #1 {}
let person = {
    name: "Lucas",
    lastName: "Smith",
    age: "28"
}

console.log(`
Person:
Name: ${person.name}
Last Name: ${person.lastName}
Age: ${person.age}
`);

// #2 new Object

let animal = new Object();

//Properties
animal.type = "Zebra";
animal.colors = "Black and white"

console.log("Animal: ",animal.type);
console.log("Animal Color: ",animal["colors"]);

//Methods: Functions and this methods

//Functions
//#1: creating a function 
let student = {
    name: "Lucas",
    lastName: "Smith",
    birthday: 2000,
    age: 0,
    //methods:
    clAge: function(year){
        return year - this.birthday;
    },
    //this methods:
    changeAge: function(year){
        let gettingAge = year - this.birthday;
        this.age = this.age += gettingAge;
    }
}
student.changeAge(2023)
console.log("Stundent: ",student.name);
console.log("Stundent Age: ",student.clAge(2023));
console.log("Stundent Age: ",student.age);

//#2: function Shorthand 
let car = {
    model: "Mustang",
    color: "Black",
    resume() {
        return `This car is ${this.model} an its color is ${this.color}`
    }
    
}

console.log(car.resume());

//This 
let obj = {
    name: "A",
    log: function (){
      this.name = "A 2";
      console.log(this);// A 2
  
    //   let that = this
      var change = function (str){
        this.name = str;
        // that.nombre = str;
      }
  
      change("B34");
      console.log(this)
      //
    }
  }
  
  console.log(obj)
  console.log(obj.log())


//Array with objects

let phone = [
    {model:"Iphone",color:"blue"},
    {model:"Nokia",color:"black"},
    {model:"Motorolla",color:"green"}
]

console.log(phone);

//delete any properties
delete obj.name 


//Destructuring 


//Object.values --> get an array

let person_values = Object.values(person);
let person_keys = Object.keys(person);
console.log("Arrays Keys: ",person_keys);
console.log("Arrays Values: ",person_values);







