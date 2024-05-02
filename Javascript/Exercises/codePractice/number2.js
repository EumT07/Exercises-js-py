"use strict"

/**
 * Number 1
 * 
 * Write a javascript program to create a new string from a given string taking the first 3 characters and the last 3 characaters of the string and adding them together. The string length must be 3 or more, if not, the origianl string is returned.
 * 
 */



const result = (str)=>{
    // #1
    return str.length < 3 ? str : str.slice(0,3) + str.slice(-3);

    // #2
    // let newString = null;

    // if(str.length >= 3){
    //     //Taking the 3 frist letters
    //     // let fisrt3_characters = str.slice(0,3);
    //     // let last3_characters = str.slice(str.length - 3);

    //     // newString = fisrt3_characters + last3_characters;

    
    //     return newString;
    // }else{
    //     return str;
    // }
}

// console.log(result("abc"));
// console.log(result("abcdefgtfd"));
// console.log(result("ab"));

/*
Exercise 2:

Write a Javascript program to extract the first half of a string of even length.
 */
const firstHalf = (str)=>{
    return str.slice(0, str.length / 2);
}

// console.log(firstHalf("tornado"));
// console.log(firstHalf("pan"));
// console.log(firstHalf("cerveza"));


/**
 * Exercise 3
 * 
 * Write a javascript program to concatenate two stringd except theris first character.
 */

const concatenate = (str1,str2) => {
    return str1.slice(1) + str2.slice(1);
}

// console.log(concatenate("abc","def"));
// console.log(concatenate("Miguel","Carrero"));


/**
 * Exercise 4:
 * 
 * Given two values, write a Javascript program to find out which one is nerest to 100
 */


const closesTo100 = (a,b)=>{

    return (100 -a) < (100 - b) ? a : b;

    // if((100 - a) < (100 -b)){
    //     return a;
    // }else{
    //     return b;
    // }
}

// console.log(closesTo100(99,1));
// console.log(closesTo100(80,20));
// console.log(closesTo100(45,55));
// console.log(closesTo100(4,96));


/**
 * Excercise 5
 * 
 * Write a JS code, to check a given string contains 2 to 4 occurences of a specified character
 */


const countChars = (str, char) => {
    let arryString = str.split("");
    let gettingChar = arryString.filter(ch => ch === char)
    return gettingChar.length;
}

const check_if_contains2T04 = (str, cha) => {
    return countChars(str,cha) >= 2 && countChars(str,cha) <= 4; 
} 

console.log(check_if_contains2T04("ooh","o"));
// console.log(check_if_contains2T04("ooooh","o"));
// console.log(check_if_contains2T04("oh","o"));
// console.log(check_if_contains2T04("oooh","o"));
