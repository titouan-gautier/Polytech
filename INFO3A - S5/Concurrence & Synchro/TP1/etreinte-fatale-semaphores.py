import multiprocessing
import threading
import time
import random

tprint = print
# A décommenter pour synchroniser l'affichage tprint()
# from tprint import tprint

#
#   Probleme d'interblocage: l'étreinte fatale (Deadlock)
#

# Les semaphores
feuille = threading.Semaphore(1)
crayon = threading.Semaphore(1)
semaphore = threading.Semaphore(1)


# A completer...


# Threads T1
def thread_T1():
    nom = "T1"
    tprint('Debut du thread ' + nom)

    # A completer...
    semaphore.acquire()

    # prise d'un jeton dans le semaphore feuille
    tprint(nom + ' : Demande P(feuille})')
    feuille.acquire()
    tprint(nom + ' : Obtient P(feuille})')

    time.sleep(random.randint(0, 3))

    # prise d'un jeton dans le semaphore crayon
    tprint(nom + ' : Demande P(crayon)')
    crayon.acquire()
    tprint(nom + ' : Obtient P(crayon})')

    # A completer...

    # Debut de section critique
    tprint(nom + ' : feuille et crayon obtenus')
    tprint(nom + ' : dessine...')

    # restitution d'un jeton dans le semaphore crayon
    tprint(nom + ' : V(crayon)')
    crayon.release()

    # restitution d'un jeton dans le semaphore feuille
    tprint(nom + ' : V(feuille})')
    feuille.release()

    semaphore.release()


# Threads T2
def thread_T2():
    nom = "T2"
    tprint('Debut du thread ' + nom)

    # A completer...
    semaphore.acquire()

    # prise d'un jeton dans le semaphore feuille
    tprint(nom + ' : Demande P(crayon})')
    crayon.acquire()
    tprint(nom + ' : Obtient P(crayon})')

    time.sleep(random.randint(0, 3))

    # prise d'un jeton dans le semaphore crayon
    tprint(nom + ' : Demande P(feuille)')
    feuille.acquire()
    tprint(nom + ' : Obtient P(feuille})')

    # A completer...

    # Debut de section critique
    tprint(nom + ' : feuille et crayon obtenus')
    tprint(nom + ' : dessine...')

    # restitution d'un jeton dans le semaphore crayon
    tprint(nom + ' : v(feuille)')
    feuille.release()

    # restitution d'un jeton dans le semaphore feuille
    tprint(nom + ' : V(crayon})')
    crayon.release()

    semaphore.release()


# Création des Thread
t1 = threading.Thread(target=thread_T1)
t2 = threading.Thread(target=thread_T2)

tprint('Debut du test')

# Démarrage des threads
for t in [t1, t2]:
    t.start()

# Attente de terminaison des threads
for t in [t1, t2]:
    t.join()

tprint('Fin du test')
