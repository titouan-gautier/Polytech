import math
import matplotlib.pyplot as plt
import numpy as np


va = [
    6041,7796,4276,3286,7315,4108,6176,4260,9583,295,
    5995,4376,4488,2974,8208,2190,589,3261,6206,4705,
    3490,7858,5366,3831,1527,1463,3874,414,4398,8682,
    2177]

'''Centralité'''

def mode(va) :
    return max(va)

def moy_ordinaire(va) :
    n = len(va)
    somme = sum(va)

    return somme/n

def medianne(va): 
    n = len(va) // 2
    va_sort = va.copy()

    va_sort.sort()

    return va_sort[n]

'''Dispersion'''

def ecart_absolu_moyen(va) :
    moy = moy_ordinaire(va)
    n = len(va)

    somme = sum([abs(i - moy) for i in va])

    return 1/n * somme

def variance(va) :
    moy = moy_ordinaire(va)
    n = len(va)

    somme = sum([pow(i - moy,2) for i in va])

    return 1/n * somme


def ecart_type(va) :
    return math.sqrt(variance(va))

def hist(va) :

    days = np.arange(1,32)

    plt.bar(days,va)
    plt.show()

hist(va)

vb = [6, 8, 8, 8, 10, 11, 12, 15, 19, 19, 24]
