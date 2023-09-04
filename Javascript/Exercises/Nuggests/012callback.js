"use strict"

function makeUpperCase(value) {
    console.log(value.toUpperCase());
}

//REverse
function reverse(value) {
    let result = value.split("").reverse().join("");
    console.log(result);
}

function full_name(name,cb) {
    const fullName = `${name} mata`;
    cb(fullName) 
}

full_name("eublan", makeUpperCase)
full_name("alberto", reverse)


//  Javascript Nuggets - Callback Hell
// after 1s first red;
// after 3s second blue; 4s
// after 2s third green; 6s
// IN SEQUENCE !!!!

const first = document.querySelector('.first')
const second = document.querySelector('.second')
const third = document.querySelector('.third')
const btn = document.querySelector('.btn')

btn.addEventListener('click', () => {
  setTimeout(() => {
    first.style.color = 'red'
    setTimeout(() => {
      second.style.color = 'blue'
      setTimeout(() => {
        third.style.color = 'green'
      }, 2000)
    }, 3000)
  }, 1000)
})