var fs = require('fs');
var http = require('http');

http.createServer(function (req, res) {
    var output = '';
    
    try {   
        var quotes = []
        quotes = fs.readFileSync('./quotes.txt').toString().split('\n');
    
        // Grab a random quote
        output  = quotes[Math.floor((Math.random() * (quotes.length)))];
    }
    catch(ex) {
        output = ex.toString();
    }
    
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end(output);
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');