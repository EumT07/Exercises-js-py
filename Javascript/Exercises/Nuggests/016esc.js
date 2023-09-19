"use strict"

//At return index

const scores = [34,56,78]

const lastNumber = scores.at(-1)
const firstNumber = scores.at(0)
console.log(lastNumber);
console.log(firstNumber);

//Fecth
async function getData(params) {
    const resp = await fetch('https://www.course-api.com/react-tabs-project');
    const data = await resp.json();
    console.log(data);
}

getData()