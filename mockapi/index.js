const express = require('express');

const app = express();
const PORT = 3001;

app.get('/api1', (req, res) => {
    const response = {
        deductible: 1000,
        stop_loss: 10000,
        oop_max: 5000
    };
    res.status(200)
        .header('Content-type', 'application/json')
        .send(response);
});

app.get('/api2', (req, res) => {
    const response = {
        deductible: 1200,
        stop_loss: 13000,
        oop_max: 6000
    };
    res.status(200)
        .header('Content-type', 'application/json')
        .send(response);
});

app.get('/api3', (req, res) => {
    const response = {
        deductible: 1000,
        stop_loss: 10000,
        oop_max: 6000
    };
    res.status(200)
        .header('Content-type', 'application/json')
        .send(response);
});

app.listen(PORT, () => {
    console.log('mock server started');
});
