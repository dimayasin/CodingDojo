var express = require("express");
var app = express();

var bodyParser = require('body-parser');
// use it!
app.use(bodyParser.urlencoded({extended: true}));

// new code:
var session = require('express-session');
// original code:
var app = express();
// more new code:
app.use(session({secret: 'codingdojorocks'}));  // string for encryption


// app.get('/', function (request, response) {
//   response.send("<h1>Hello Express</h1>");
// })

app.get('/', function (req, res){
  res.render('index', {title: "my Express project"});
});
app.use(express.static(__dirname + "/static"));

app.set('views', __dirname + '/views');

app.set('view engine', 'ejs');

app.get("/users", function (request, response){
  // hard-coded user data
  var users_array = [
      {name: "Michael", email: "michael@codingdojo.com"}, 
      {name: "Jay", email: "jay@codingdojo.com"}, 
      {name: "Brendan", email: "brendan@codingdojo.com"}, 
      {name: "Andrew", email: "andrew@codingdojo.com"}
  ];
  response.render('users', {users: users_array});
})

app.post('/users', function (req, res){
  console.log("POST DATA \n\n", req.body)
  //code to add user to db goes here!
  // redirect the user back to the root route.  
  res.redirect('/')
});

// app.HTTP_VERB('URL', function (req, res){});


app.listen(8000, function() {
  console.log("listening on port 8000");
})
