"use strict"

// Creating a String
console.log("< < < String > > >");
let country = "Venezuela"; //String
let city = new String("El Tigre");
console.log(country);
console.log(city);

// length

let name = "Eublan"
console.log("Lenght: " + name.length);

// Transforming text
/**
 * toLowercase()
 * toUpperCase()
 * toString()
 * concat()
 */
console.log("< < < Transforming String > > >");

let text = "I'm A professional";
//toUpperCase()
console.log("UpperCase: ", text.toUpperCase());
//toLowercase()
console.log("LowerCase: ",text.toLowerCase());
//toString()
let num = 123;
console.log("From Number to string: ", num.toString());
console.log("Type: ",typeof num);

//Normal
let house = "My house";
let verb = "is";
let adjetive = "beautiful";

const house_adjetive = house.toUpperCase() + " " + verb + " " + adjetive.toLowerCase();
console.log("Join string: ", house_adjetive);


// Example with concat: join string, variables and arrays
let text1  = "Hello";
let text2  = "and Welcome";
let text3 = "This will be the best day of your life";

const result_of_text = text1.concat(" ", text2, " ",text3);
console.log("Concatenated text: ", result_of_text);

//With backtick ` ` 
// insert variable ${}

//one line
let subject = "Eublan";
let connectors = "and"
let subject2 = "Luisa";
let complement = "Looking for a new house"

const result = `${subject} ${connectors} ${subject2} are ${complement}
`;

console.log("Sentence: ", result);



