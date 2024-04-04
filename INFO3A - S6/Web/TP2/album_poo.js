'use strict';

const fs = require('fs');
const { title } = require('process');

class Album {

    constructor({title, artist, year}) {
        this.title = title;
        this.artist = artist;
        this.year = year;

    }

    getTitle() {
        return this.title;
    }

    getArtist() {
        return this.artist;
    }

    getYear() {
        return this.year;
    }

}

async function readJSON() {

    const jsonData = require('./album.json')
    const listePaire = []

    for (let [key, value] of Object.entries(jsonData)) {
        listePaire.push([key, value]);
    }

    const listePaireObjet = listePaire.map(([title,object]) => [title, new Album(object)])
    const listeObjet = listePaireObjet.map(([title,object]) => ({[title]: object}))

    console.log(listeObjet)
}

/* const album = new Album({ title: "Album Title", artist: "Artist Name", year: 2024 });
console.log(album.getTitle()); */

readJSON();