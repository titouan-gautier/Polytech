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

CREATE TABLE COMPOSITIONINGREDIENT (
    nomIngredient VARCHAR2(50) ,
    nomSousIngredient VARCHAR2(100),
    type VARCHAR2(50),
    FOREIGN KEY (nomIngredient) REFERENCES INGREDIENT(nomIngredient)

)