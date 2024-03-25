moyenne <- function(v) {
    
    sum = 0

    for (i in v) {

        sum = sum + i

    }

    mean = sum / length(v)

    return(mean)

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




khi2 <- function(facteur1, facteur2, K) {
  tableObs <- table(facteur1, facteur2)
  tableTheorique <- table(facteur1) %*% t(table(facteur2)) / K
  
  sumD <- sum((tableObs - tableTheorique)^2 / tableTheorique)
  
  return(sumD)
}