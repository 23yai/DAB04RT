'use strict';
import dotenv from 'dotenv';
dotenv.config();

import express from 'express';

const app = express();

const { PORT } = process.env;

// login
app.get('/login', function (req, res) {
    res.send('Login');
});

// algo
app.get('/', function (req, res) {
    res.send('Hello World');
});

app.listen(PORT, () => {
    console.log(`http://127.0.0.1:${PORT}`);
});
