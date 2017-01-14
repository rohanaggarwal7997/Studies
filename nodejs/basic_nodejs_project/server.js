var http=require('http');   //import module http

function onRequest(request,response)    //Handle the request to the server
{   //What response to be given
    //Change head
    response.writeHead(200,{'Content-Type':'text/plain'});
    //Key what to set and value what to write
    response.write('Hello World');
    response.end();
}
http.createServer(onRequest).listen(8000); //Listen to the port 8000



/*
* var http=require('http');

 function onRequest(request,response)
 {
 response.writeHead(200,{'Content-Type':'text/plain'});
 response.write('Hello World');
 response.end();
 }
 http.createServer(onRequest).listen(8000);
 */