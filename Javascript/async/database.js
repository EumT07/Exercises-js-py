const util = require("util");
const sleep = util.promisify(setTimeout);


module.exports = {
    async taskOne(){
        try{
            // throw new Error("There is a problem")
            await sleep(4000);
            return "Task One";
        }
        catch(err){
            console.log("Err in TaskOne",err)
        }
    },
    async taskTwo(){
        try{
            await sleep(2000);
            return "Task Two";
        }
        catch(err){
            console.log("Err in TaskTwo",err)
        }
    }
}

