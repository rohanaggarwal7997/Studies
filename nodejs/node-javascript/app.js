var http=require('http');
var module1=require('./module2');

http.createServer(function (request,response)
{
    response.writeHead(200,{'Content-Type':'text/plain'});
    response.write(module1.myVariable);
    response.end();
}).listen(8000);