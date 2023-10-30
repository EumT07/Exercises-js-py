"use strict"

//Callback hell

function requesHandler(req,res){
    user.findById(req.userd, function(err,user){
        if(err){
            res.send(err);
        }else{
            Tasks.findById(user.taskId, function(err,tasks){
                if(err){
                    return res.send(err);
                }else{
                    tasks.completed = true;
                    tasks.save(function(err){
                        if(err){
                            return res.send(err);
                        }else{
                            res.send("Task Completed")
                        }
                    })
                }
            })
        }
    })
}

//Callbackhell => 

let request = requesHandler((req,res)=>{
    User.findById(req.userId, (err,user)=>{
        if(err){
            res.send(err);
        }else{
            Tasks.findById(user.taskId, (err,tasks) =>{
                if(err){
                    return res.send(err);
                }else{
                    tasks.completed = true;
                    tasks.save((err)=>{
                        if(err){
                            return res.send(err);
                        }else{
                            res.send("Task Completed")
                        }
                    })
                }
            })
        }
    })
}) 

//Promesa
 
function requesHandler(req,res){
    User.findById(req.UserId)
    .then(function(user){
        return Tasks.findById(user.tasksId)
    })
    .then(function(tasks){
        tasks.completed = true;
        return tasks.save();
    })
    .then(function(){
        res.send("Task Completed");
    })
    .catch(function(err){
        res.send(errors)
    })
}

//Promse =>
let request2 = requesHandler((req,res) => {
    User.findById(req.UserId)
    .then((user)=>{
        return Tasks.findById(user.tasksId)
    })
    .then((tasks)=>{
        tasks.completed = true;
        return tasks.save();
    })
    .then(()=>{
        res.send("Task Completed");
    })
    .catch((err)=>{
        res.send(errors)
    })
});

//Async


async function requesHandler(req,res){
    try{
        const user = await User.findById(req.UserId);
        const tasks = await Task.findById(user.taskId);
        tasks.completed = true;
        await tasks.save();
        res.send("Task Completed");
    }catch(e){
        res.send(e);
    }
}

