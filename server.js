const express = require('express');
const app = express();
const path = require('path');

// Serve static files from the 'product' directory
app.use(express.static(path.join(__dirname, 'product')));

// Serve index.html at root
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'product', 'index.html'));
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});