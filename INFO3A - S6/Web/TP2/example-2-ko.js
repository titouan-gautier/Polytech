'use strict';

(function () {
    let b = 0;
    const a = b = 5;

    console.log(typeof a);
    console.log(typeof b);
}());

// Question 1 //
//
// Le programme n'affiche rien car les console.log() ne sont pas dans la fonction auto-invoquée.
// et le variable b n'est pas declarée.

// Question 2 //
//
// La notation a = b = 5 est un peu particulière.