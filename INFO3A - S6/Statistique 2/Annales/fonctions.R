intervalle_confiance <- function(echantillon) {

    # Nombre d'observations dans l'échantillon
    n <- length(echantillon)

    # Niveau de confiance (par exemple, 95%)
    confiance <- 0.90

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

#t.test(moyenne de 15)
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

sort_cor <- function(df, min) {
    cor = cor(df)

    for (i in 1:ncol(cor)) {
        for (j in i:ncol(cor)) {
            if (i!=j) {
                if (abs(cor[i,j]) > min) {
                    cat(colnames(cor)[i]," en correlation avec ", colnames(cor)[j]," avec une valeur de ",cor[i,j], "\n")
                }
            }
        }
    }
}


# Question 4 TP4 


X2_total <- function(f1, f2, K) {
    table_obs = table(f1, f2)
    table_th = (table(f1) %*% t(table(f2))/K)
    sumd2 = 0
    for (i in 1:nrow(table_obs)) {
        for (j in 1:ncol(table_obs)) {
            sumd2 = sumd2 + ((table_obs[i, j]*table_obs[i, j] - table_th[i, j]*table_th[i, j])/table_th[i,j])
        }
    }
    return (sumd2)
}


# Question 5 tp 4 

cramer <- function(f1, f2, K) {
    khi2 = X2_total(f1, f2, K)
    return (sqrt(khi2/(K*(min(nrow(table(f1,f2)), ncol(ncol(table(f1, f2)))) - 1))))
}

moyenne_carre <- function(v) {

    sum = 0

    for (i in v) {

        if (!is.na(i)) {

            sum = sum + (i*i)

        }
        

    }

    mean = sum / length(v)

    return(mean)

}

moyenne <- function(v) {
    
    sum = 0

    for (i in v) {

        if (!is.na(i)) {
            sum = sum + i
        }
        

    }

    mean = sum / length(v)

    return(mean)

}

moyenne_xy <- function(x,y) {

    sum = 0

    for (i in 1:length(x)) {

        sum = sum + x[i] * y[i]

    }

    mean = sum / length(x)

    return(mean)

}

variance <- function(v) {

    return(moyenne_carre(v) - moyenne(v) * moyenne(v))

}

covariance <- function(x,y) {

    return(moyenne(x*y) - moyenne(x) * moyenne(y))

}

correlation <- function(x,y) {
    
    return(covariance(x,y) / sqrt(variance(x) * variance(y)))

}

val_corr <- function(dfCor,min) {

    for(i in 1:ncol(dfCor)) {
        
        for(j in i:ncol(dfCor)) {
            
            if(colnames(dfCor)[i] != colnames(dfCor)[j]) {
                
                if(abs(dfCor[i,j]) > min) {
                    
                    print(paste(colnames(dfCor)[i]," et ",colnames(dfCor)[j]," : ",dfCor[i,j]))
                    
                }
                
            }
            
        }

    }

}