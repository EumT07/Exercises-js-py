// Async await secuencial

const {taskOne, taskTwo} = require("./database");

// async function main(){
//     try{
//         console.time("Measuring time")
//         const valueOne = await taskOne();
//         const valueTwo = await taskTwo();
//         console.timeEnd("Measuring time");
//         //=====================// 
//         console.log("Task One returned: ", valueOne);
//         console.log("Task Two returned: ", valueTwo);
//     }
//     catch(err){
//         console.log("Problema dentro del try: ",err)
//     }
// }



// main();



async function main(){
    try{
        console.time("Measuring time")
        const result = await Promise.all([taskOne(),taskTwo()])
        console.timeEnd("Measuring time");
        //=====================// 
        console.log("Task One returned: ", result[0]);
        console.log("Task Two returned: ", result[1]);
    }
    catch(err){
        console.log("Problema dentro del try: ",err)
    }
}

main();

