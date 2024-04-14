'use strict';

const http = require('http');

http.createServer((request, response)=>{

    if (request.method === 'GET') {

        const args = request.url.split('?');

        const html = '<!DOCTYPE html>\n' +
            '<html lang="en">\n' +
            '<head>\n' +
            '    <meta charset="UTF-8">\n' +
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n' +
            '    <title>Bonjour</title>\n' +
            '</head>\n' +
            '<body>\n' +
            '<p>Analyse de votre requête :</p>\n' +
            `<p>Vous accéder à l'url : ${args[0]}</p>\n` +
            `<p>La chaine de requête est: ${args[1]}</p>\n` +
            '</body>\n' +
            '</html>';

        response.writeHead(200, {
            'Content-Type': 'text/html',
            'Content-Length': Buffer.byteLength(html),
        });

        response.end(html);

    } else {

        response.writeHead(405, {'Content-Type': 'text/plain'});

        response.end('Erreur');

    }



}).listen(8080);


