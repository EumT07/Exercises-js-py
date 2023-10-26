"use strict"

const http = require("http");// http
const fs = require("fs");//File system
const path = require("path");//Path

http.createServer((req, res) => {
   //Mostrara el url
   console.log(`${req.method} se require ${req.url}`);

if(req.url == "/"){
   fs.readFile("./public/index.html", "UTF-8", (err, html) => {    
       res.writeHead(200,{"Content-type" : "text/html" });
           res.end(html);            
       })
   }else if(req.url.match(/.css$/)){
       const reqPath = path.join(__dirname, "public", req.url);
       const fileStream = fs.createReadStream(reqPath, "UTF-8");
       res.writeHead(200, {"Content-type" : "text/css"});
       fileStream.pipe(res);
       //enviar la informacion -->res ejecuta el contenido gracias a su metodo end
   }else if(req.url.match(/.js$/)){
       const reqPath = path.join(__dirname, "public", req.url);
       const fileStream = fs.createReadStream(reqPath, "UTF-8");
       res.writeHead(200, {"Content-type" : "text/js"});
       fileStream.pipe(res);
   }else{
       res.writeHead(404, {"content-type" : "text/plain"});
       res.end("404 Error");
   }
}).listen(3000); 

console.log("Server is Strating");

// req.url.match(/.css$/ -> permite encontrar el archivo que termine con la extension .css

// fs.createReadStream(): permite leer archivos con gran cantidad de informacion