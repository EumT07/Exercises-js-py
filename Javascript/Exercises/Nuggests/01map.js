"use strict"
//Using map : take an array, transform its elements, and include the results in a new array.
const people = [
    {
        name: "Alicia",
        age: 25,
        position: "Admin" 
    },
    {
        name: "Miguel",
        age: 21,
        position: "Web Developer" 
    },
    {
        name: "Carlos",
        age: 22,
        position: "Data Sciencs" 
    },
    {
        name: "Pedro",
        age: 25,
        position: "UI/UX" 
    },
    {
        name: "José",
        age: 30,
        position: "Backend Developer" 
    },
    {
        name: "Luis",
        age: 22,
        position: "QA Engineer" 
    },
    {
        name: "Andrea",
        age: 28,
        position: "Fullstack Developer" 
    }
]
//It Does not change the zise of original array ( unlike filter )
// Uses values from original array when making new one

// #1 ES6
const ages = people.map(person => {
    return person.age;
});

const position = people.map(person => person.position);

// #2 Function
function getNames(person){
    return person.name.toLowerCase();
}

const names = people.map(getNames);

// #3 arrow Function
const getName_and_Ages = (person) => {
    return {
        name: person.name.toUpperCase(),
        age: person.age
    }
}

const gettingObj = people.map(getName_and_Ages);


console.log("GEtting ages from peopleArry: ", ages);
console.log("GEtting position from peopleArry: ", position);
console.log("GEtting names from peopleArry: ", names);
console.log("GEtting gettingObj from peopleArry: ", gettingObj);