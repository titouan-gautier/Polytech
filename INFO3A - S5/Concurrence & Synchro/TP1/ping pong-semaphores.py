import multiprocessing
import threading
import time
import random
tprint = print
# A décommenter pour synchroniser l'affichage tprint()
# from tprint import tprint



# liste des noms de threads à créer
NomsThreads = ["PONG","PING"]
# puis essayez avec:
# NomsThreads = ["PONG","PING","PING","PONG","PING","PONG","PONG","PING"]
threads = []

# boucle de répétition de chaque thread
NbCoups = 10

# ressource critique: 
chaine_ping_pong = ''


# Les semaphores
# A completer ...



def verifier_chaine_ping_pong(nom,i):
    global chaine_ping_pong
    chaine_ping_pong = chaine_ping_pong + nom + ' '
    tprint( '{nom} : \t (i={i}) chaine_ping_pong={chaine_ping_pong}'.format(nom=nom, i=i, chaine_ping_pong=chaine_ping_pong) )
    if chaine_ping_pong == "PONG " or chaine_ping_pong.endswith("PING PING ") or chaine_ping_pong.endswith("PONG PONG ") :
        tprint( '{nom} : \t ERREUR !'.format(nom=nom) )


# Threads de type Ping
def thread_ping(nom) :
    global chaine_ping_pong
    tprint( '{nom} : Debut du thread nom={nom}, pid={pid}, tid={tid}'.format(nom=nom, pid=multiprocessing.current_process().pid, tid=threading.get_ident()))

    for i in range(NbCoups):
        time.sleep(random.randint(0, 3))

    	# A completer ...

        # Debut de section critique
        tprint( '{nom} : Debut de section critique'.format(nom=nom))

        time.sleep(random.randint(0, 3))
        verifier_chaine_ping_pong(nom,i)

        tprint( '{nom} : Fin de section critique'.format(nom=nom))
        # fin de section critique
	
    	# A completer ...

    tprint( '{nom} : Fin du thread'.format(nom=nom))


# Threads de type Pong
def thread_pong(nom) :
    global chaine_ping_pong
    tprint( '{nom} : Debut du thread nom={nom}, pid={pid}, tid={tid}'.format(nom=nom, pid=multiprocessing.current_process().pid, tid=threading.get_ident()))

    for i in range(NbCoups):
        time.sleep(random.randint(0, 3))

    	# A completer ...

        # Debut de section critique
        tprint( '{nom} : Debut de section critique'.format(nom=nom))

        time.sleep(random.randint(0, 3))
        verifier_chaine_ping_pong(nom,i)

        tprint( '{nom} : Fin de section critique'.format(nom=nom))
        # fin de section critique
	
    	# A completer ...

    tprint( '{nom} : Fin du thread'.format(nom=nom))

  

  
# Création des Thread
thread_main = dict({"PING":thread_ping, "PONG":thread_pong})
for nom in NomsThreads:
    threads.append(threading.Thread(target=thread_main[nom], args=(nom,)))
# ou
# threads = [threading.Thread(target=thread_ping_pong, args=(nom,)) for nom in NomsThreads]

tprint('Debut du test avec {nom}'.format(nom=NomsThreads))

# Démarrage des threads
for t in threads:
    t.start()

# Attente de terminaison des threads
for t in threads:
    t.join()

tprint('Fin du test')


# Exemple de trace d'exécution (chronogramme)
# A COMPLETER
#
# on obtient
#
#:Pi     :Po     ::Si        ::So        ::Comment
#:       :       ::E  :F     ::E  :F     ::
#: -     : -     ::1  :      ::0  :      ::État initial
#:       :P(So)* ::1  :      ::-1 :Po    ::So.E <0 => Po empilé sur So.F et endormi
#:P(Si)  :W      ::0  :      ::-1 :Po    ::
#:PING   :W      ::0  :      ::-1 :Po    ::Pi: PING(1)
# completez ...
#:       :       ::   :      ::   :      ::
#:       :       ::   :      ::   :      ::
#
#
# Avec :
# Processus={Pi,Po}   (Pi=Ping, Po=Pong)
# Semaphore Si, So  (Si=Sping, So=Spong)
# Pour Semapore S dans {Si,So} )
#    S.E : le compteur  du semaphore S (pour S dans {Si,So} )
#    S.F : la liste d’attente FIFO des processus  bloqués sur le sémaphore S
#
# Etat Processus:
#   - P(S)* : P(S) avec empilement et  attente
#   - W : attente passive (processus endormi/bloqué/en attente)
#   - *P(S) : fin d’attente sur P(S) et reprise
#   - P(S) = P(S) sans attente ( = P(S)*  + * P(S) )
#   - V(S) : V(S) avec dépilement éventuel
#   - PING, PONG : opérations en section critique SC
#   - F : fin