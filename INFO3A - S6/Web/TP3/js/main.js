'use strict';
/* eslint-env browser, es6 */

// Pas besoin d'évenement window.onload puisqu'on utilise l'attribut defer
// lorsque l'on charge notre script

async function loadGenres() {

    let genres = '';
    const select = document.querySelector('#main select');

    try {

        genres = await fetch('http://localhost:3000/genres');
        genres = await genres.json();

    }
    catch (err) {

        console.log(err);

    }

    genres.forEach((elem) => {

        const option = document.createElement('option');
        option.textContent = elem.name;
        option.value = elem.id;

        select.appendChild(option);

    });

    select.addEventListener('change', () => {

        const genreSelect = genres.find((element) => element.id === select.value);

        loadArtists(genreSelect);

    });

    await loadArtists(genres[0]);

}

async function loadArtists(genre) {

    const mainTitle = document.querySelector('#main h2');
    mainTitle.textContent = 'Top ' + genre.name + ' artists';

    const mainParagraph = document.querySelector('#main > p');
    mainParagraph.textContent = genre.description;

    let artistByGenre = '';

    try {

        artistByGenre = await fetch('http://localhost:3000/genres/' + genre.id + '/artists');
        artistByGenre = await artistByGenre.json();

    }
    catch (err) {

        console.log(err);

    }

    const listeAlbum = document.querySelector('#main ul');

    listeAlbum.innerHTML = '';

    artistByGenre.forEach((elem) => {

        const album = document.createElement('li');

        const img = document.createElement('img');
        img.src = elem.photo;

        const lienAlbum = document.createElement('a');
        lienAlbum.href = '#';
        lienAlbum.id = elem.id;

        lienAlbum.addEventListener('click', (evt) => {

            artistSelected(evt);

        });

        const titreAlbum = document.createElement('h2');
        titreAlbum.textContent = elem.name;

        lienAlbum.appendChild(titreAlbum);

        album.appendChild(lienAlbum);
        album.appendChild(img);

        listeAlbum.appendChild(album);
    });

}

async function artistSelected(evt) {

    const idArtist = evt.target.parentElement.id;

    let albumArtist = await fetch('http://localhost:3000/artists/' + idArtist + '/albums');
    albumArtist = await albumArtist.json();

    const tableBody = document.querySelector('table > tbody');

    tableBody.innerHTML = '';

    albumArtist.forEach((album) => {

        const tableRow = document.createElement('tr');

        const tableCover = document.createElement('td');
        const cover = document.createElement('img');
        cover.src = album.cover;
        tableCover.appendChild(cover);

        const tableTitle = document.createElement('td');
        tableTitle.textContent = album.title;

        const tableYear = document.createElement('td');
        tableYear.textContent = album.year;

        const tableLabel = document.createElement('td');
        tableLabel.textContent = album.label;

        tableRow.appendChild(tableCover);
        tableRow.appendChild(tableTitle);
        tableRow.appendChild(tableYear);
        tableRow.appendChild(tableLabel);
        tableBody.appendChild(tableRow);

    });

    const albumPopUp = document.querySelector('#albums');
    const body = document.querySelector('body');

    albumPopUp.style.visibility = 'visible';
    albumPopUp.style.opacity = '1';
    albumPopUp.style.transition = 'opacity 0.5s ease-out';
    albumPopUp.style.top = `${body.clientHeight / 2 - 100}px`;
    albumPopUp.style.left = `${body.clientWidth / 2 - 350}px`;

    console.log(body.clientWidth / 2);

    const closeBtn = document.querySelector('button');

    closeBtn.addEventListener('click', () => {

        albumPopUp.style.opacity = '0';
        albumPopUp.style.visibility = 'hidden';
    });


}

loadGenres();