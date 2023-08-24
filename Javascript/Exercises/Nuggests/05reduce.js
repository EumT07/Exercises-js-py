"use strict"

//Reduce
//iterates, callback function
// reduce to a single value: number, array, object
//1st parameter ("acc") - total of all calculations
//2nd parameter ("curr") - current iteration/value

const staff = [
    {name:"bob",age:20,position:"web developer",salary:120},
    {name:"luis",age:26,position:"Android developer",salary:500},
    {name:"andrea",age:30,position:"senior",salary:80},
    {name:"miguel",age:34,position:"Backend developer",salary:350},
    {name:"carlos",age:18,position:"Frontend developer",salary:70},
];
// acc : acumulara toda las suma de los valores
//curr: sera el valor actual que esta calculando : sera la referencia de el objecto

// Getting Salary 
//Acc -> Total
//curr -> object : people from staff
const result = staff.reduce((total,person)=>{
    total += person.salary;
    return total;
},0);

console.log(result);