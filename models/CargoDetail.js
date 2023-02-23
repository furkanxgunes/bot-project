const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//create Schmea
const CargoDetailSchema = new Schema({
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Product"
  },
  fast_delivery:Boolean,
  free_cargo:Boolean,
  description:String,
});

const CargoDetail = mongoose.model('CargoDetail', CargoDetailSchema);

module.exports = CargoDetail; 