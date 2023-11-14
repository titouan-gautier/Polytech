select * from DRAGONS;

-- Question 1 --

select dragon from DRAGONS;

-- Question 2 --

select COMPORTEMENTAMOUREUX from .DRAGONS;

-- Question 3 --


-- Question 4 --

select dragon from "PUBLIC".DRAGONS where sexe = 'M';

-- Question 5 --

select dragon, crachedufeu from DRAGONS where sexe = 'M' and crachedufeu = 'o';

-- Question 6 --

select dragon, comportementamoureux from DRAGONS where comportementamoureux = 'timide' or comportementamoureux = 'sincere';

-- Question 7 --

select dragon, longueur from DRAGONS where longueur > 200;

-- Question 8 --

select dragon, longueur from DRAGONS where longueur > 100 and longueur < 200;

-- Question 9 --

select dragon, comportementamoureux from DRAGONS where dragon not in (select dragon from DRAGONS where comportementamoureux = 'macho' or comportementamoureux = 'timide');

-- Question 10 --

select * from DRAGONS where dragon LIKE '%oc%';

-- Question 11 --

select dragon, longueur from DRAGONS where longueur IS NULL;

-- Question 12 --

select dragon , nombreecailles - longueur as difference from DRAGONS;

------------------- EXO 2 -----------------------

-- Question 1 --

select * from REPAS;

select d.dragon,d.sexe,r.produit from DRAGONS d,REPAS r where d.dragon = r.dragon;

-- Question 2 --

select distinct d.dragon, d.sexe from DRAGONS d, REPAS r where d.dragon = r.dragon;

-- Question 3 --

select dragon,longueur from DRAGONS where longueur > (select longueur from DRAGONS where dragon like 'MissToc');

select d1.dragon from DRAGONS d1 join DRAGONS d2 on d1.longueur > d2.longueur where d2.dragon = 'MissToc';

-- Question 4 --

select d1.dragon from DRAGONS d1 join DRAGONS d2 on d1.longueur > d2.longueur and d1.nombreecailles > d2.nombreecailles where d2.dragon = 'Smeagol'

-- Question 5 --

select d.dragon,d.sexe,r.produit from DRAGONS d left join REPAS r on d.dragon = r.dragon;