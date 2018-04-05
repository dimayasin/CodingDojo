var express = require("express");
var bodyParser = require('body-parser');
var session = require('express-session');

var app = express();
app.use(express.static(__dirname + "/static"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({ secret: 'codingdojorocks' }));  // string for encryption


app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');


app.get('/', function (req, res) {
 
  res.render('index');
});
// Ninja Level 1

app.post('/results', function (req, res) {
  var info = req.body;
  res.render('results', {info: info});
});

// Ninja Level 2
app.get('/back', function (req, res) {

  res.redirect('/');
});



app.listen(5000, function () {
  console.log("listening on port 5000");
})
