y = c(1,3,2.7,-1,3,4,6)
print(y)
print(mean(y))

#curve(dnorm(x, mean=0, sd=1), from=-4, to=4, lwd=2, col="red")
#curve(dnorm(x, mean=25, sd=8),from=0, to=50 ,col="red")
#print(pnorm(q = 20, mean = 25, sd = 8))
#print(1 - pnorm(q = 40, mean = 25, sd = 8))

#curve(dchisq(x,3), from=-1, to=10)
print(qchisq(0.5,3))
print(qchisq(0.8,3))
print(qchisq(0.2,3))

#a
#print(qchisq(0.1,3))

#b
#print(qchisq(0.9,3))

n = rnorm(1000)
print(n)

hist(n, freq=FALSE)
curve(dnorm(x), col="red", add=TRUE)