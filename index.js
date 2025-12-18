const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Everything you need!');
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
app.get('/about', (req, res) => {
  res.send('About Page');
});

app.get('/contact', (req, res) => {
  res.send('Contact Page');
});
require('dotenv').config();
