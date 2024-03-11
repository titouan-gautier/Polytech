##### PARTIE 1 #####

# Import the spotify.data file
spotify_data <- read.table("spotify.data")

# Create a data frame
df <- data.frame(spotify_data)

#attach(df)

#### PARTIE 1.1 ####

### QUESTION 1 ###

s <- summary(df)
#b <- boxplot(df)
#h <- hist(df$acousticness)

### QUESTION 2 ###

# La variable acousticness présente des valeurs extrêmes, ce qui est visible sur le boxplot.

df_sorted <- df[order(-liveness), ] # On sort le dataframe par ordre décroissant de liveness
# Resultats :
# Radioactive [Imagine Dragons]                                     76
# Let It Go - James Bay Spotify Session 2015 [James Bay]            72
# She Will Be Loved - Acoustic [Maroon 5]                           70

### QUESTION 3 ###

stestBPM <- shapiro.test(BPM) # p-value < 0.05, la distribution n'est pas normale
stestDance <- shapiro.test(danceability) #p-value > 0.05, la distribution est normale
stestEnergy <- shapiro.test(energy) # p-value > 0.05, la distribution est normale
stestLiveness <- shapiro.test(liveness) # p-value < 0.05, la distribution n'est pas normale
stestValence <- shapiro.test(valence) # p-value > 0.05, la distribution est normale
stestAcousticness <- shapiro.test(acousticness) # p-value < 0.05, la distribution n'est pas normale

### QUESTION 4 ###

result <- apply(df,2,sd) # Ecart type de chaque colonne du df


#### PARTIE 1.2 ####

### QUESTION 1 ###

dfCor <- cor(df) # Matrice de corrélation

# La valence est plus lié à la danceability qu'a l'energy car la valeur de la corélation entre valence et danceability est plus proche de 1 que celle entre valence et energy.

### QUESTION 2 ###

#nuage_points <- pairs(df) # Nuage de points

### QUESTION 3 ###

# CORRELATION = COV(X,Y) / SQRT(VAR(X) * VAR(Y))
# COVARIANCE(X,Y) = MEAN(X*Y) - MEAN(X) * MEAN(Y)
# VARIANCE(X) = MEAN(X^2) - MEAN(X)^2

source('fonctions_tp3.R')

cor_dance_acou <- correlation(danceability,acousticness)

### QUESTION 4 ###

ncol(dfCor) #Donne le nombre de colonnes du df
colnames(dfCor) #Donne le nom des colonnes du df

#res_corr <- val_corr(dfCor,0.2) # Donne les colonnes qui ont une corrélation supérieur à 0.5

### QUESTION 5 ###
res <- cor.test(danceability,valence) # Test de corrélation entre danceability et acousticness

# La p-value est inférieure à 0.05, on rejette l'hypothèse nulle, il y a une corrélation entre danceability et valence == significatif
# La p-value est supereiure à 0.05, on ne rejette pas l'hypothèse nulle, mais on ne peut pas dire si il n'y a pas de corrélation == pas significatif

# Une valeur absolue de 0.7 à 1 indique une corrélation forte.
# Une valeur absolue de 0.3 à 0.7 indique une corrélation modérée.
# Une valeur absolue inférieure à 0.3 indique une corrélation faible.

# Resultats :
# data:  danceability and valence
# t = 3.9943, df = 48, p-value = 0.000222
# cor 0.4994608

# La p-value est inférieure à 0.05, on rejette l'hypothèse nulle, il y a une corrélation entre danceability et valence == significatif
# La corelation est modérée car entre 0.3 et 0.7

res2 <- cor.test(energy,acousticness) # Test de corrélation entre energy et acousticness

# Resultats :
# data:  energy and acousticness
# t = -6.8903, df = 48, p-value = 1.083e-08
# cor -0.7051655

# La p-value est inférieure à 0.05, on rejette l'hypothèse nulle, il y a une corrélation entre energy et acousticness == significatif
# La corelation est forte car entre 0.7 et 1

res3 <- cor.test(BPM,acousticness) # Test de corrélation entre BPM et acousticness

# Resultats :
# data:  BPM and acousticness
# t = -1.9242, df = 48, p-value = 0.06027
# cor -0.2676016

# La p-value est supérieure à 0.05, on ne rejette pas l'hypothèse nulle, mais on ne peut pas dire si il n'y a pas de corrélation == pas significatif
# La corelation est faible car inférieure à 0.3

res4 <- cor.test(danceability,acousticness) # Test de corrélation entre danceability et acousticness

# Resultats :
# data:  danceability and acousticness
# t = -1.5033, df = 48, p-value = 0.1393
# cor -0.2120455 

# La p-value est supérieure à 0.05, on ne rejette pas l'hypothèse nulle, mais on ne peut pas dire si il n'y a pas de corrélation == pas significatif
# La corelation est faible car inférieure à 0.3

res5 <- cor.test(energy,valence) # Test de corrélation entre energy et valence

# Resultats :
# data:  energy and valence
# t = 1.8947, df = 48, p-value = 0.06417
# cor 0.2637863 

# La p-value est supérieure à 0.05, on ne rejette pas l'hypothèse nulle, mais on ne peut pas dire si il n'y a pas de corrélation == pas significatif
# La corelation est faible car inférieure à 0.3

### QUESTION 6 ###

##### PARTIE 2 #####

#### PARTIE 2.1 ####

x <- rnorm(60, mean=0, sd=1) # Génère 60 valeurs aléatoires suivant une loi normale

y <- -3.14 * x + 7.04
z = -exp(x)
t = x^2

### QUESTION 1 ###

plot(x,t)
ress <- cor(x,y)

### QUESTION 2 ###

# Pearson = cor.test(x,y,method="pearson") (par défaut) == corrélation linéaire
# Spearman = cor.test(x,y,method="spearman") == corrélation basé sur le rang
# Kendall = cor.test(x,y,method="kendall") == corrélation basé sur le rang, plus adapté pour population + petite avec beaucoup d'égalité

