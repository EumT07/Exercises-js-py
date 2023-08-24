"use strict"

//Spread Operator
// Allows and iterable to spread/expand individually inside reciever
//Split into single items And copy them

const title = "Course";
const newArryTile = [...title];

// console.log(newArryTile);

//Creating a new array
const boys = ["jhon","jimmy","charles","max"];
const girls = ["anna","susan","july"];

const bestFriend = "josef";

const allFriends = [...boys,...girls,bestFriend];

// console.log(allFriends);

//Reference

const newArray_Friends = allFriends;
newArray_Friends[0] = "peter";

// console.log(allFriends);
// console.log(newArray_Friends);

//Copy
const copyArry = [...allFriends];
copyArry[0] = "andrew";

// console.log(allFriends);
// console.log(copyArry);

//Objects


const person = {name:"Lucas",age: 23};
const newPerson = {...person,city:"Barcelona"}

console.log(person); // { name: 'Lucas', age: 23 }
console.log(newPerson);// { name: 'Lucas', age: 23, city: 'Barcelona' }
