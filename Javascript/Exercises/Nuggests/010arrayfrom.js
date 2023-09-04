"use strict"
// Array.from -> not on prototype

//from - returns ArraysObjects from an Object
//With a length property or an iterable object
//from - turns array-like/ish into array - node List string

const udemy = "udemy";

console.log(Array.from(udemy))


const text = document.querySelectorAll(".text");

const nexText = Array.from(text).find((el) => el.innerHTML === "chao");

// console.log(nexText)

//Page numbers
const items = Array.from({length: 120}, (_,index)=>{
    return index
})

const itemsPerPage = 14;
const pages = Math.ceil(items.length / itemsPerPage);
console.log(pages);
