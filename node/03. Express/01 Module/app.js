const express = require("express");

const app = express();

// the main route of our app
app.get("/", (request, response) => {
    console.log(request.url);
    response.send("Hello World!");
  });

app.listen(3000);

console.log("express us running")