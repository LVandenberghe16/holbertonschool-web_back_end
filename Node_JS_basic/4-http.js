const http = require('http');

const port = process.env.PORT || 1245;

http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('Hello Holberton School!');
  res.end();
}).listen(port, () => {
  console.log(`App is running on port ${port}`);
});
