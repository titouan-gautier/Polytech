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

## EXERCICE 2 ##

# 2.1

pairs(vins)
correlations <- cor(vins)

#Corrélation entre :
# sucre et sulphates
# acicdite et alcool

# 2.2
# Oui elle est significative on puet le voir sur le graphique et sa valeur est superieur a 0.5











