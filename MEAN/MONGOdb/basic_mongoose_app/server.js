// setting up express, body parser, and session

var express = require("express");
var bodyParser = require('body-parser');
var session = require('express-session');

var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.use(session({ secret: 'codingdojorocks' }));  // string for encryption
app.set('view engine', 'ejs');

// setting up mongoose
var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/basic_mongoose');
var UserSchema = new mongoose.Schema({
  name: { type: String },
  age: { type: Number }
}, { timestamps: true })

mongoose.model('User', UserSchema); // We are setting this Schema in our Models as 'User'
var User = mongoose.model('User')

mongoose.Promise = global.Promise;

app.get('/', function (req, res) 
{
  User.find({}, function (err, users) {
    if (err){
      res.render('index');
    }
    else{
      res.render('index', {users:users});
    }
  })

  
})
app.post('/users', function (req, res) 
{
  console.log("POST DATA", req.body);
  
  var user = new User({ name: req.body.name, age: req.body.age });
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  user.save(function (err) 
  {
    // if there is an error console.log that something went wrong!
    if (err) 
    {
      console.log('something went wrong');
    } 
    else 
    { // else console.log that we did well and then redirect to the root route
      res.render('/', { users: user });
    }
  })
})

app.listen(5000, function () {
  console.log("listening on port 5000");
})
