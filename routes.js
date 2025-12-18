const express = require('express');
const app = express();
const User = require('./models/User');
const Product = require('./models/Product');

// Signup Route
app.post('/signup', async (req, res) => {
  const newUser = new User({
    username: req.body.username,
    email: req.body.email,
    password: req.body.password,
  });
  await newUser.save();
  res.json(newUser);
});

// Get all products
app.get('/products', async (req, res) => {
  const products = await Product.find();
  res.json(products);
});

// Add product
app.post('/products', async (req, res) => {
  const newProduct = new Product(req.body);
  await newProduct.save();
  res.json(newProduct);
});
