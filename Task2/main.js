const express = require("express");
const app = express();
const mongoose = require("mongoose");
const User = mongoose.model("User", {
  name: String,
  email: String,
  Age: Number,
});
connectToMongoDB();
// end point for users
app.get("/api/users", async (req, res) => {
  const data = await User.find();
  res.status(200).json(data);
});

app.listen(3000, () => {
  console.log("server listening on http://localhost:3000");
});

// connect to database
function connectToMongoDB() {
  console.log("connecting.....");
  mongoose
    .connect(
      "mongodb+srv://adityaaroraaditya12:password@cosmeticdoctor.xgddwfq.mongodb.net/"
    )
    .then(console.log("DB connected succesfully"));
}
