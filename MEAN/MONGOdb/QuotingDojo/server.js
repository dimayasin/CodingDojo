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

var server=app.listen(5000, function () {
  console.log("listening on port 5000");
})
var io = require('socket.io').listen(server);

// setting up mongoose
var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/QuotingDojo');
var UserSchema = new mongoose.Schema({
  name: { type: String },
  quote: { type: String },
  date: { type: Date, default: Date.now }
})

UserSchema.path('name').required(true, 'Name cannot be blank');
UserSchema.path('quote').required(true, 'Quote cannot be blank');

mongoose.model('User', UserSchema);

var User = mongoose.model('User')
var quoteData = '';
mongoose.Promise = global.Promise;

app.get('/', function (req, res) 
{
      res.render('index');
  
})

app.get('/quotes', function(req, res) {
	User.find({},  function(err, users){
		console.log(users);
		quoteData = users;
		if (err)
		{
			console.log('could not get users')
		}
		else {
			
		}
	}).sort('-date');
	// This is where we would get the users from the database and send them to the index view to be displayed.
	res.render('quotes');
})

io.sockets.on('connection', function(socket) {
	console.log('WE ARE USING SOCKETS!');
	console.log(socket.id);
	socket.emit('quotes', quoteData);
})
app.post('/quotes', function (req, res) 
{
  console.log("POST DATA", req.body);
  
  var Q = new User();
  Q.name = req.body.name;
  Q.quote= req.body.quote;
    
  Q.save(function (err) 
  {
    // if there is an error console.log that something went wrong!
    if (err) 
    {
      res.render('index', {title: 'you have errors!', errors: quoter.errors});
    } 
    else 
    { // else console.log that we did well and then redirect to the root route
      res.redirect('/quotes');
    }
  })
})


