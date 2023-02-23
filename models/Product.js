const mongoose = require("mongoose");
const Schema = mongoose.Schema;

//create Schmea
const ProductSchema = new Schema({
  link: { type: String, required: true,unique:true },
});

const Product = mongoose.model("product", ProductSchema);

module.exports = Product;
