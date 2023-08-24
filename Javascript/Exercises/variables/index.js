"use strict"

let name = "name"; //String
var number = 34; //Number
const _true = true;//Boolean

//Return a string
function returning_a_string(str){
    return str
}
//caclulator dunctions
const calculator = {
    add: (num1, num2) => num1 + num2,
    subtract: (num1, num2) => num1 - num2,
    multiply: (num1,num2) => num1 * num2,
    divide: (num1,num2) => num1 / num2,
    rest: (num1,num2) => num1 % num2
}

//Same length
function sameLength(valueA,valueB) {
    if(valueA.length === valueB.length){
        return "They have the same Length";
    }else{
        return "They don't have the same Length";
    }
}


//Calling all function

const showString = returning_a_string("Hello bro.!!");

//Calculator

const addResult = calculator.add(20,34);
const subtractResult = calculator.subtract(156,86);
const multiplyResult = calculator.multiply(20,5);
const divideResult = calculator.divide(35,8);
const restResult = calculator.rest(15,2);


//Length
const string1Length = sameLength("Hello","hi");
const string2Length = sameLength("Pedro","Pedro");

let name1 = "Andres";
let name2 = "Antonio";
const namesLength = sameLength(name1,name2);

const fruitList = ["Apple","Pear","Banana","Lemon","Melon","Whatermelon"];
const foodList = ["Arepa","Hamburger","Hot Dog","Spagetti","Tacos"];

const arraysLength = sameLength(fruitList,foodList);




console.log(showString);
console.log("Add: ",addResult);
console.log("Subtract: ",subtractResult);
console.log("Multiply: ", multiplyResult);
console.log("Divide: ", divideResult);
console.log("Rest: ", restResult);
console.log("------Length----");
console.log("Grettings Length 1: ",string1Length);
console.log("Grettings Length 2: ",string2Length);
console.log("Names Length: ",namesLength);
console.log("Array Length: ",arraysLength);
