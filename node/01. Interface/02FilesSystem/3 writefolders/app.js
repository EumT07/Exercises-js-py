const fs = require("fs");

//mkdir: Create a new folder

//Sync

fs.mkdirSync("img");

//Asyncr


fs.mkdir("html", (err) => {
    if(err){
        throw ("There is a " + err)
    }
    console.log("Carpeta creada");
});


//To be sure if the folder Exist or not
let folder = "Javascript";


if(fs.existsSync(folder)){
    console.log("The folder exist");
}else{
    fs.mkdir(folder, (err)=>{
        if(err){
            throw (err)
        }
        console.log("The folder has been created");
    })
}
