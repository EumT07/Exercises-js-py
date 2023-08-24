"use strict"

//dot notation
const person = {
    name: "Eublan"
}
person.age = 30
console.log(person.age);

//Square bracket notation

const items = {
    "featured-items": ["Items 1","Items 2","Items 3"],
}
console.log(items["featured-items"]);

let appStatus = "Loading";
// appStatus = "error"
const keyName = "Computer"
const app = {
    [appStatus]: "Wait few minutes"
}
//Addin a new properties
app[keyName] = "PC gamming"

// console.log(app);

//Creating a function

let state = {
    loading: true,
    name:null,
    age:null
};

function newProperty(key,value){
    return state[key] = value;
}

newProperty("Taza","Coffee and Milk");
newProperty("name","Will Smith");
newProperty("age","54");
newProperty("loading",false);

//Adding variables
let car = "car";
let model = "Mustang"
newProperty(car,model)

console.log("Object",state);