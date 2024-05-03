'use strict';

// import du module Express
const express = require('express');
const app = express();
const fetch = require('node-fetch');
const xpath = require('xpath');
const {DOMParser} = require('xmldom');

app.get('/genres/', async (req, res) => {

    const genresReq = await fetch('http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key\n' +
        '=2c08f218f45c6f367a0f4d2b350bbffc');

    const genresXML =  await new DOMParser().parseFromString(await genresReq.text());

    const genres = xpath.select('//name/text()', genresXML).map(elem => elem.data);

    const promises = [];
    const descriptions = [];
    const json = [];

    genres.forEach((elem) => {
        promises.push(fetch('http://ws.audioscrobbler.com/2.0/?method=tag.getinfo&tag=' +
            `${elem}&api_key=2c08f218f45c6f367a0f4d2b350bbffc`));
    });

    await Promise.all(promises).then( async (responses) => {

        for (const element of responses) {
            const doc = await new DOMParser().parseFromString(await element.text());
            const summary = xpath.select('//summary/text()', doc);
            descriptions.push(summary[0].data);
        }

    });

    for (let i = 0; i < genres.length; i += 1) {
        json.push({
            name: genres[i],
            id: genres[i],
            description: descriptions[i],
        });
    }

    res.set('Content-Type', 'text/json');
    res.send(JSON.stringify(json));

});

app.get('/genres/:genreId/artists', async (req, res) => {

    const json = [];

    const artistsReq = await fetch('http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag=' + req.params.genreId + '&api_key=2c08f218f45c6f367a0f4d2b350bbffc');

    const artistsXML =  await new DOMParser().parseFromString(await artistsReq.text());

    const artistsNames = xpath.select('//artist/name/text()', artistsXML).map(elem => elem.data);

    const artistsPhoto =  xpath.select('//artist/image[@size="medium"]/text()', artistsXML).map(elem => elem.data);

    for (let i = 0; i < artistsNames.length; i += 1) {
        json.push({
            name: artistsNames[i],
            id: artistsNames[i],
            photo: artistsPhoto[i],
        });
    }

    res.set('Content-Type', 'text/json');
    res.send(JSON.stringify(json));

});
// export de notre application vers le serveur principal
module.exports = app;
