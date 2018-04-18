var express = require("express");
app.use(express.static( __dirname + '/HelloAng/dist' ));

app.get('/', function (request, response) {
    response.send("<h1>Hello Express</h1>");
})

app.listen(8000, function () {
    console.log("listening on port 8000");
})