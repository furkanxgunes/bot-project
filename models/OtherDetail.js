const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//create Schmea
const ProductOtherDetailSchema = new Schema({
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Product"
  },
  stock:Boolean,
  title:String,
  category:String,
  seller:String,
  brand:String,
  image:String,
  description:String,
});

const ProductOtherDetail = mongoose.model('OtherDetail', ProductOtherDetailSchema);

module.exports = ProductOtherDetail;