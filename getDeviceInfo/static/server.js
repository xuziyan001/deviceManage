var http = require('http');
var url = require('url');
http.createServer(function(req, res){
	var postdata = '';
	var pathname = url.parse(req.url).pathname;
	console.log("request coming from " + pathname);
	req.setEncoding('utf8');
	req.addListener('data', function(data){
		console.log('data get!')
		postdata += data;
		console.log(postdata);
	});
	req.addListener('end',function(){
		console.log('data is end!');
	})
}).listen(3000);