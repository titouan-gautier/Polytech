'use strict';

const t = [0, 3, 2, 5];
console.log('Plus petite valeur ' +
    t[findMinIndex(t, 0, t.length)]);
console.log('Plus petite valeur parmi les trois dernières ' +
    t[findMinIndex(t, 1, t.length)]);
sortTable(t);
console.log(t);

/**
 * return the index of the minimal value in the array 't' from index
 * 'from' to index 'to' (excluded)
 */
function findMinIndex(t, from, to) {
    let j = from;
    for (let i = from + 1; i < to; i += 1) {
        if (t[j] > t[i]) {
            j = i;
        }
    }
    return j;
}

/**
 * sort the table 't'
 */
function sortTable(t) {
    let j, s;
    for (let i = 0; i < t.length - 1; i += 1) {
        // Find the index of the minimal value in the unsorted part of
        // the array
        j = findMinIndex(t, i, t.length);
        // Swap the ith minimal value
        s = t[j];
        t[j] = t[i];
        t[i] = s;
    }
}


// Question 1 //
//
// Ici il y a plusieur erreur de syntax dans le code, les variable i dans les boucles ne sont pas déclarées.
// Les autres variables sont déclaré avec var au lieu de let ou const
// Il n'y a pas le 'use strict'

// Question 2 //
//
// On peut détecter les erreurs de syntaxe en utilisant un linter comme ESLint.
// On peut juste lancer gulp pour voir les erruer de syntaxe avec npm start
