##### PARTIE 1 #####

x = c(1,3,2.7,-1,3,4,6)
y = x>3
z = x[x>3]

### Question 1 ###
mode(x) #type de x
length(x) #taille de x

### Question 2 ###
summary(x) #résumé des valeurs statistiques de x Exemple: min, max, moy
#hist(x) #donne l'histogramme de x

### Question 3 ###
which(x == 3) #Donne l'indice des élements de x == 3
which(x > 3) #Donne les indice des éléments de x > 3



##### PARTIE 2 #####

### Question 1 ###
a1 = numeric(10)
a2 = character(10)
a3 = logical(10)

### Question 2 ###
b1 = as.numeric(y)
b2 = as.character(x)
b3 = as.logical(x)

### Question 3 ###
c1 = is.numeric(x)
c2 = is.numeric(y)
c3 = is.character(b2)
c4 = is.character(x)
c5 = is.logical(y)
c6 = is.logical(x)

### Question 4 ###
d <- c(2,5,3,5,5,-1,3,-1,-1,5,5,5)
d
class(d) #équivalent à mode
levels(d) #
summary(d)


e <- factor(d) #Regroupe les termes par groupe facteur
e
class(e)
levels(e) #Donne les termes unique
summary(e) #Donne la quantité par termes

f <- factor(d)
levels(f) <- c("A","B","C","D") #Remplace les termes unique par les éléments
f

##### PARTIE 5 #####
g = c(1,2,3,4,5)
h = c(2,3,4,5,6)
i = c(3,4,5,6,7)

df = data.frame(g,h,i) #Créer un objet data frame
df

nrow(df) #Donne le nombre de ligne du df
ncol(df) #Donne le nombre de colonne du df

rownames(df) #Donne le nom des lignes
colnames(df) #Donne le nom des colonnes
colnames(df) <- c("A","B","C")

us = read.table('USArrests.data') #Charge un fichier de données
us[1] #Donne la première colonne
us[1:3] #Donne la colonne 1 à 3
us[1,] #Donne la ligne 1
us[1:3,] #Donne la ligne 1 à 3
us[,1] #Donne le vecteur de la colonne 1, toutes ces valeurs
us[1,1] #Donne la valeur de la case 1,1

#attach(us) #Créer des varaible pour chaque colonne du DF qui représente le vecteur colonne correspondant



##### PARTIE 5 #####

# Représenter N(5,3)
k <- seq(-10, 20, length=1000) #Sequence de nombre entre x et y avec n nombres
l = dnorm(k,mean=5,sd=3) #Densité de la loi normale N(5,3)
#plot(l) #Graphique de la loi Normale 

#P(0 < X < 12)
m <- pnorm(12,mean=5,sd=3) - pnorm(0,mean=5,sd=3)

#3 quantile
n <- qnorm(0.75, mean=5, sd=3) #qnorm donne un quantile, 0,75 pour le 3eme

#Intervalle de confiance à 95%
o_inf = qnorm((1 - 0.95) / 2, mean=5, sd=3) #Intervalle de confiance inférieur
o_sup = qnorm((1 + 0.95) / 2, mean=5, sd=3) #Intervalle de confiance supérieur



##### PARTIE 6 #####
source("addition.R") #Permet de charger le fichier addtion
addition(2,2) #utilise la fonction addition
p <- c(0,10)
moyenne(p)