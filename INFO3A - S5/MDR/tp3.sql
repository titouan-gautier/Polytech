-- DROP TABLE --
drop table PRISE_POTION;
drop table COMPOSITION;
drop table PATIENT;
drop table POTION;
drop table COMPOSITIONINGREDIENT;
drop table INGREDIENT;
drop view potion_and_ingredient;

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
    noPotion NUMBER GENERATED ALWAYS AS IDENTITY,
    nomPotion VARCHAR2(50) PRIMARY KEY,
    Origine VARCHAR2(100),
    druideCreateur VARCHAR2(50),
    genre VARCHAR2(50),
    dateCreation DATE,
    posologie NUMBER,
    nbIngredient NUMBER
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
    QuantiteUtilise NUMBER,
    FOREIGN KEY (nomPotion) REFERENCES POTION(nomPotion),
    FOREIGN KEY (nomIngredient) REFERENCES INGREDIENT(nomIngredient),
    PRIMARY KEY (nomPotion, nomIngredient)
);

CREATE TABLE COMPOSITIONINGREDIENT (
    nomIngredient     VARCHAR2(50),
    nomSousIngredient VARCHAR2(100),
    quantiteUtilise   NUMBER,
    PRIMARY KEY (nomIngredient, nomSousIngredient),
    FOREIGN KEY (nomIngredient) REFERENCES INGREDIENT (nomIngredient),
    CONSTRAINT maxQte CHECK ( quantiteUtilise <= 5 ),
    CONSTRAINT ingredientDifferent check ( nomSousIngredient <> nomIngredient ));

--- MISE A JOUR DE LA BASE ---

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
INSERT INTO COMPOSITION (nomPotion, nomIngredient, QuantiteUtilise)
VALUES ('Potion2', 'Feuille de Laurier', 2);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, QuantiteUtilise)
VALUES ('Potion2', 'Racine de Mandragore', 2);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, QuantiteUtilise)
VALUES ('Potion3', 'Racine de Mandragore', 1);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, QuantiteUtilise)
VALUES ('Potion4', 'Serpentardium', 3);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, QuantiteUtilise)
VALUES ('Potion5', 'Racine de Mandragore', 2);
INSERT INTO COMPOSITION (nomPotion, nomIngredient, QuantiteUtilise)
VALUES ('Potion6', 'Baie de Sureau', 2);

INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Feuille de Laurier', 'Herbe', 2);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Racine de Mandragore', 'Arbre', 1);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Serpentardium', 'Ecaille', 3);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Baie de Sureau', 'Fruit', 2);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Serpentardium', 'Venin', 4);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES('Œil de Trithemius', 'Pupille', 1);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES('Feuille de Laurier', 'Branche', 1);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Baie de Sureau', 'Baguette', 1);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Baie de Sureau', 'Feuille de Laurier', 1);
INSERT INTO CompositionIngredient (nomIngredient, nomSousIngredient, QuantiteUtilise)
VALUES ('Serpentardium', 'Baie de Sureau', 1);

------------------------------ CHAPITRE 2 ----------------------------------

-- Question 3.1 --

CREATE OR REPLACE TRIGGER nbIngredientPotion
BEFORE INSERT OR UPDATE
ON POTION
FOR EACH ROW
    DECLARE
    v_nbIngredient NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_nbIngredient
    FROM COMPOSITION c
    WHERE c.nomPotion = :NEW.nomPotion;

    :NEW.nbIngredient := v_nbIngredient;
END;

INSERT INTO POTION (nomPotion, Origine, druideCreateur, genre, dateCreation, posologie)
VALUES ('Potion16','Latine','Amnesix', 'Envoûtante', TO_DATE('15-11-2023', 'DD-MM-YYYY'), 1);

update POTION set posologie = 2 where POTION.nomPotion = 'Potion2';

-- Question 3.2 --

CREATE OR REPLACE PROCEDURE MiseAJourNbIngredient AS
BEGIN
    FOR rec IN (SELECT DISTINCT nomPotion FROM COMPOSITION) LOOP
        UPDATE POTION
        SET nbIngredient = (SELECT COUNT(*) FROM COMPOSITION WHERE nomPotion = rec.nomPotion)
        WHERE nomPotion = rec.nomPotion;
    END LOOP;
END MiseAJourNbIngredient;

CALL MiseAJourNbIngredient();

-- Question 3.3 --



-- Question 4.1 --



CREATE VIEW potion_and_ingredient as
SELECT p.nomPotion, c.nomIngredient, p.nbIngredient from POTION p, COMPOSITION c
where p.nomPotion = c.nomPotion;

-- Question 4.2 --
DELETE FROM POTION_AND_INGREDIENT
where nbIngredient >= 2;

-- Question 5.1 --
SELECT distinct
  CI.nomIngredient AS ingredient,
  CI.nomSousIngredient AS sousIngredient,
  LEVEL AS hierarchy_level
FROM
  CompositionIngredient CI, INGREDIENT i
START WITH
  CI.nomIngredient = 'Baie de Sureau'
CONNECT BY
  PRIOR CI.nomSousIngredient = CI.nomIngredient
ORDER BY
  hierarchy_level, sousIngredient;

-- Question 5.2 --

SELECT
    ci.nomSousIngredient as sousIngredient,
    ci.nomIngredient as ingredient,
    LEVEL as hierarchy_level
FROM
    COMPOSITIONINGREDIENT ci
START WITH
    ci.nomSousIngredient = 'Feuille de Laurier'
CONNECT BY
    PRIOR ci.nomIngredient = ci.nomSousIngredient
ORDER BY
    hierarchy_level, ingredient;

------------------------------ CHAPITRE 3 ----------------------------------

-- Question 1.1 --
select * from dba_users;

-- Question 1.2 --
select grantee, privilege from dba_sys_privs;

-- Question 1.3 --
select granted_role from dba_role_privs;

-- Question 1.4 --
select grantee, granted_role from dba_role_privs;

-- Question 1.5 --
select username, bytes, max_bytes, max_blocks from dba_ts_quotas;

-- Question 2.1 --
create user notho identified by notho;

-- Question 2.2 --

-- Question 2.3 --
GRANT CREATE TABLE to notho;

CREATE ROLE NouveauRole;

------------------------------ CHAPITRE 4 ----------------------------------

select * from dba_tablespaces;

select * from dba_data_files;

select * from all_tables;

select * from ALL_TAB_COLUMNS where table_name = 'PATIENT';

select * from DBA_TAB_COMMENTS where table_name = 'PATIENT';

select * from DBA_COL_COMMENTS where table_name = 'PATIENT' and owner = 'E217657J';

-- Question 4.1 --

SELECT ROWNUM as numero_physique,
       ROWID as numero_logique,
       nom_Patient
FROM PATIENT;

SELECT *
FROM dba_data_files df
JOIN dba_tables t ON df.tablespace_name = t.tablespace_name
WHERE t.table_name = 'PATIENT';

select * from dba_data_files;

-- Question 4.2 --

-- TABLESPACE = USERS ;
-- Dans quel table space et quel schema est elle stocké
SELECT table_name, tablespace_name, owner
FROM all_tables
WHERE table_name = 'PATIENT'
      and owner = 'E217657J';

-- Danq quel fichier physique
SELECT tablespace_name, file_name
FROM dba_data_files
WHERE tablespace_name = 'USERS';


-- Question 4.3 --

SELECT segment_name, sum(bytes) as nb_octet, SUM(blocks) as nb_block
FROM dba_segments
WHERE segment_name = 'PATIENT'
    or segment_name = 'COMPOSITION'
    or segment_name = 'COMPOSITIONINGREDIENT'
    or segment_name = 'POTION'
    or segment_name = 'INGREDIENT'
group by segment_name;


SELECT TABLESPACE_NAME AS "TABLESPACE",
       SEGMENT_TYPE AS "TYPE OBJET",
       Sum(BYTES) / 1024 / 1024 AS "TAILLE (Mb)"
FROM DBA_EXTENTS
WHERE OWNER = USER
GROUP BY OWNER, TABLESPACE_NAME, SEGMENT_TYPE
ORDER BY OWNER, TABLESPACE_NAME

--- La requête fournit une vue agrégée de l'utilisation de l'espace disque par les objets (tables, indexes, etc.)
-- pour l'utilisateur courant, en présentant la taille totale en mégaoctets pour chaque type d'objet dans chaque tablespace.

SELECT
    ci.nomSousIngredient as sousIngredient,
    ci.nomIngredient as ingredient,
    LEVEL as hierarchy_level
FROM
    COMPOSITIONINGREDIENT ci
START WITH
    ci.nomSousIngredient = 'Feuille de Laurier'
CONNECT BY
    PRIOR ci.nomIngredient = ci.nomSousIngredient
ORDER BY
    hierarchy_level, ingredient;

