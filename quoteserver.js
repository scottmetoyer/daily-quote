var fs = require('fs');
var http = require('http');

http.createServer(function (req, res) {
    var output = { };
    
    try {   
        var quotes = []
        quotes = fs.readFileSync('./quotes.txt').toString().split('\n');
    
        // Grab a random quote
        var quote = quotes[Math.floor((Math.random() * (quotes.length)))].trim().split('-');
        output = { text: quote[0].trim(), author: quote[1].trim() };
    }
    catch(ex) {
        output = ex.toString();
    }
    
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.write(JSON.stringify(output));
    res.end();
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');