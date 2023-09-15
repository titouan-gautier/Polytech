import tp0.util as util
import tp0.arithmetique as art

n: int = util.saisir_entier()
if not art.est_pair(n):
    n +=1
print(f"Somme de 0 à {n} = {art.somme(n)}")