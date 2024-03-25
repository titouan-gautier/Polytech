NiveauFondant = cut(Fondant, breaks=quantile(Fondant, probs = seq(0, 1, 0.25), names=FALSE), labels=c("faiblement fondant","légèrement fondant","plutot fondant","très fondant"), include.lowest=TRUE)

NiveauAmertume = cut(Amertume, breaks=quantile(Amertume, probs = seq(0, 1, 0.25), names=FALSE), labels=c("faiblement amer","légèrement amer","plutot amer","très amer"), include.lowest=TRUE)
