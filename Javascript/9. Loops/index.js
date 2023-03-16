"use strict"

/**
 * Loops -> Ciclos
 * 2 tipos: Definidos e Indefinidos
 */

 //Ciclo For
 //Contador - Condicion - incremento/reduccion

let num1 = 10;
 // num # 0 ---> num # 10
for(let i=0; i <= num1; i++){
    // console.log("num1 #", i);
}

let num2 = 0;
// num # 10 ---> num # 0
for(let i=10; i >= num2; i--){
    // console.log("num2 #", i);
}

//** Ciclo for in */

let obj = {
    name: "Miguel",
    email: "miguelito@gmail.com",
    saludar(){
        return "Hello my friend"
    }
}

let data_obj = null;
for(data_obj in obj){
    // console.log(`Result: ${data_obj} : ${obj[data_obj]}`);
}

//** Cilo for of */: return index

let cars = ["mustang", "ferrari","lamborgini"];

let car = null;
for(car in cars){
    // console.log(cars[car]);
}

/***************************/
// Ciclo While and Do..While
/***************************/

//** Ciclo while */

let count1 = 5;

//From 5 to 0
while(count1 >= 0){
    // console.log("From 5 to 0: " + count1);
    count1--;
}

let count2 = 0;

//from 0 to 5
while (count2 <= 5) {
    // console.log("From 0 to 5: "+ count2);
    count2++;
}

//** Do While */
let count3 = 5;

do{
    // console.log(count3);
    count3--;
}while (count3 >= 2)


//** Control : break,continue,debugger */
let numbers = 20;

for (let i = 0; i <= numbers; i++) {
    console.log("numer #: ", i);
    if( i === 5){
        console.log("this is 5");
        break;
    }
    // if(i % 2 == 0){
    //     console.log("i % == 0", i);
    //     continue;
    // }
    
}
