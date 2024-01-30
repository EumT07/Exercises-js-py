"use strcit"
// npm i mongoose -s 
const mongoose = require("mongoose");

const dbConnect = () => {
    const DB_Uri = process.env.DB_Uri;
    mongoose.connect(DB_Uri, {
        useNerUrlParser: true,
        useUnifiedTopology: true,
        family: 4
    })
}

module.exports = db.dbConnect