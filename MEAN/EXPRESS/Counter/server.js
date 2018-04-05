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
  var counter = 0;
  if (req.session.counter != null || req.session.counter == 0 ) {
    req.session.counter += 1;
    counter = req.session.counter;
    // console.log(counter);
  }
  else {
    req.session.counter = 1;

    counter = 1;
  }
  res.render('index', { counter: counter });
});
// Ninja Level 1

app.get('/result', function (req, res) {
  var counter = 0;
  if (req.session.counter != null) {
    req.session.counter += 3;
    counter = req.session.counter;
    // console.log(counter);
  }
  else {
    req.session.counter = 3;

    counter = 3;
  }
  res.redirect('/');
});

// Ninja Level 2
app.get('/back', function (req, res) {

  res.redirect('/');
});



app.listen(8000, function () {
  console.log("listening on port 8000");
})
