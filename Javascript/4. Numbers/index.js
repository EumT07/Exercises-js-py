"use strict"

// Properties

console.log("MAX_VALUE: ", Number.MAX_VALUE);
console.log("MIN_VALUE: ", Number.MIN_VALUE);
console.log("NEGATIVE_INFINITY: ", Number.NEGATIVE_INFINITY);
console.log("NEGATIVE_INFINITY: ", Number.POSITIVE_INFINITY);

console.log("NaN: ", Number.NaN);

// Numbers Method

let num = "30.5";

console.log('Type of Data: ', typeof num);
console.log('Number: ', typeof Number(num));
console.log('parseInt: ',  parseInt(num));//N Inter
console.log('parseFloat: ', Number.parseFloat(num));// Float
console.log('isNaN: ', isNaN(num));// ? si es un numero
console.log('isInteger: ', Number.isInteger(num));

// 

let num2 = 3.7453;

console.log("toExponential: ", num2.toExponential(4));
console.log("toFixed: ", num2.toFixed(3));
console.log("toPrecision: ", num2.toPrecision(2));
console.log("toString: ", typeof num2.toString());


// Math module
console.log("\n Math Module\n");
let num3 = 4.57

console.log(" Math round: ",  Math.round(num3))// --> 5
console.log(" Math round: ",  Math.floor(num3))// --> 4
console.log(" Math round: ",  Math.ceil(num3))// --> 5

console.log("Exp: ", Math.pow(2,2));
console.log("Exp: ", Math.pow(3,4));
console.log("Exp: ", Math.pow(4,3));


//Date
let date = new Date();
//Propiedades
let month = date.getMonth();
let day = date.getDay();
let hour = date.getHours();
let minute = date.getUTCMinutes();
let second = date.getSeconds();

console.log(date);