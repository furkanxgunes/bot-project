const Price = require("../models/Price");

exports.addPrice = async (req, res, next) => {
  try {
    const addedData = await Price.create(req.body);
    res.status(200).send(JSON.stringify(addedData));
  } catch (error) {
    console.log(error.message);
    return res.status(403).json("You are not authorized"); 
  }
};

 
