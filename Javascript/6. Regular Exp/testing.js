"use strict"

//i = incase sensitive (Capitalcase/lowercase)
let regexp = /hello world/i;
console.log(regexp.test("Hello World")); // True

//Limit

let word = /\bcat\b/i;// it will be cat

console.log(word.test("cat"));
console.log(word.test("cAt"));//with i: return true
console.log(word.test("dog"));

//Search 

let regexp2 = /dog|cat|kichen/i;

console.log(regexp2.test("There is a cat"));
console.log(regexp2.test("There is a fish"));
console.log(regexp2.test("There is a DOG"));

/**
 * 
 * ^ start
 * * end
 */

let start_exp, end_exp, both_exp;

start_exp = /file/;
end_exp = /.js/;
both_exp = /^file|.js/;

console.log("file.js: ",start_exp.test("file.js"));
console.log(".js: ",end_exp.test("file.js"));

console.log(".js: ",end_exp.test("file.css"));
console.log("file.js: ",both_exp.test("file.js"));


/**
 * Methods : replace()
 */


let sentence = "I love suchi, and pizza, but I would like to eat to eat to eat a glass of water";

console.log("replace(): ", sentence.replace(/to eat/ig, "drink" ));


/***
 * 
 * loops
 * 
 */

let message = "There 2 apples, and 3 pears"

// \b = limit numbers

// let patron = /\b(\d+)\b/g;

// var match;

// while (match = patron.exec(message)) {
//     console.log(match)
//     console.log("We find ", match[1], " in this position: ", match.index);
// }





