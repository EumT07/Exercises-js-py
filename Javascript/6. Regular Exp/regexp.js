"use strict"

// exp 1
let regexp1 = new RegExp("abc");
console.log(regexp1);

// exp 2
let regexp2 = /abc/;
console.log(regexp2);

// test : it allow if the exp is True or False

console.log("Regular expression 'abc': ",regexp1.test("abc"));
console.log("Regular expression 'abc': ",regexp2.test("dFe"));

// Checking is there are number into de exp

let exp_numbers = /[12345]/;//One by one
let exp_number_rango = /[1-9]/;
let exp_letter_rangoLwr = /[a-z]/;//Lowercase
let exp_letter_rangoUpr = /[A-Z]/;//Uppercase
let exp_combined_rango = /[1-9a-zA-Z]/;//Uppercase

console.log(exp_numbers.test("There is 4 houeses"));// There is a Number 4
console.log(exp_letter_rangoLwr.test("HELLO WORLD"));// There is not lowercase letter
console.log(exp_letter_rangoUpr.test("Hello World"));// There are two Upper Letter

// Characters

let characters = /\d\d-\d\d-\d\d\d\d/;
console.log(caract.test('29-junio-2007')); //29 06 2007
// number -> d 
// dd-dd-dddd -> 