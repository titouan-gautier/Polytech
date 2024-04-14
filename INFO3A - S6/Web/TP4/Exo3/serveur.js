'use strict';

const api = require('./api/api')
const express = require('express');
const app = express();

app.use(express.static('public'));

app.use('/api', api);

app.listen(8080);
