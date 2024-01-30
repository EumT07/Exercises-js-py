"use strict"

/**
 * Number 1
 * 
 * Write a javascript program to create a new string from a given string taking the first 3 characters and the last 3 characaters of the string and adding them together. The string length must be 3 or more, if not, the origianl string is returned.
 * 
 */



const result = (str)=>{
    let newString = null;

    if(str.length >= 3){
        //Taking the 3 frist letters
        let fisrt3_characters = str.slice(0,3);
        let last3_characters = str.slice(str.length - 3);

        newString = fisrt3_characters + last3_characters;

        return newString;
    }else{
        return str;
    }
}

// console.log(result("abc"));
// console.log(result("abcdef  "));


const firstHalf = (str)=>{
    return str.slice(0, str.length / 2);
}

console.log(firstHalf("tornado"));
console.log(firstHalf("pan"));
console.log(firstHalf("cerveza"));

const closesTo100 = (a,b)=>{

    if((100 - a) < (100 -b)){
        return a;
    }else{
        return b;
    }
}

console.log(closesTo100(99,1));
console.log(closesTo100(80,20));
console.log(closesTo100(45,55));
console.log(closesTo100(4,96));


/**
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
console.log(check_if_contains2T04("ooooh","o"));
console.log(check_if_contains2T04("oh","o"));
console.log(check_if_contains2T04("oooh","o"));
