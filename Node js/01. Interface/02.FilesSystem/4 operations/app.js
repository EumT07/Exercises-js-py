const fs = require("fs");

const file = "text4.txt";
const content = "Nuevo archivo"

// creat a file

fs.writeFile(file, content, (err)=>{
    if(err){
        throw ("There was an err")
    }
    console.log("the file was created");
})


//Creat a folder

fs.mkdir("html", (err) => {
    if(err){
        throw ("There is a " + err)
    }
    console.log("Carpeta creada");
});


// Basic Operations
//====================== rename ===========================
//1 Syncr

fs.renameSync("./text4.txt", "./text5.txt" );


//2 ASyncr

fs.rename("./text4.txt", "./text5.txt", (err)=> {
    if(err){
        throw(err);
    }
    console.log("The file was rename");
} );


//====================== move file ==========================


fs.rename("./text4.txt", "./html/text4.txt", (err)=>{
    if(err){
        throw(err);
    }
    console.log("this file was moved")
})


//====================== delete file ==========================


fs.unlinkSync("./html/text4.txt");
console.log("This file was deleted");

