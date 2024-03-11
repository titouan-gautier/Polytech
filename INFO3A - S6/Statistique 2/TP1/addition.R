addition <- function(x,y) {
    z <- x+y
    return(z)
}

moyenne <- function(v) {
    
    sum = 0

    for (i in v) {

        sum = sum + i

    }

    mean = sum / length(v)

    return(mean)

}