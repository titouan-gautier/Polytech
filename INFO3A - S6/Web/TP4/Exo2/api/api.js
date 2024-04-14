'use strict';

// import du module Express
let express = require('express');
let app = express();
const db = require('./data/db.json');

app.get('/genres/', (req, res) => {

    const genres = JSON.stringify(db.genres);

    res.set('Content-Type', 'application/json');

    res.send(genres);

    res.end();

});

app.get('/genres/:genreId/artists', (req, res) => {

    const artists = db.artists.filter((elem) => elem.genreId === req.params.genreId);

    res.set('Content-Type', 'application/json');

    res.send(artists);
});

app.get('/artists/:artistId/albums', (req, res) => {

    const albums = db.albums.filter((elem) => elem.artistId === req.params.artistId);

    res.set('Content-Type', 'application/json');

    res.send(albums);

});


// export de notre application vers le serveur principal
module.exports = app;
