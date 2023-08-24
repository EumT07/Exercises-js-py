"use strict"

//Rest operator ...
//Gathes/collects items
//desctructuring, function
//placemente importa, careful with the same name
// rest when declare function, spread when invoke the function.
 

//arrays

const hobbies = ["Red","write","listen to musisc","run","jump"];

const [firstHobby,...rest] = hobbies;

//Getting a specific value -> run
const run = rest.find(item => item === "run");

// console.log(firstHobby);// red
// console.log(rest);//[ 'write', 'listen to musisc', 'run', 'jump' ]
// console.log(run);// run

//Object
const user = {name:"Jess",email:"jess@gmail.com",job:"developer"};

// #1

// const {name,...other} = user;

// console.log(name);// Jess
// console.log(other);// { email: 'jess@gmail.com', job: 'developer' }

//#2
const {job,...other} = user;

// console.log(job);// developer
// console.log(other);// { name: 'Jess', email: 'jess@gmail.com' }


//Functions

const getAverage = ({name},...score) => {
    console.log(name);
    console.log(score);
    const media = score.reduce((total,items)=> total += items) / score.length;
    console.log(media.toFixed(2));
}

let scoreDta = [45,69,23,30,20,70]
// --> withour spread [ [ 45, 69, 23, 30, 20, 70 ] ]
// --> with spread [ 45, 69, 23, 30, 20, 70 ]

getAverage(user,scoreDta);
// Jess
// [ [ 45, 69, 23, 30, 20, 70 ] ]
// [ 45, 69, 23, 30, 20, 70 ]


getAverage(user,...scoreDta);//Spread operator
// Jess
// [ 45, 69, 23, 30, 20, 70 ]    
// 257