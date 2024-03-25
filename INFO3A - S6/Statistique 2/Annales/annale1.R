source('fonctions.R')

## EXERCICE 1 ##

film <- read.table('films.data')
vins <- read.table('vins.data', header = TRUE)

#attach(vins)

# 1.1
nombre_vins <- nrow(vins)

# 1.2

boxplot(chlorides,sucre,sulphates, data = vins)

# Sulphates est en grande quantité
# Chlorides présente des valeurs extremes du coté des petites 

# 1.3

plot(density(sulphates))

# C'est monomodale car un seul maximum

# 1.4

qqnorm(chlorides)
qqline(chlorides)

# On voit que les valeurs ne suivent pas la ligne de la loi normale alors notre variable ne suis pas une loi normale

# 1.5

mean_sucre <- mean(sucre)
variance_sucre <- var(sucre)

variance_non_corrigee <- mean(sucre * sucre) - mean(sucre) * mean(sucre)

# 1.6
vins_sup_13 <- vins[alcool > 13,]

# 1.7
I_sucre <- intervalle_confiance(sucre)

# 1.8
p_value <- calculate_p_value(sucre, 15)

#p_value > 0,01 alors on ne rejette pas l'hypothèse H0

## PARTI 2 ##

# 2.1

pairs(vins)
correlations <- cor(vins)

#Corrélation entre :
# sucre et sulphates
# acicdite et alcool

# Question 2 : corrélation significative

cor.test(sulphates, sucre)
# p-value < 0.05 donc la corrélation est significative


# Question 3 : calcul de la valeur observée
correlation = cor(acidite, chlorides)
n = nrow(vins)
stat_test = correlation*sqrt(n-2)/sqrt(1 - correlation^2)


# EXERCICE 2 
# Partie 2.1 Analyse 1D

# Question 1 : nombre de films dans le jeux de données
nrow(films)

# Question 2 : Combien de réalisateurs différents sont présents ?
directorf = factor(director)
length(levels(directorf))
# 73

#Question 3 : Visualisez la distribution des cat ́egories de films (genre)
genref = factor(genre)
pie(summary(genref))

# Question 4 : Les donn ́ees remettent-elles en cause l’hypoth`ese H0 d’une proportion de com ́edies  ́egale à 30% dans la population ?
prop.test(sum(genre == "Comedy"), length(genre), 0.3) # On effectue un test de proportion pour savoir si 30% de comedie est envisageable
# p-value = 0.04978 < 0.05 donc on rejette l'hypothèse


# Partie 2.2 : analyse 2D

# Question 1 : Donnez la table de contingence qui croise les deux variables.
table_g_s = table(genre,starring)


# Question 2 : Question théorique : indiquez par une formule comment vous pouvez calculer la table de contingence attendue sous hypoth`ese d’ind ́ependance.
table(genre) %*% t(table(starring)) / sum(table(genre, starring))


# Question 3 : 
table = table(starring, genre)
assocplot(table)











