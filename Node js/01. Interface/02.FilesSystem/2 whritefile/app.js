"use strict"

const fs = require("fs");

const file = "text3.txt";

//To be sure that there is a file inside the folder 
//===========================================================\\
// First --You can use --> if

if(fs.existsSync(file)){
    console.log("Exits a file");
}else{
    console.log("There is not a file");
}

// Second you cand use access
 
fs.access(file, fs.constants.F_OK, (err)=>{
     if(err){
         console.log("File not Exist");
     }else{
         console.log("File Exist");
     }
 })

//===========================================================\\

//Write a file 

const content = "This is a new file";

//Syncr

fs.writeFileSync(file, content);
console.log("You wrote a new file");


//Asyncr

fs.writeFile(file, content, (err) =>{
    if(err){
        throw ("There was a err when you wrote the file");
    }
    console.log("You have wrote a file");
});


//===========================================================\\

//add more content.

const newContent = "\nA new line of code";

fs.appendFile(file, newContent, (err) => {
    if(err) {
        throw("You can add more text");
    }
    console.log("You add more text");
});