"use strict"

//Functions

//Creating
function hello() {
    console.log("Hello");
};

//Calling
hello();

//Params

function helloWorld(str1,str2) {
    const result = `${str1} ${str2}`;
    console.log(result);
}

//arguments

helloWorld("Hello","World");

// default Params

function add(n = 4) {
    const add = 4 + n;
    console.log(add);
}

add(6);//10
add();//8

/*
    REST Operator: params
*/

function lunch(food, drink, ...meals) {
    const result = `My lunch: ${food} ${drink} and ${meals} `;
    console.log(result);
};

lunch("Rice with meat","Pepsi-cola"," candies"," cup-cake"," cookies");

/**
    Spread Operator: arguments
 */

function diner(food,drink,meals1,meals2,meals3) {
    const diner = `My diner: ${food} ${drink} and ${meals1} ${meals2} ${meals3} `;
    console.log(diner);
};

let meals = ["cookies","Pie", "chocolate"];

diner("Hamburguer","Coca-cola",...meals);


/*
    Expresion functions
*/

const bye = function(str){
    console.log("Bye bye my friend ", str);
}

bye("Adios...!!");

//*** ESC6 Arrow Functions

const sayHello = ()=> console.log("Hello babies");
sayHello();

// one Param

const sayBye = (str) => console.log(str);
sayBye("Bye");

// two Params

const grettings = (a,b) => {
    console.log(a + " " + b);
}

grettings("Good", "Morning");






