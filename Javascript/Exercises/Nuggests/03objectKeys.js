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


//For in Loop
const laptop = {
    brand: "Samsung",
    processor: "i7",
    ram: 16
}

for (const propertyName in laptop){
    console.log(`${propertyName} : ${laptop[propertyName]}`);
}


//Objects.keys()
console.log("Keys");
const laptoKeys = Object.keys(laptop)
console.log(laptoKeys);

//Objects.values()
console.log("Values");
const laptoValues = Object.values(laptop)
console.log(laptoValues);

//Objects.entries()
console.log("Entries");
const laptopEntries = Object.entries(laptop)
console.log(laptopEntries);

//MAp method
const newResult = laptopEntries.map(item =>{
    // console.log("Show item");
    // console.log(item)
    const [kyes, values] = item
    console.log("keys: ", kyes);
    console.log("vavalues: ",values);
})

