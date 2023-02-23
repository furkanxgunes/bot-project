const Product = require("../models/Product");
const {spawn} = require('child_process');

exports.addProduct = async (req, res, next) => {
  try {
    // console.log(req.body);
    
    const addedData = await Product.create(req.body);
    res.status(200).send(JSON.stringify(addedData));

    var dataToSend;
 // spawn new child process to call the python script
 const python = spawn('python', ['../bot/trendyol_bot.py']);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 res.send(dataToSend)
 });
  } catch (error) {
    console.log(error.message);
    return res.status(403).json("You are not authorized");
  }
};

// exports.getAssignmentsWithStudentsAndClass = async (req, res) => {
//   try {
//     const filter = req.params.id!=undefined?{
//       _id:req.params.id
//     }:null;
//     const assignments = await Assignment.find(filter).populate({
//       path: "students",
//       select: "name age class",
//       model: Student,
//       populate: {
//         path: "class",
//         model: "Class",
//         select: "name",
//       },
//     });  

//     return res.status(200).send(assignments);
//   } catch (error) {
//     console.log(error.message);
//     return res.status(403).json("You are not authorized");
//   }
// };
 
