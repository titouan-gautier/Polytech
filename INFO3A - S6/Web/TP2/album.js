'use strict';

function createAlbum() {
    const album = {
        'Fresh Cream': createArtist('Cream', '1966', 'Fresh Cream'),
        'Hot Rats': createArtist('Frank Zappa', '1969', 'Hot Rate'),
        'Space Oddity': createArtist('David Bowie', '1969', 'SPace Oddity'),
        'Merry Christmas': createArtist('Mariah Carey', '1994', 'Merry Christmas'),
        'Songs from a Room': createArtist('Leonard Cohen', '1969', 'Songs from a Room'),
        'Ummagumma': createArtist('Pink Floyd', '1969', 'Ummagumma'),
        'Camembert Électrique': createArtist('Gong', '1971', 'Camembert Électrique'),
        'The Piper at the Gates of Dawn': createArtist('Pink Floyd', '1967', 'The Piper at the Gates of Dawn'),
    };

    console.log(album);

    return album;
}

function createArtist(name, year, title) {

    const artist = {
        name: name,
        year: year,
        title: title,
    };

    return artist;

}

function albumArtist(album, title) {
    return album[title].name;
}

function albumYear(album, title) {
    return album[title].year;
}

const album = createAlbum();

console.log(albumArtist(album, 'Ummagumma'));
console.log(albumYear(album, 'Ummagumma'));

console.log(JSON.stringify(album));