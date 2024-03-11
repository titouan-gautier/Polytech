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

intervalle_confiance <- function(echantillon) {

    # Nombre d'observations dans l'échantillon
    n <- length(echantillon)

    # Niveau de confiance (par exemple, 95%)
    confiance <- 0.95

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