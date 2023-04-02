const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/fake/people', (req, res) => {
  res.sendFile(__dirname + '/public/fake_entity_person.html')
})

app.get('/fake/locations', (req, res) => {
  res.sendFile(__dirname + '/public/fake_entity_locations.html')
})

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});