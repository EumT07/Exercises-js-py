"use strict"

/**
 * Creating an array
 */

let animal_list = [ "monkey", "gorila", "dog", "elephant", "eagle", "cat"];
let food_list = new Array("hamburger", "hot-dog","pizza", "empanada");
let not_array = {Hola:"hola"}

console.log("Animal list: ", animal_list);
console.log("food list: ", food_list);


//Check if is array or not
console.log(Array.isArray(animal_list));// true
console.log(Array.isArray(food_list));// true
console.log(Array.isArray(not_array));// false

//Length
console.log("Lenght Method");
console.log(animal_list.length);// 6
console.log(food_list.length);// 4

//Getting an element from array

// Gettin a random animal, insert any number inside the brackets
let dog = animal_list[2];
let first_Animal = animal_list[0];
let last_Animal = animal_list[animal_list.length -1];

console.log("Dog: ", dog);
console.log("first_Animal: ",first_Animal);
console.log("last_Animal: ",last_Animal);

//Adding arrays into a new array
console.log("\n< < < [Arrays , Arrays] > > >\n");
let animal_and_food_list = [animal_list, food_list];

console.log(animal_and_food_list[0][3]);//elephant
console.log(animal_and_food_list[1][2]);//pizza

//spread operator
console.log("< < < Spred operator > > >");
let spreadOperator = [...animal_list, ...food_list];
console.log(spreadOperator[8]);//Pizza

//Destructuring 
console.log("< < < Destructuring > > >");
let letters = ["A","B","C"];
let [a,b,c] = letters;

console.log("Letter A: ",a);
console.log("Letter B: ",b);
console.log("Letter C: ",c);

/**Arrys Methods:
 * Push
 * Pop
 * unshift
 * shift
 * indexof
 * splice
 * join
 * split
*/

console.log(("< < < Array Methods > > >\n"));

let cars = ["mustang","ferrari","volkswagen"];
console.log("Array: ",cars);

//Push: add an element At the end of the list
console.log("Push: ", cars.push("ford"));
console.log("New Arrays: ",cars);

//Pop: delete an element At the end of the list
console.log("pop: ", cars.pop());
console.log("New Arrays: ",cars);

//Unshift: add an element At the beginning of the 
console.log("unshift: ", cars.unshift("lamborgini"));
console.log("New Arrays: ",cars);

//shift: delete an element At the beginning of the 
console.log("shift: ", cars.shift());
console.log("New Arrays: ",cars);

//indexof : allow us to know the index
console.log("index: ", cars.indexOf("volkswagen"));// 2

//splice: it allows us to delete and add elements.
let fruts = ["apple","book","banana","strawberry"];
let new_Fruts = fruts.splice(1, 2,"orange");
console.log("Array of fruts: ", fruts);// result: [ 'apple', 'orange', 'strawberry' ]
console.log("splice Array of fruts: ", new_Fruts); // removed: [ 'book', 'banana' ]

//join: It allows us to create a string from an array
let cpu = ["i3 2600", "i3 5400", "i5 3600", "i5 5800","i7 5800", "i7 12000"];

let cpu_string_1 = cpu.join(" ");//i3 2600 i3 5400 i5 3600 i5 5800 i7 5800 i7 12000
let cpu_string_2 = cpu.join("-");//i3 2600-i3 5400-i5 3600-i5 5800-i7 5800-i7 12000
let cpu_string_3 = cpu.join("\n");

console.log("join(' ') : ",cpu_string_1);
console.log("join('-'): ",cpu_string_2);
console.log("join('\n'): ",cpu_string_3);

//split: It allows us to creat an array from a string
let color_list = "red, blue, yellow, purple";
let new_ArrayWithSplit = color_list.split(", ");
console.log("Split: ",new_ArrayWithSplit);

//ArrayFrom: HTML DOM
// let dishes = Array.from(document.querySelectorAll('.dishes p'));
// let dishes_list = dishes.map(element => element.textContent);

//Arrays of:
let monitor_list = Array.of("Samsung", "LG", "Benq","Dell", "Hp");
console.log("array of",monitor_list);

//Sorting

let fruts_list2 = ["Avocado","Lemon","Apple","Pear","Banana","Orange","Coconut"];

console.log("Antes: ", fruts_list2);
//sort()
console.log("Sort: ", fruts_list2.sort());
//reverse()
console.log("Reverse: ", fruts_list2.reverse());


//SET: objects are collections of values. A value in the Set may only occur once; it is unique in the Set's collection. You can iterate through the elements of a set in insertion order. The insertion order corresponds to the order in which each element was inserted into the set by the add() method successfully (that is, there wasn't an identical element already in the set when add() was called).


const array = [1, 2, 3, 4, 5, 6, 1, 2, 5, "hello", { id: 5 }, "hello"];

const miSet = new Set(array);

console.log(array);
console.log(miSet);

// .add()
miSet.add(9);
console.log(miSet);

// .delete()
miSet.delete("hola");
console.log(miSet);

// .clear()
// miSet.clear()
// console.log(miSet)

// .has() -> tienes
// console.log(array.includes(2))
console.log(miSet.has(40));

// .size
console.log(miSet.size);

miSet.forEach(valor => {
  console.log(valor);
});

const it_miSet = miSet.values();
console.log(it_miSet);

//Spred operator
const ar_miSet = [ ...miSet ]
console.log(ar_miSet[1]);



