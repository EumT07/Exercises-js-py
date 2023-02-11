"Use strict"

let data_A = 20;
let data_B = 10;

/**
 * if
 */

console.log("\nif statements \n");

if(data_A > data_B) console.log("Data A is Greater than Data B"); // One line

if(data_A >= 18){
    console.log("Data A is Greater than Data B");
}

/**
 * if - else
*/
console.log("\nif - else statements \n");

if(data_A < data_B){
    console.log("Data A is less than Data B");
}else{
    console.log("Sorry Data A is greater than Data B");
}

/**
 * if - else if - else
*/
console.log("\nif - else if - else statements \n");

let num1 = 21;
let num2 = 22;
let str = "Hello"

if(num1 > num2){
    console.log("Result A");
}else if(num1 == 25){
    console.log("Result B");
}else if(num2 == num1){
    console.log("Result C");
}else if((num2 && num1) != str ){
    console.log("They are really different");
}

console.log("\nNested if statements \n");
/**
 * Nested if statements
*/

let value1 = "Hello"
let value2 = "ola"


if (value1 == "Hello"){
    console.log("Result : Hello, This is in English");
    if(value2 == "Hola"){
        console.log("Result : Hola,This is in Spanish");
    }else{
        console.log("No data value 2");
    }
}else{
    console.log("No data value 1");
}

/**
 * Switch
 * 
*/
console.log("\n Switch statements \n");

const color = "Violet";

switch (color) {
    case "Blue":
        console.log("This color is Blue");
        break;
    case "Yellow":
        console.log("This color is Yellow");
        break;
    case "Red":
        console.log("This color is Red");
        break;
    case "Black":
        console.log("This color is Black");
        break;
    case "White":
        console.log("This color is White");
        break;
    case "Violet":
        console.log("This color is Violet");
        break;
    default:
        console.log("That color doesn't exit");
        break;
}



