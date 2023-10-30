const express = require('express');
const api = express.Router();

app.get('/users', (req, res) => res.send('users'));
app.post('/user', (req, res) => res.send('user POST'));

app.get('/messages', (req, res) => res.send('messages'));
app.post('/message', (req, res) => res.send('message POST'));

module.exports = api;
