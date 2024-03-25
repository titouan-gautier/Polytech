#Fonctions

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