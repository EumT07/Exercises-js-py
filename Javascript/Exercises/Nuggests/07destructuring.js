"use strict"

//faster/easier way to access/unpack variables from arrays

const fruits = ["orange", "banana","lemon"];

const orange = fruits[0];
const banana = fruits[1];
const lemon = fruits[2];

// console.log(orange,banana,lemon);

//Destructing method

const cars = ["corola","mazda","ford","chevrolet"];
const [corola,mazda,ford,chevrolet] = cars;
const [A,B,C,D] = cars;
const [E,,F,] = cars;

// console.log(corola,mazda,ford,chevrolet);
// console.log(A,B,C,D);
// console.log(E,F);

//video 8 Destructuring objects

const user = {
    name: "robert",
    lastname: "Smith",
    email: "robertsmith@gmail.com",
    siblings: {
        sister: "jane",
        brother: "max"
    },
};

// const {name,lastname,email,siblings} = user;
const {name:robert,lastname,email,siblings:{sister}} = user;

// console.log(email,robert,lastname,sister);


//Destructurin with a function

// function getDataFromUser(data) {
    
//     const {name,lastname,email} = data;
    
//     console.log(name,lastname,email);
// }

// getDataFromUser(user);

function getDataFromUser({name,lastname,email,siblings:{brother}}) {

    console.log(name,lastname,email,brother);
}

getDataFromUser(user);