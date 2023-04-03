const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/fake/people', (req, res) => {
  res.sendFile(__dirname + '/public/fake_entity_people.html')
})

app.get('/fake/gpe', (req, res) => {
  res.sendFile(__dirname + '/public/fake_entity_gpe.html')
})

app.get('/fake/locations', (req, res) => {
  res.sendFile(__dirname + '/public/fake_entity_locations.html')
})

app.get('/fake', (req, res) => {
  res.sendFile(__dirname + '/public/fake.html')
})


app.get('/true/people', (req, res) => {
  res.sendFile(__dirname + '/public/true_entity_people.html')
})

app.get('/true/gpe', (req, res) => {
  res.sendFile(__dirname + '/public/true_entity_gpe.html')
})

app.get('/true/locations', (req, res) => {
  res.sendFile(__dirname + '/public/true_entity_locations.html')
})

app.get('/true', (req, res) => {
  res.sendFile(__dirname + '/public/true.html')
})

app.get('/russia/gpe', (req, res) => {
  res.sendFile(__dirname + '/public/russia_gpe.html')
})

app.get('/russia/people', (req, res) => {
  res.sendFile(__dirname + '/public/russia_people.html')
})


app.get('/russia/locations', (req, res) => {
  res.sendFile(__dirname + '/public/russia_locations.html')
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