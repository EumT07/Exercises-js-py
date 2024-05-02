"use strict"

/**
 * Exercise 1:
 * 
 * Write a javascript program to check two number and return true if one of the number is 100 or if the sum of the two number is 100.
 */

const num1 = 34;
const num2 = 100;

// const value = (num1, num2) => {
//     let result = num1 + num2;
//     if(num1 == 100 && num2 == 100){
//         return `Num1:${num1} and Num2:${num2} are equal to 100`;
//     }else if(num1 == 100){
//         return `Num1:${num1} is equal to 100`;
//     }else if(num2 == 100){
//         return `Num2:${num2} is equal to 100`;
//     }else if(result == 100){
//         return `Num1 + Num2 are equal to 100`
//     }else{
//         return `Both number are not equal to 100 and even if you add them you won't get 100`;
//     }
// }

// console.log(value(50,50));
// console.log(value(100,100));
// console.log(value(40,60));
// console.log(value(30,30));
// console.log(value(100,50));
// console.log(value(50,100));

/** Other result */

const isEqualTo100 = (a,b) => a === 100 || b === 100 || (a+b) === 100;

// console.log(isEqualTo100(20,80));//True
// console.log(isEqualTo100(60,40));//True


/**
 * Exercise 2:
 * ----------
 * Write a Javascript program to get the extension of a filename.
 */

let filename1 = "index.js";
let filename2 = "index.css";

const getExtension = (file) => {
    //Getting position
    let position = file.indexOf(".");
    //Getting all extension .js, .css, .py
    let extension1 = file.slice(position, file.length);
    //getting without .
    // let extension2 = file.slice(position + 1, file.length);

    console.log(extension1);
    // console.log(extension2);
}

// getExtension(filename1);
// getExtension(filename2);


// Another way to do it

let filename4 = "app.routes.js"
let filename5 = "app.css"

const getExtension2 = (file) => {
    //lastIndexOf

    let result = file.slice(file.lastIndexOf("."));
    console.log(result);
}

// getExtension2(filename4);
// getExtension2(filename5);


/**
 * Exercise 3:
 * ----------
 * 
 * Write a JavaScript program to replace every character in a given string with the character following it in the alphabet
 */

// String.fromCharCode
// charCodeAt

const moveCharacter = (str) => {
    // let result = str.split("").map(char => String.fromCharCode(char.charCodeAt(0) + 1)).join("");

    return result;
}


// console.log(moveCharacter("abcd"));

/**
 * Exercise 4:
 * 
 * Write a JavaScript program to get the current date.
 * Formats:
 *          mm-dd-yyyy,
 *          mm/dd/yyyy,
 *          dd--mm-yyyy,
 *          dd/mm/yyyy
 */


const dateFormat = () => {
    let date = new Date();
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();


    return `${day}-${month}-${year}`;
}

// console.log(dateFormat());

/**
 * Exercise 5:
 * Write a Javascript program to create a new string adding "New!" in front of a given string. If the given string begins with "New!" already then return the original string.
 */

const addNew = (str) => {
    let result = str.indexOf("New!") === 0 ? str : `New! ${str}`

    console.log(result);
}

addNew("New! Look")
addNew("Look")