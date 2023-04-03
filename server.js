const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/fakepeople', (req, res) => {
  res.sendFile(__dirname + '/public/fakepeople.html')
})

app.get('/fakegpe', (req, res) => {
  res.sendFile(__dirname + '/public/fakegpe.html')
})

app.get('/fakelocations', (req, res) => {
  res.sendFile(__dirname + '/public/fakelocations.html')
})

app.get('/fake', (req, res) => {
  res.sendFile(__dirname + '/public/fake.html')
})

app.get('/truepeople', (req, res) => {
  res.sendFile(__dirname + '/public/truepeople.html')
})

app.get('/truegpe', (req, res) => {
  res.sendFile(__dirname + '/public/truegpe.html')
})

app.get('/truelocations', (req, res) => {
  res.sendFile(__dirname + '/public/truelocations.html')
})

app.get('/true', (req, res) => {
  res.sendFile(__dirname + '/public/true.html')
})

app.get('/russiagpe', (req, res) => {
  res.sendFile(__dirname + '/public/russiagpe.html')
})

app.get('/russiapeople', (req, res) => {
  res.sendFile(__dirname + '/public/russiapeople.html')
})


app.get('/russialocations', (req, res) => {
  res.sendFile(__dirname + '/public/russialocations.html')
})


app.get('/russia', (req, res) => {
  res.sendFile(__dirname + '/public/russia.html')
})


app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});