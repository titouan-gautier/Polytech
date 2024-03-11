#tous_les_objets <- ls()
# Supprimer toutes les variables
#rm(list = tous_les_objets)

source('fonction.R')

##### PARTIE 1 #####

df = read.table('../data/medical.data')

### Question 1 ###

#Les NA représente une case vide dans le tableau NA = Non Attribué

### Question 2 ###


#attach(df)

agef <- factor(age)
groupe.sanguinf <- factor(groupe.sanguin)
nb.opf <- factor(nb.op)
poidsf <- factor(poids)
sexef <- factor(sexe)
taillef <- factor(taille)

#detach(df)

### Question 3 ###

# - Les fonctions var() -> variance er sd() -> écart type permette d'évaluer la dispersion
# - Le paramètre trim de age permet d'exclure une plage de valeur, par exemple trim = 0.1 exclu 10% des valeurs les plsu hautes et 10% des plus basses

a = mean(taille, trim = 0.2, na.rm = TRUE)
b = var(age)
c = sd(age)
d = median(age)
e = quantile(age)
f = IQR(age)

### Question 4 ###

var_age = moyenne_carre(age) - (moyenne(age) * moyenne(age))
b = var(age)

### Question 5 ###

#Donne tout les indicateurs principaux de chaque colonne du data frame
s = summary(df)

#### 1.2 ####

### Question 1 ###

# Donne la boite a moustache
#boxplot(age)

# Donne l'histogram
# breaks permet de choisir le nombre de bar de l'histogram
# freq donnes la frequence a la place de la densité
#hist(age, breaks = 20)
#hist(age,freq = FALSE)

# Donne le diagramme camemberts
#pie(summary(agef))

### Question 2 ###

# Donne la fonction de réparttion
#plot(ecdf(age))

### Question 3 ###

#Plot permet de tracer une courbe
# adjust permet de définir la souplesse de la courbe
#plot(density(age, adjust = 0.1))

# Permet de supperposer un histogramme et un plot
#hist(age, freq = FALSE)
#lines(density(age))

### Question 4 ###

# Nuage de points
#qqnorm(taille)

# Ligne qui se rapporche plus du nuages de points
#qqline(taille)

#### 1.3 ####

### Question 1 ###

#intervalle_confiance(taille)
#intervalle_confiance(poids)

### Question 2 ###

#Non

##### PARTIE 2 #####

### Question 1 ###

#Si la p-valeur est inférieure à un niveau de signification choisi (généralement 0.05), on rejette l'hypothèse nulle, ce qui signifie que 
#les données ne suivent pas une distribution normale.

#Si la p-valeur est supérieure à 0.05, on ne peut pas rejeter l'hypothèse nulle, ce qui signifie que les données semblent suivre une distribution normale.

res_shapiro_taille <- shapiro.test(taille)
# p-valeur = 0.2151 donc les données semblent suivre une loi normale

res_shapiro_poids <- shapiro.test(poids)
# p-valeur = 0.3475 donc les données semblent suivre une loi normale

### Question 2 ###

# t.test donne les intervalle de confiance 95%
# La p valeur est plus petite que 0.05 donc on rejette l'hypothèse nul, les donées ne suivent pas une loi normale
res_t_taille <- t.test(taille, mu=175, conf.level = 0.95)

### Question 3 ###

# La p valeur est au dessus de 0.05 donc on ne peut pas rejeter h0, les donées semblent suivre une loi normale
res_t_poids <- t.test(poids, mu=68, conf.level = 0.95)

### Question 4 ###

nb_homme <- sum(sexe == "M")
nb_femme <- sum(sexe == "F")
len_sexe <- length(sexe)

# On ne rejete pas car la p valeur > 0.05
res_prop_sexe <- prop.test(x = nb_homme, n = len_sexe, 0.5)

### Question 5 ###

# - conf.level agit sur l'intervalle de confiance
# - mu (moyenne) agit sur la p-valeur

### Question 6 ###

res_t_test = t.test(taille, conf.level = 0.99999999)
