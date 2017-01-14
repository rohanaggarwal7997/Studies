var http=require('http');
var mod=require('./app');

http.createServer(mod.handleRequest).listen(8000);