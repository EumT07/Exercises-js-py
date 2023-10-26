"use strict"

const http = require("http");

//Server without HTML

let server = http.createServer((req, res)=>{
    //header
    res.writeHead(200, {"content-type" : "text/plain"});
    res.end("Hola mundo!");
});

//Server is running
server.listen(3000, ()=>{
    console.log("Server is starting right now.. on Port 3000");
});


//Server with HTML

let server2 = http.createServer((req, res)=>{
    //Header
    res.writeHead(200, {"content-type" : "text/html"});
    res.end(`<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Documento html</title>
    </head>
    <body>
        <h1>Hola mundo bellisimo</h1>
    </body>
    </html>`);
});

server2.listen(3000, ()=>{
    console.log("Server is starting right now.. on Port 3000");
});