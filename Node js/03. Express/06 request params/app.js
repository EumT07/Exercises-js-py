const express = require("express");
const app = express();

app.get("/hello/:user", (req, res) => {
  res.end("Hello " + req.params.user + ".");
});

// sometimes we need to parse the params
app.get("/add/:userId", (req, res) => {
  let userId = parseInt(req.params.userId, 10);
  userId++;
  console.log(userId);
  res.send("Your user Id + 1 is: " + userId);
});

app.listen(3000);
console.log("Server on port ", 3000);