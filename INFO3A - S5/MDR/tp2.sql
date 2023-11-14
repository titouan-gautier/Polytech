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
VALUES ('Potion4', 'Marais', 'Gargamel', 'Mystérieux', TO_DATE('20-01-2023', 'DD-MM-YYYY'), 1);
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
VALUES ('Potion14', 'Bretagne', 'Nimue', 'Envoûtante', TO_DATE('15-11-2023', 'DD-MM-YYYY'), 1);
INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion15','Latine','Nimue', 'Envoûtante', TO_DATE('15-11-2023', 'DD-MM-YYYY'), 10);




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

select * from PATIENT;
select * from POTION;
select * from PRISE_POTION;
select * from INGREDIENT;
select * from COMPOSITION;

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
WHERE P.village IS NOT NULL AND P.nom_Patient = PP.nom_Patient AND PP.nomPotion = PO.nomPotion AND PO.Origine = P.village
GROUP BY P.nom_Patient, P.village
HAVING COUNT(PP.nomPotion) >= 2;

-- Question 4 : lister les patients qui ne consomment que des potions créées par ’Panoramix ’ --

-- Question 5 : lister les patients qui ne consomment pas de potion de genre ’curatives’ ou ’magiques’ --
select pa.nom_Patient, pp.nomPotion, po.genre
from PATIENT pa, PRISE_POTION pp , POTION po
where pa.nom_Patient = pp.nom_Patient
  and pp.nomPotion = po.nomPotion EXCEPT select pa.nom_Patient, pp.nomPotion, po.genre
           from PATIENT pa, PRISE_POTION pp , POTION po
           where pa.nom_Patient = pp.nom_Patient
             and pp.nomPotion = po.nomPotion
             and (po.genre = 'Curatives' or po.genre = 'Magiques');

-- Question 6 : lister les potions créées par Amnésix et Panoramix en 52 avant J-C --

-- Question 7 : lister les ingrédients intervenant dans toutes les potions de genre ’curatif’ et la quantité totale utilisée pour chaque ingrédient --
SELECT DISTINCT i.nomIngredient
FROM INGREDIENT i, COMPOSITION c, POTION p
WHERE i.nomIngredient = c.nomIngredient AND c.nomPotion = p.nomPotion AND p.genre = 'Curatif'
AND NOT EXISTS (
    SELECT pp.nomPotion
    FROM POTION pp
    WHERE pp.genre <> 'Curatif'
    AND pp.nomPotion = p.nomPotion
);

-- Question 8 --
select distinct i.nomIngredient
from INGREDIENT i where
not exists(
    select ii.nomIngredient
    from INGREDIENT ii, COMPOSITION c
    where ii.nomIngredient = c.nomIngredient
    and ii.nomIngredient = i.nomIngredient
)


-- Question 9 --







