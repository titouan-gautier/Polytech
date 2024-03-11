cosmetics <- read.table("cosmetics.data", header = TRUE)

#attach(cosmetics)

### QUESTION 1 ###

summary(cosmetics)
#pairs(cosmetics) # Affiche les nuages de points pour chaque paire de variables
cor_cosmetics <- cor(cosmetics) # Affiche la matrice de corrélation
# On voit qu'entre certaines varibles les points se rejoingnent, ce qui montre une corrélation

### QUESTION 2 ###

#boxplot(elastic ~ formule) #Peau plus élastique avec formule 2
#boxplot(hydrat ~ formule) #Peau plus hydratée avec formule 1
#boxplot(rides ~ formule) #Moins de rides avec formule 1
#boxplot(satisfaction ~ formule) #Plus de satisfaction avec formule 1

### QUESTION 3 ###

ttest_elastic_formule = t.test(elastic ~ formule) #Test de Student pour comparer les moyennes de deux échantillons
ttest_hydration_formule = t.test(hydrat ~ formule)
ttest_rides_formule = t.test(rides ~ formule)

#Si la p value est en dessous de 0.05 le cas esr significatif

#La formule 1 est éfficace sur les rides

### QUESTION 4 ###

#Pour le test dd fisher, il faut que les variables suivent une loi normale

hydrat1 = subset(hydrat, formule == 1)
hydrat2 = subset(hydrat, formule == 2)

#Shapiro test > 0.05 = loi normale

shap_test_hydrat1 = shapiro.test(hydrat1) # Loi normale VRAI
shap_test_hydrat2 = shapiro.test(hydrat2) # Loi normale VRAI

fisher_hydrat = var.test(hydrat1,hydrat2) #test de Fisher pour comparer les variances de deux échantillons
#P value > 0.05, on rejette H0, alors on peut utiliser le test de student au lieu du test de Welch

test_student_hydrat = t.test(hydrat1,hydrat2, var.equal = TRUE) #Test de Student pour comparer les moyennes de deux échantillons

### QUESTION 5 ###

#Calcule de la p-value pour le test de Student
t = test_student_hydrat$statistic
k = length(hydrat1)
pvalue_student_hydrat  = 2*pt(t,k-1)

# Calcul de la p-value pour le test de Fisher
x = var(hydrat1) / var(hydrat2)
pf = pf(x, length(hydrat1)-1, length(hydrat2)-1)
res = 2*(1-pf)

##### PARTIE 2 #####

deputes = read.table("députés.data", header = TRUE)

#attach(deputes)
#genre	groupe	age	experience	participation	participationSpecialite

### QUESTION 1 ###

summary(deputes)
#hist(genre)
#hist(age)
#hist(experience)
#hist(participation)
#hist(participationSpecialite)

table_genre_groupe = table(groupe, genre)
#assocplot(table_genre_groupe)

#boxplot(experience~groupe)
#boxplot(age~groupe)

### QUESTION 2 ###

#On fait apparaitre les parti de droite et de gauche
#boxplot(experience~groupe)

#boxplot(age~groupe)

### QUESTION 3 ###

#LAREM sont les plus actifs à l'assemblée
#boxplot(participation~groupe)

### QUESTION 4 ###

#Refaites les graphiques pr ́ec ́edents en utilisant le genre comme pivot cette fois-ci

#boxplot(experience~genre) # Homme plus d'expericence
#boxplot(age~genre) # Femme plus jeune
#boxplot(participation~genre) # Femme plus participative

### QUESTION 5 ###

res_anova_genre_groupe = anova(lm(participation ~ groupe))

# p value > 0.05 = significatif
# les deux inertie = colonne Sum Sq = 0.5807 et 3.5801

#inertie totale = inertie residuelle + inertie factorielle.
sum_inertie = 0.5807 + 3.5801
inertie_totale = var(participation)*(length(participation)-1)
