chocolat <- read.table('chocolat.data', header = TRUE)
attach(chocolat)

## Exercice 1 ##

# Partie 1 #

# 1.1

boxplot(chocolat)
#Le boxplot permet de voir vers ou se situe les valeurs
#On remarque que l'odeur la plus prononcé pour les consommateur est l'odeur de cacao
#Le gout le plus prononcé pour les consommateur est le gout de cacao

#1.2

chocolat_fondant <- head(chocolat[order(Fondant, decreasing = TRUE), ], 5)

#1.3

var_cacao = var(Cacao)
#La variance mesure la dispersion des valeurs autour de la moyenne
#Elle permet de voir si les valeurs sont proche ou éloigné
#Dans le cas de cacao elle permet de savoir si tous les chocolats on le meme taux de gout de caco pour les consommateurs ou si 
#ils trouvent des taux de caco différents et a quel points ils sont différents
#Ici il y a une variance de 5,24 ça veut dire que le gout de cacao resssentie par les utilisateurs varie pas mal

#1.4

stest_Fondant <- shapiro.test(Fondant)
#p-value de 0,0019, est plus petit que 0,05 donc on rejette H0 e les donné ne semble pas suivre une distribution normale

stest_Amertume <- shapiro.test(Amertume)
#p-value de 1.707e-06 est plus petit que 0,05 donc on rejette H0 e les donné ne semble pas suivre une distribution normale

#Malgres que les deux p-value soit en dessous de 0,05 celle qui pourait le plus suivre une distribution normale est la variable Fondant

#1.5

nb_amer <- nrow(chocolat[Amertume > 5,])
#Il y a 129 chocolat avec une amertume > 5

#1.6 

ttest_Amertume <- t.test(Amertume, mu = 5)
#On a une p-value de 1.156e-05 qui est < 0,05 donc on rejette H0

#Oui on rejette l'hypothèse qu'il y a autant de chocolats jugés amers
#et non amers dans la population

#1.7

intervalle_confiance_Fondant = intervalle_confiance(Fondant,0.9)

#Intervalle de confiance 90% Fondant
#Borne inférieure: 4.72587 
#Borne supérieure: 5.14213 

#On ne rejette pas l'hypothèse H0 de mu = 5 pour Fondant car 5 se trouve entre les bornes


# Partie 2 #

#2.1

cor_chocolat = cor(chocolat)
#On prend les fortes corrélation celle au dessus de 0,7

#On a une forte correlation entre cacao et OdeurCacao, ce qui est logique
#On a une forte correlation entre lait et OdeurLait
#On a une forte corelation entre Amertume et Cacao

#2.2

pairs(chocolat)
#On retrouve les meme correlation sur le graphique que dans les chiffres
#Le couple OdeurCacao et Fondant est proche de l'indépendance car son graphe est un nuage de points et non une droite ce qui montre
#une faible corrélation

#2.3

#En effet sur le couple Amertume,Lait, une grosse partie des points se trouve a gauche  et le reste est un nuage de points
#Cela représente les chocolat qui non pas de lait ou  tres peu

nb_chocolat_sans_lait = nrow(chocolat[Lait < 1,])
#Il y a 156 chcocolat qui ont tres peu de lait

#2.4

ctest_Fondant_OdeurCacao <- cor.test(Fondant,OdeurCacao)
#p-value > 0,05 donc la corrélation n'est pas significative

#2.5


#1.2.1

pie(table(NiveauFondant))
pie(table(NiveauAmertume))
#On remarque que le nombre de chaque niveau de fondant et d'amertume est quasiment égale

#1.2.2

assocplot(table(NiveauFondant,NiveauAmertume))
#On fait un assocplot pour voir le lien entre ces deux variables
#On remarque que les chocolats les plus fondant sont les moins amer
#Et les chocolat les moins fondant les plus amer

#Malgrés cette tendance il y a une bonne partie des chocolats les plus amer qui sont très fondant

#1.2.3

#Table de contingence 
table_contingence = table(NiveauFondant,NiveauAmertume)

#Table de contingence sous hypothèse d’indépendance

#1.4

stest_Fondant <- shapiro.test(Fondant)
#p-value de 0,0019, est plus petit que 0,05 donc on rejette H0 e les donné ne semble pas suivre une distribution normale

stest_Amertume <- shapiro.test(Amertume)
#p-value de 1.707e-06 est plus petit que 0,05 donc on rejette H0 e les donné ne semble pas suivre une distribution normale

#Malgres que les deux p-value soit en dessous de 0,05 celle qui pourait le plus suivre une distribution normale est la variable Fondant

#1.5

nb_amer <- nrow(chocolat[Amertume > 5,])
#Il y a 129 chocolat avec une amertume > 5

#1.6 

ttest_Amertume <- t.test(Amertume, mu = 5)
#On a une p-value de 1.156e-05 qui est < 0,05 donc on rejette H0

#Oui on rejette l'hypothèse qu'il y a autant de chocolats jugés amers
#et non amers dans la population

#1.7

intervalle_confiance_Fondant = intervalle_confiance(Fondant,0.9)

#Intervalle de confiance 90% Fondant
#Borne inférieure: 4.72587 
#Borne supérieure: 5.14213 

#On ne rejette pas l'hypothèse H0 de mu = 5 pour Fondant car 5 se trouve entre les bornes


# Partie 2 #

#2.1

cor_chocolat = cor(chocolat)
#On prend les fortes corrélation celle au dessus de 0,7

#On a une forte correlation entre cacao et OdeurCacao, ce qui est logique
#On a une forte correlation entre lait et OdeurLait
#On a une forte corelation entre Amertume et Cacao

#2.2

pairs(chocolat)
#On retrouve les meme correlation sur le graphique que dans les chiffres
#Le couple OdeurCacao et Fondant est proche de l'indépendance car son graphe est un nuage de points et non une droite ce qui montre
#une faible corrélation

#2.3

#En effet sur le couple Amertume,Lait, une grosse partie des points se trouve a gauche  et le reste est un nuage de points
#Cela représente les chocolat qui non pas de lait ou  tres peu

nb_chocolat_sans_lait = nrow(chocolat[Lait < 1,])
#Il y a 156 chcocolat qui ont tres peu de lait

#2.4

ctest_Fondant_OdeurCacao <- cor.test(Fondant,OdeurCacao)
#p-value > 0,05 donc la corrélation n'est pas significative

#2.5


# Partie 1.2 #

NiveauFondant = cut(Fondant, breaks=quantile(Fondant, probs = seq(0, 1, 0.25), names=FALSE), labels=c("faiblement fondant","légèrement fondant","plutot fondant","très fondant"), include.lowest=TRUE)

NiveauAmertume = cut(Amertume, breaks=quantile(Amertume, probs = seq(0, 1, 0.25), names=FALSE), labels=c("faiblement amer","légèrement amer","plutot amer","très amer"), include.lowest=TRUE)

#1.2.1

pie(table(NiveauFondant))
pie(table(NiveauAmertume))
#On remarque que le nombre de chaque niveau de fondant et d'amertume est quasiment égale

#1.2.2

assocplot(table(NiveauFondant,NiveauAmertume))
#On fait un assocplot pour voir le lien entre ces deux variables
#On remarque que les chocolats les plus fondant sont les moins amer
#Et les chocolat les moins fondant les plus amer

#Malgrés cette tendance il y a une bonne partie des chocolats les plus amer qui sont très fondant

#1.2.3

#Table de contingence 
table_contingence = table(NiveauFondant,NiveauAmertume)

#Table de contingence sous hypothèse d’indépendance
table_contingence_independant = table(NiveauFondant) %*% t(table(NiveauAmertume)) / sum(table(NiveauFondant, NiveauAmertume))

#1.2.4

K <- nrow(chocolat) #Nombre observation

mesure_khi2 = khi2(NiveauFondant,NiveauAmertume,K)
#La mesure du khi2 est de 41.90557

#1.2.5

#Pour savoir si les deux variable sont fortement lié on va utiliser le coef de cramer

coef_cramer = cramer(NiveauFondant,NiveauAmertume,K)
#Le coef de cramer est de 0,647 donc l'intensité de la relation est forte

### Exercice 2 ######################################################

agro = read.table('agro.data', header = TRUE)
attach(agro)

#2.1

nb_etu = nrow(agro)
#Il y a 75 etudiant

#2.2
pie(table(cursus))
#On voit que les cursus son bien réparti mais il y a une majorité de prépa

barplot(table(genre))
#On voit qu'il y a une majorité de fille

sum_note <- summary(note)
# On voit que la moyenne des notes est à 13,29 et q'une bonne partie se trouve entre 12,51 et 14,57

boxplot(note)
#La boite a moustache nous permet de voir les valeurs extreme au dessus en en dessous

#2.3

q30_note = quantile(note, 0.3)
q70_note = quantile(note, 0.7)

#Quantile 30% : 12,726
#Quantile 70% : 14,352

#2.4

var_non_corrige = mean(note * note) - mean(note) * mean(note)

#Variance non corrige = 3,73

#2.5

boxplot(note~cursus)
#On voit que la distributio des notes entre les cursus est a peu près la meme
#La prépa est un peu en dessous de BUT qui est un peu en dessous de PI
#Prépa à une plus grande plage de notes
#Elles ont toutes quelques valeurs extreme vers le bas

boxplot(note~genre)
#Les filles on des meilleurs notes que les garçon mais aussi une plus grandes plages de notes
#Les deux on quelques valeurs extreme en bas

#2.6

#Pour savoir si l'effet du cursus sur les notes est significatids je fait une anova
anova_test_cursus_note = anova(lm(note ~ cursus))
#p-value = 0,4626

# La p-value est > 0,05 donc on ne rejette pas h0 et c'est significatif

#2.7

anova_test_genre_note = anova(lm(note ~ genre))
#p-value = 0,01461

# La p-value est < 0,05 dnc on rejette H0 et c'est pas significatif



############################ FONCTIONS ###############################

intervalle_confiance <- function(echantillon, conf) {

    # Nombre d'observations dans l'échantillon
    n <- length(echantillon)

    # Niveau de confiance (par exemple, 95%)
    confiance <- conf

    # Degrés de liberté (n-1 pour un échantillon)
    degres_liberte <- n - 1

    # Valeur critique pour un intervalle à deux queues
    alpha <- 1 - confiance
    valeur_critique <- qt(confiance + alpha / 2, df = degres_liberte)

    # Estimation de la moyenne et de l'écart-type de l'échantillon
    moyenne_echantillon <- mean(echantillon, na.rm = TRUE)
    ecart_type_echantillon <- sd(echantillon, na.rm = TRUE)

    # Calcul de l'erreur standard de la moyenne (SEM)
    erreur_standard_moyenne <- ecart_type_echantillon / sqrt(n)

    # Calcul des bornes de l'intervalle de confiance
    borne_inferieure <- moyenne_echantillon - valeur_critique * erreur_standard_moyenne
    borne_superieure <- moyenne_echantillon + valeur_critique * erreur_standard_moyenne

    # Affichage des résultats
    cat("Intervalle de confiance à", confiance * 100, "% pour la moyenne :", "\n")
    cat("Borne inférieure:", borne_inferieure, "\n")
    cat("Borne supérieure:", borne_superieure, "\n")
}

calculate_p_value <- function(variable,h0) {

    sample_mean <- mean(variable)
    sample_size <- length(variable)
    population_mean <- h0
    sample_sd <- sd(variable)

    t_value <- (sample_mean - population_mean) / (sample_sd / sqrt(sample_size))
    df <- sample_size - 1
    p_value <- 2 * pt(abs(t_value), df = df, lower.tail = FALSE)

    return(p_value)

}


khi2 <- function(facteur1, facteur2, K) {
  tableObs <- table(facteur1, facteur2)
  tableTheorique <- table(facteur1) %*% t(table(facteur2)) / K
  
  sumD <- sum((tableObs - tableTheorique)^2 / tableTheorique)
  
  return(sumD)
}

cramer <- function(facteur1,facteur2,K) {

    khi2 = khi2(facteur1,facteur2,K)

    return(sqrt(khi2 / K * min(nrow(table(facteur1,facteur2)),ncol(table(facteur1,facteur2)) - 1)))

}