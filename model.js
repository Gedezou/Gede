const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
});

const productSchema = new mongoose.Schema({
  title: String,
  description: String,
  price: Number,
  images: [String],
  likes: { type: Number, default: 0 },
  comments: [{ user: String, text: String }],
});

const User = mongoose.model('User', userSchema);
const Product = mongoose.model('Product', productSchema);
