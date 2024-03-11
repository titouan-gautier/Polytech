khi2 <- function(facteur1, facteur2, K) {

    tableObs <- table(facteur1,facteur2)
    tableTheorique <- table(facteur1) %*% t(table(facteur2)) / K

    sumD = 0

    for (i in 1:nrow(tableObs)) {

        for (j in 1:ncol(tableObs)) {

            sumD = sumD + ((tableObs[i,j] - tableTheorique[i,j]) * (tableObs[i,j] - tableTheorique[i,j]) ) / tableTheorique[i,j]

        }


    }

    return(sumD)

}

cramer <- function(facteur1,facteur2,K) {

    khi2 = khi2(facteur1,facteur2,K)

    return(sqrt(khi2 / K * min(nrow(table(facteur1,facteur2)),ncol(table(facteur1,facteur2)) - 1)))

}