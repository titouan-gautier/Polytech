source('fonction.R')

# Table de contingence est une table qui permet de résumer les données de deux variables qualitatives.

telephone <- read.table("telephones.data")

#attach(telephone) # Marque	ErgonomieDesign	Ecran	Photo	Audio	Autonomie	Prix

marquef <- factor(Marque)
ergonomiedesignf <- factor(ErgonomieDesign)
ecranf <- factor(Ecran)
photof <- factor(Photo)
audiof <- factor(Audio)
autonomief <- factor(Autonomie)
prixf <- factor(Prix)

##### Partie 1 #####

### QUESTION 1 ###

sumTele <- summary(telephone)

#pie(summary(marquef))
#pie(summary(ergonomiedesignf))
#pie(summary(ecranf))
#pie(summary(photof))
#pie(summary(audiof))
#pie(summary(autonomief))
#pie(summary(prixf))

### QUESTION 2 ###

tableMarquePrix <- table(marquef,prixf) # Table de contingence entre la marque et le prix
#mosaicplot(tableMarquePrix) # Diagramme en mosaïque = table de contingence sous forme de graphe = répartition des effectifs
# Plus la collone est large, plus il y a de données, ensuite les données sont reparti en pluseiurs carré à la vertical
assocplot(tableMarquePrix) #Montre les différeences de prix entre les marques par rapport au prix moyen
# Comparaison des prix si ils était reparti uniformémeent

### QUESTION 3 ###

# Test du khi-deux
#d²ij = (nij - ntheij)² / ntheij
#ntheij = (ni * nj) / n # = K

# khi2 = somme des d²ij

K <- 101  # Car il y a 101 observations
tableMarquePrix2 <- table(Marque) %*% t(table(Prix)) / K

### QUESTION 4 ###

#La fonction fait la somme des khi carré locale pour chaque case et renvoie cette somme qui est le khi2

khi2MarquePrix <- khi2(marquef, prixf, K)
khi2MarquePhoto <- khi2(marquef,photof, K)

# On ne peux pas comparer les deux valeur de khi2 car ils n'ont pas le meme degré de liberté

### QUESTION 5 ###

# min dans cette formule represente le degré de liberté
# Plus c'est petit plus c'est indépendant
# Plus c'est grand plus c'est lié

CramerPrixMarque <- cramer(prixf,marquef,K)
CramerPrixPhoto <- cramer(prixf,photof,K) # Plus grandes valeurs
CramerPrixEcran <- cramer(prixf,ecranf,K)
CramerPrixAudio <- cramer(prixf,audiof,K)
CramerPrixAutonomie <- cramer(prixf,autonomief,K) # Plus petites valeurs

##### Partie 2 #####

testkhi2 <- chisq.test(tableMarquePrix) # Test du khi2







