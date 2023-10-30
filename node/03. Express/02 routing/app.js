const express = require('express');
const app = express();

//settings
app.set('port', 3000);

//Router
app.get('/', (req, res)=>{
    res.send("Hello from page :3");
});

app.get('/home', (req, res)=>{
    res.send("Hello from home :3");
});

app.listen(app.get('port'), ()=>{
    console.log('Hellooooooo from my server');
});