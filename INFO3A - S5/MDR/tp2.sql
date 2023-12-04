--- TP1 ---

--- CREATION DE LA BASE ---

-- DROP TABLE --

drop table PRISE_POTION;
drop table COMPOSITION;
drop table PATIENT;
drop table POTION;
drop table INGREDIENT;

-- Question 1 --

--- Utiliser https://mocodo.net/ --

-- Question 2 --

-- Création de la table PATIENT
CREATE TABLE PATIENT (
    nom_Patient VARCHAR2(50) PRIMARY KEY,
    prenom VARCHAR2(50),
    sexe CHAR(1),
    age NUMBER,
    profession VARCHAR2(100),
    village VARCHAR2(100),
    nationalite VARCHAR2(50)
);

-- Création de la table POTION
CREATE TABLE POTION (
    nomPotion VARCHAR2(50) PRIMARY KEY,
    Origine VARCHAR2(100),
    druideCreateur VARCHAR2(50),
    genre VARCHAR2(50),
    dateCreation DATE,
    posologie NUMBER
);

-- Création de la table PRISE-POTION
CREATE TABLE PRISE_POTION (
    nom_Patient VARCHAR2(50),
    nomPotion VARCHAR2(50),
    date_prise DATE,
    PRIMARY KEY (nom_Patient, nomPotion, date_prise),
    FOREIGN KEY (nom_Patient) REFERENCES PATIENT(nom_Patient),
    FOREIGN KEY (nomPotion) REFERENCES POTION(nomPotion)
);

-- Création de la table INGREDIENT
CREATE TABLE INGREDIENT (
    nomIngredient VARCHAR2(50) PRIMARY KEY,
    villeOrigine VARCHAR2(100),
    type VARCHAR2(50)
);

-- Création de la table COMPOSITION
CREATE TABLE COMPOSITION (
    nomPotion VARCHAR2(50),
    nomIngredient VARCHAR2(50),
    quantiteUtilisee NUMBER,
    FOREIGN KEY (nomPotion) REFERENCES POTION(nomPotion),
    FOREIGN KEY (nomIngredient) REFERENCES INGREDIENT(nomIngredient),
    PRIMARY KEY (nomPotion, nomIngredient)
);

--- MISE A JOUR DE LA BASE ---

-- Question 1 --

--PATIENT--
INSERT INTO PATIENT (nom_Patient, prenom, sexe, age, profession, village, nationalite)
VALUES ('Smith', 'John', 'M', 45, 'Avocat', 'NAntes', 'Anglais');
INSERT INTO PATIENT (nom_Patient, prenom, sexe, age, profession, village, nationalite)
VALUES ('Martin', 'Marie', 'F', 30, 'Infirmière', 'Paris', 'Française');
INSERT INTO PATIENT (nom_Patient, prenom, sexe, age, profession, village, nationalite)
VALUES ('Garcia', 'Luis', 'M', 38, 'Ingénieur', 'Barcelone', 'Espagnol');
INSERT INTO PATIENT (nom_Patient, prenom, sexe, age, profession, village, nationalite)
VALUES ('Mueller', 'Anna', 'F', 29, 'Scientifique', 'Londres', 'Allemande');
INSERT INTO PATIENT (nom_Patient, prenom, sexe, age, profession, village, nationalite)
VALUES ('Kim', 'Ji-hoon', 'M', 32, 'Médecin', 'Séoul', 'Coréen');

--POTION--
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion2', 'Montagne', 'Getafix', 'Magiques', TO_DATE('10-02-2023', 'DD-MM-YYYY'), 3);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion3', 'Plaine', 'Miraculix', 'Curatives', TO_DATE('05-03-2023', 'DD-MM-YYYY'), 1);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion4', 'Marais', 'Merlin', 'Mystérieux', TO_DATE('20-01-2023', 'DD-MM-YYYY'), 1);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion5', 'Londres', 'Merlin', 'Curatives', TO_DATE('12-04-2023', 'DD-MM-YYYY'), 2);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion6', 'Londres', 'Panoramix', 'Magiques', TO_DATE('03-07-2023', 'DD-MM-YYYY'), 1);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion11', NULL, 'Merlin', 'Magiques', TO_DATE('01-02-2023', 'DD-MM-YYYY'), 2);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion12', NULL, 'Circe', 'Envoûtante', TO_DATE('15-11-2023', 'DD-MM-YYYY'), 1);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion13', 'Bretagne', 'Merlin', 'Magiques', TO_DATE('01-09-2023', 'DD-MM-YYYY'), 2);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion14', 'Bretagne', 'Amnesix', 'Envoûtante', TO_DATE('15-11-2023', 'DD-MM-YYYY'), 1);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion15','Latine','Amnesix', 'Envoûtante', TO_DATE('15-11-2023', 'DD-MM-YYYY'), 10);


--PRISE_POTION--
INSERT INTO PRISE_POTION (nom_Patient, nomPotion, date_prise)
VALUES ('Smith', 'Potion2', TO_DATE('20-02-2023', 'DD-MM-YYYY'));
INSERT INTO PRISE_POTION (nom_Patient, nomPotion, date_prise)
VALUES ('Martin', 'Potion3', TO_DATE('10-03-2023', 'DD-MM-YYYY'));
INSERT INTO PRISE_POTION (nom_Patient, nomPotion, date_prise)
VALUES ('Garcia', 'Potion4', TO_DATE('02-02-2023', 'DD-MM-YYYY'));
INSERT INTO PRISE_POTION (nom_Patient, nomPotion, date_prise)
VALUES ('Mueller', 'Potion5', TO_DATE('15-04-2023', 'DD-MM-YYYY'));
INSERT INTO PRISE_POTION (nom_Patient, nomPotion, date_prise)
VALUES ('Mueller', 'Potion6', TO_DATE('15-04-2023', 'DD-MM-YYYY'));
INSERT INTO PRISE_POTION (nom_Patient, nomPotion, date_prise)
VALUES ('Kim', 'Potion6', TO_DATE('05-07-2023', 'DD-MM-YYYY'));


--INGREDIENT--
INSERT INTO INGREDIENT (nomIngredient, villeOrigine, type)
VALUES ('Feuille de Laurier', 'Athènes', 'Herbe médicinale');
INSERT INTO INGREDIENT (nomIngredient, villeOrigine, type)
VALUES ('Racine de Mandragore', 'Forêt de Brocéliande', 'Plante magique');
INSERT INTO INGREDIENT (nomIngredient, villeOrigine, type)
VALUES ('Serpentardium', 'Amazonie', 'Herbe exotique');
INSERT INTO INGREDIENT (nomIngredient, villeOrigine, type)
VALUES ('Baie de Sureau', 'Cotswolds', 'Plante médicinale');
INSERT INTO INGREDIENT (nomIngredient, villeOrigine, type)
VALUES ('Œil de Trithemius', 'Transylvanie', 'Ingrédient mystique');


--COMPOSITION--
INSERT INTO COMPOSITION (nomPotion, nomIngredient, quantiteUtilisee)
VALUES ('Potion2', 'Feuille de Laurier', 2);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, quantiteUtilisee)
VALUES ('Potion3', 'Racine de Mandragore', 1);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, quantiteUtilisee)
VALUES ('Potion4', 'Serpentardium', 3);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, quantiteUtilisee)
VALUES ('Potion5', 'Racine de Mandragore', 2);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, quantiteUtilisee)
VALUES ('Potion6', 'Baie de Sureau', 2);

-- Question 2 --
delete from POTION where origine IS NULL;

-- Question 3 --
update POTION set origine = 'Armorique' where origine = 'Bretagne';

--- CONSULTATION DE LA BASE ---

-- Question 1 : indiquer l’origine de chaque potion --
select nomPotion,origine from POTION;

-- Question 2 : lister les potions d’origine latine dont la posologie est supérieure à 5g --
select nomPotion, origine, posologie
from POTION
where Origine LIKE 'Latine' and posologie > 5;

-- Question 3 : lister les patients qui consomment au moins deux potions qui ont pour origine leur village --
SELECT P.nom_Patient, P.village, COUNT(PP.nomPotion) AS nombre_Potions_Consommees
FROM PATIENT P, PRISE_POTION PP, POTION PO
WHERE P.nom_Patient = PP.nom_Patient AND PP.nomPotion = PO.nomPotion AND PO.Origine = P.village
GROUP BY P.nom_Patient, P.village
HAVING COUNT(PP.nomPotion) >= 2;

SELECT P.nom_Patient, P.village, COUNT(PP.nomPotion) AS Potions_Consommees
FROM PATIENT P
JOIN PRISE_POTION PP ON P.nom_Patient = PP.nom_Patient
JOIN POTION PO ON PP.nomPotion = PO.nomPotion AND PO.Origine = P.village
GROUP BY P.nom_Patient, P.village
HAVING COUNT(PP.nomPotion) >= 2;

-- Question 4 : lister les patients qui ne consomment que des potions créées par ’Panoramix ’ --
select pp.nom_Patient
from PRISE_POTION pp
INNER JOIN POTION P on pp.nomPotion = P.nomPotion
where druideCreateur='Panoramix' except select pp.nom_Patient
from PRISE_POTION pp INNER JOIN POTION P on pp.nomPotion = P.nomPotion
where druideCreateur!='Panoramix';

SELECT pp.nom_Patient
FROM PRISE_POTION pp
INNER JOIN POTION P ON pp.nomPotion = P.nomPotion
WHERE P.druideCreateur = 'Panoramix' EXCEPT SELECT pp.nom_Patient
FROM PRISE_POTION pp
INNER JOIN POTION P ON pp.nomPotion = P.nomPotion
WHERE P.druideCreateur != 'Panoramix';


-- Question 5 : lister les patients qui ne consomment pas de potion de genre ’curatives’ ou ’magiques’ --
select pa.nom_Patient, pp.nomPotion, po.genre
from PATIENT pa, PRISE_POTION pp , POTION po
where pa.nom_Patient = pp.nom_Patient
  and pp.nomPotion = po.nomPotion EXCEPT select pa.nom_Patient, pp.nomPotion, po.genre
           from PATIENT pa, PRISE_POTION pp , POTION po
           where pa.nom_Patient = pp.nom_Patient
             and pp.nomPotion = po.nomPotion
             and (po.genre = 'Curatives' or po.genre = 'Magiques');

SELECT pa.nom_Patient, pp.nomPotion, po.genre
FROM PATIENT pa
JOIN PRISE_POTION pp ON pa.nom_Patient = pp.nom_Patient
JOIN POTION po ON pp.nomPotion = po.nomPotion EXCEPT SELECT pa.nom_Patient, pp.nomPotion, po.genre
FROM PATIENT pa
JOIN PRISE_POTION pp ON pa.nom_Patient = pp.nom_Patient
JOIN POTION po ON pp.nomPotion = po.nomPotion
WHERE po.genre IN ('Curatives', 'Magiques');


-- Question 6 : lister les potions créées par Amnésix et Panoramix en 52 avant J-C --
select nomPotion
from POTION po
where (druideCreateur='Panoramix'and dateCreation < to_date('-0052/01/01','syyyy/mm/dd'))
or (druideCreateur='Amnésix' and dateCreation < to_date('-0555/01/01','syyyy/mm/dd'));

-- Question 7 : lister les ingrédients intervenant dans toutes les potions de genre ’curatif’ et la quantité totale utilisée pour chaque ingrédient --
SELECT DISTINCT i.nomIngredient, sum(p.posologie) as Quantite
FROM INGREDIENT i, COMPOSITION c, POTION p
WHERE i.nomIngredient = c.nomIngredient AND c.nomPotion = p.nomPotion AND p.genre = 'Curatives'
AND NOT EXISTS (
    SELECT pp.nomPotion
    FROM POTION pp
    WHERE pp.genre <> 'Curatives'
    AND pp.nomPotion = p.nomPotion
) group by i.nomIngredient;

SELECT i.nomIngredient, SUM(p.posologie) AS Quantite
FROM INGREDIENT i
JOIN COMPOSITION c ON i.nomIngredient = c.nomIngredient
JOIN POTION p ON c.nomPotion = p.nomPotion
WHERE p.genre = 'Curatives'
  AND NOT EXISTS (
    SELECT 1
    FROM POTION pp
    WHERE pp.nomPotion = p.nomPotion AND pp.genre <> 'Curatives'
  )
GROUP BY i.nomIngredient;

-- Question 8 --
select distinct i.nomIngredient
from INGREDIENT i where
not exists(
    select ii.nomIngredient
    from INGREDIENT ii, COMPOSITION c
    where ii.nomIngredient = c.nomIngredient
    and ii.nomIngredient = i.nomIngredient
);

SELECT DISTINCT i.nomIngredient
FROM INGREDIENT i
WHERE NOT EXISTS (
    SELECT 1
    FROM COMPOSITION c
    WHERE c.nomIngredient = i.nomIngredient
);


-- Question 9 : lister les patients qui ne consomment que des potions ayant pour origine leur village --
select distinct p.nom_Patient
from Patient p, PRISE_POTION pp, POTION po
where po.nomPotion = pp.nomPotion
and pp.nom_Patient = p.nom_Patient
and not exists(
    select 1
    from POTION po2, PRISE_POTION pp2, PATIENT p2
    where po2.nomPotion = po.nomPotion
    and pp2.nom_Patient = p2.nom_Patient
    and p.nom_Patient = p2.nom_Patient
    and po2.Origine <> p2.village
);

SELECT DISTINCT p.nom_Patient
FROM PATIENT p
JOIN PRISE_POTION pp ON p.nom_Patient = pp.nom_Patient
JOIN POTION po ON pp.nomPotion = po.nomPotion
WHERE p.nom_Patient NOT IN (
    SELECT p2.nom_Patient
    FROM PATIENT p2
    JOIN PRISE_POTION pp2 ON p2.nom_Patient = pp2.nom_Patient
    JOIN POTION po2 ON pp2.nomPotion = po2.nomPotion
    WHERE po2.Origine <> p2.village
);


-- Question 10 : lister les patients qui consomment toutes les potions ayant pour origine leur village --
select distinct P.nom_Patient
from PRISE_POTION pp INNER JOIN PATIENT P on P.nom_Patient = pp.nom_Patient
INNER JOIN POTION P2 on pp.nomPotion = P2.nomPotion
where village=origine;

-- Question 11 : lister les potions et éventuellement les ingrédients qui les composent --
select po.nomPotion, co.nomIngredient from POTION po
left join COMPOSITION co on po.nomPotion = co.nomPotion;

-- Question 12 : années de création des 5 potions les plus anciennes --
SELECT EXTRACT(YEAR from dateCreation)
FROM POTION
ORDER BY dateCreation ASC
FETCH FIRST 5 ROWS ONLY;

SELECT EXTRACT(YEAR FROM dateCreation) AS Année
FROM (
    SELECT dateCreation
    FROM POTION
    ORDER BY dateCreation ASC
)
WHERE ROWNUM <= 5;

-- Question 13 : nom des druides dont le nombre de potions inventées est supérieur au nombre de potions créées par Amnésix --
select po.druideCreateur, count(*) as NB_CREE
from POTION po
group by druideCreateur
having count(*) > (select count(*) as NB_CREE
                   from POTION po
                   where po.druideCreateur = 'Amnesix'
                   group by druideCreateur);

SELECT druideCreateur
FROM POTION
GROUP BY druideCreateur
HAVING COUNT(*) > (
    SELECT COUNT(*)
    FROM POTION
    WHERE druideCreateur = 'Amnesix'
);



-- Question 14 : liste des druides qui n’ont proposé aucune potion entre 52 et 40 avant J-C --
select P.druideCreateur
from POTION P except select P.druideCreateur
from POTION P
where P.dateCreation between to_date('-0052/01/01','syyyy/mm/dd') AND to_date('-0040/01/01','syyyy/mm/dd');

SELECT druideCreateur
FROM POTION
MINUS
SELECT druideCreateur
FROM POTION
WHERE dateCreation BETWEEN to_date('-0052/01/01','syyyy/mm/dd') AND to_date('-0040/01/01','syyyy/mm/dd');


-- Question 15 : quels sont les druides dont toutes les potions créées sont dans les genres ’curatif’ et ’magique’ --
SELECT DISTINCT P.druideCreateur
FROM POTION P
WHERE NOT EXISTS (
    SELECT 1
    FROM POTION PP
    WHERE P.druideCreateur = PP.druideCreateur
    AND PP.genre NOT IN ('Curatives', 'Magiques')
);

SELECT DISTINCT P.druideCreateur
FROM POTION P
WHERE P.druideCreateur NOT IN (
    SELECT druideCreateur
    FROM POTION
    WHERE genre NOT IN ('Curatives', 'Magiques')
);





