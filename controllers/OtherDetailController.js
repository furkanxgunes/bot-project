const OtherDetail = require("../models/OtherDetail");

exports.addOtherDetail = async (req, res, next) => {
  try {
    const addedData = await OtherDetail.findOneAndUpdate(
      {product:req.body.product},
      { $set: req.body },
      { upsert: true, new: true }
      );
    res.status(200).send(JSON.stringify(addedData));

  } catch (error) {
    console.log(error.message);
    return res.status(403).json("You are not authorized"); 
  }
};

 
