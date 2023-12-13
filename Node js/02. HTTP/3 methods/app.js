const http = require("http");
const fs = require("fs");

http.createServer((req, res) => {

    if(req.method == "GET"){
        res.writeHead(200, {"content-Type": "text/html"});
        fs.createReadStream("./index.html", "UTF-8").pipe(res);
    }else if(req.method == "POST"){
        let body = "";

        req.on("data", chunk => {body+= chunk; });

        req.on("end", () => {
        res.writeHead(200, {"content-Type": "text/html"});
        res.end(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Form</title>
            </head>
            <body>
                <h1>Form Result</h1>
                <p>${body}</p>        
            </body>
            </html>`);
        });
    }
}).listen(3000);
console.log("Server Startint on Port 3000");