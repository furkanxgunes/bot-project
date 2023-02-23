const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//create Schmea
const PriceSchema = new Schema({
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Product"
  },
  first_price:String,
  last_price:String,
  date_price:Date,
});

const Price = mongoose.model('Price', PriceSchema);

module.exports = Price;