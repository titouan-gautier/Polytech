| Loi                  | Distribution Densité f(x) | Fonction de Répartition F(q) | Fonction Quantile F⁻¹(p) | Générateur Aléatoire            |
|----------------------|---------------------------|-------------------------------|---------------------------|----------------------------------|
| Loi Uniforme         | dunif(x, min, max)      | punif(q, min, max)          | qunif(p, min, max)     | runif(n, min, max)            |
| Loi Binomiale        | dbinom(x, size, prob)   | pbinom(q, size, prob)       | qbinom(p, size, prob)  | rbinom(n, size, prob)         |
| Loi de Poisson       | dpois(x, lambda)        | ppois(q, lambda)            | qpois(p, lambda)       | rpois(n, lambda)              |
| Loi Normale          | dnorm(x, mean, sd)      | pnorm(q, mean, sd)          | qnorm(p, mean, sd)     | rnorm(n, mean, sd)            |
| Loi de Student       | dt(x, df)               | pt(q, df)                   | qt(p, df)              | rt(n, df)                     |
| Loi du χ² (khi2)     | dchisq(x, df)           | pchisq(q, df)               | qchisq(p, df)          | rchisq(n, df)                 |
| Loi Exponentielle    | dexp(x, rate)           | pexp(q, rate)               | qexp(p, rate)          | rexp(n, rate)                 |


| Valeur de Cramer | Intensité de la Relation entre Variables       |
|-------------------|---------------------------------------------|
| < 0,10            | Relation Nulle ou Très Faible               |
| >= 0,10 et < 0,20 | Relation Faible                             |
| >= 0,20 et < 0,30 | Relation Moyenne                            |
| >= 0,30           | Relation Forte                              | 


- shapiro.test(taille) # Testez la normalite des variables
- t.test(taille, mu = 175) # test esperance    
- var.test(hydrat~formule) # comparaison de 2 variances
- prop.test(table(sexe)) # test frequence 
- cor(x, t, method="pearson") # test de correlation
- cor(x, t, method="spearman") # -0.05579328
- cor(x, t, method="kendall") # -0.1333333
- chisq.test(Marque, Ecran) # test d'indépendance chi2
- t.test(hydrat~formule, var.equal=TRUE) # comparaison de deux - échantillons student
- t.test(elastic~formule) # comparaison de deux échantillons welch

- stat_test = correlation*sqrt(n-2)/sqrt(1 - correlation^2)

p-value < seuil de risque -> on rejette H0



