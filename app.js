const express = require("express");
const mongoose = require("mongoose");
const moment = require("moment");
const path = require("path");

const ProductController = require("./controllers/ProductController");
const OtherDetailController = require("./controllers/OtherDetailController");
const CargoDetailController = require("./controllers/CargoDetailController");
const PriceController = require("./controllers/PriceController");

const app = express();

//connect DB
mongoose.set("strictQuery", true);
mongoose.connect("mongodb://127.0.0.1:27017/bot-project");

//MIDDLEWARE
app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const hostname = "127.0.0.1";
const port = 3000;
app.get("/", (req, res) => {
  res.send("HelloWorld");
});
app.post("/product/add", ProductController.addProduct);
app.post("/product/OtherDetail/add", OtherDetailController.addOtherDetail);
app.post("/product/CargoDetail/add", CargoDetailController.addCargoDetail);
app.post("/product/Price/add", PriceController.addPrice);
app.listen(port, () => {
  console.log(`Server ${port} port is started`);
});
