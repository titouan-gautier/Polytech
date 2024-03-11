import multiprocessing
import threading
import time
import random
tprint = print
# A decommenter pour synchroniser l'affichage tprint()
#from tprint import tprint

#
# Implémentation d'un sémaphore de comptage à partir des moniteurs python (Lock et Condition)
#


#
# Définition du Moniteur sémaphore
#

class Semaphore_moniteur():
    def __init__(self,counter=0):
        # Variables d'état
        # A compléter: compteur (ressource critique)
        # A compléter: condition, mutex
        pass
    
# Les Points d'entrée :

def P(semaphore):
    # A compléter : EM
    # A compléter: décrémenter le compteur
    # A compléter: endormir si compteur < 0
    # A compléter : EM
    pass

def V(semaphore):
    # A compléter : EM
    # A compléter: incrémenter le compteur
    # A compléter: reveiller processus endormi si compteur <= 0
    # A compléter : EM
    pass



# fin de definition du moniteur





#
# test 1 avec exlusion mutuelle par sémaphore
#
def testEM():


    # boucle de répétition de chaque thread
    NbCoups = 10

    # ressource critique:
    global RC
    RC = 0

    # Les semaphores
    semaphore = Semaphore_moniteur(1)



    # Threads P1
    def thread_P1(nom) :
        global RC
        tprint( '{nom} : Debut du thread nom={nom}'.format(nom=nom, pid=multiprocessing.current_process().pid, tid=threading.get_ident()))

        for i in range(NbCoups):
            time.sleep(random.randint(0, 3))

            # prise d'un jeton dans le semaphore
            tprint( '{nom} : Demande P(semaphore)'.format(nom=nom) )
            P(semaphore)

            # Debut de section critique
            tprint( '{nom} : Debut de section critique'.format(nom=nom))

            a = RC
            time.sleep(random.randint(0, 3))
            RC = a + 1
            tprint( '{nom} : \t (i={i}) RC={RC}'.format(nom=nom, i=i, RC=RC) )

            tprint( '{nom} : Fin de section critique'.format(nom=nom))
            # fin de section critique

            # liberation d'un jeton dans le semaphore pong (resp. ping)
            V(semaphore)
            tprint( '{nom} : V(semaphore)'.format(nom=nom) )
                
        tprint( '{nom} : Fin du thread'.format(nom=nom))

    # Threads P2
    def thread_P2(nom) :
        global RC
        tprint( '{nom} : Debut du thread nom={nom}'.format(nom=nom, pid=multiprocessing.current_process().pid, tid=threading.get_ident()))

        for i in range(NbCoups):
            time.sleep(random.randint(0, 3))

            # prise d'un jeton dans le semaphore
            tprint( '{nom} : Demande P(semaphore)'.format(nom=nom) )
            P(semaphore)

            # Debut de section critique
            tprint( '{nom} : Debut de section critique'.format(nom=nom))

            b = RC
            time.sleep(random.randint(0, 3))
            RC = b + 2
            tprint( '{nom} : \t (i={i}) RC={RC}'.format(nom=nom, i=i, RC=RC) )

            tprint( '{nom} : Fin de section critique'.format(nom=nom))
            # fin de section critique

            # liberation d'un jeton dans le semaphore pong (resp. ping)
            V(semaphore)
            tprint( '{nom} : V(semaphore)'.format(nom=nom) )
                
        tprint( '{nom} : Fin du thread'.format(nom=nom))



      
    # Création des Thread
    P1 = threading.Thread(target=thread_P1, args=("P1",))
    P2 = threading.Thread(target=thread_P2, args=("P2",))

    tprint('Debut du test')

    # Démarrage des threads
    for t in [P1, P2]:
        t.start()

    # Attente de terminaison des threads
    for t in [P1,P2]:
        t.join()

    RCcorrect = 3*NbCoups 
    if RC != RCcorrect :
        tprint( 'ERREUR RC={RC} != {RCcorrect} !'.format(RC=RC,RCcorrect=RCcorrect))

    
    tprint('Fin du test')



# Test 1 : Exemple de trace d'éxécution (chronogramme)

#
# on obtient
#
#: Processus  :: Moniteur   :: Mutex   :: Variables :Condition:
#:PE:P1::PE:P2::MP:MPE:MF   ::Mu:MuF   ::RC::E  : F   :: Comment
#:  :  ::  :  ::  :   :     ::1 :      ::0 ::1  :     ::
#:P :L*::  :  ::  :   :     ::0 :      ::0 ::1  :     ::P1 debut P(S), lock(Mu)>
#:P :*L::  :  ::P1:P  :     ::0 :      ::0 ::1  :     ::P1 lock(Mu)<
#:P :  ::P :L*::P1:P  :     ::-1:P2    ::0 ::1  :     ::P2 debut P(S), lock(Mu)>
#:P :  ::P :L ::P1:P  :P2   ::-1:P2    ::0 ::1  :     ::P2 attend sur Mu
#:P :E-::P :L ::P1:P  :P2   ::-1:P2    ::0 ::0  :     ::P1 E--
#:P :U ::P :L*::P1:P  :P2   ::0 :      ::0 ::0  :     ::P1 unlock(Mu)->reveil P2
#:P :  ::P :  ::  :   :P2   ::0 :      ::0 ::0  :     ::P1 fin P(S)
#:  :  ::P :*L::P2:P  :     ::0 :      ::0 ::0  :     ::P2 lock(Mu)<, P2 reprend
#:  :  ::P :E-::P2:P  :     ::0 :      ::0 ::-1 :     ::P2 E--
#:  :RC::P :  ::P2:P  :     ::0 :      ::1 ::-1 :     ::P1 RC:=RC+1
#:V :L*::P :  ::P2:P  :     ::-1:P1    ::1 ::-1 :     ::P1 debut V(S), lock(Mu)
# A COMPLETER ...

#
# Avec :
# Processus={P1,P2}
# PE: nom du point d'entrée (P ou V)
# Point entrée moniteur (théorique) :
#  - MP: Processus en cours dans le moniteur
#  - MPE: nom du point d'entrée en cours dans le moniteur (P ou V)
#  - MF: Liste d'attente en entrée du moniteur
# Mutex pseudo-moniteur (accès réel) :
#  - Mu: valeur du Mutex d'accès au moniteur
#  - MuF: liste d'attente du Mutex d'accès au moniteur
# Variables d’état (VE) et conditions :
#  - F: condition/liste attente "semaphore",
#  - E: compteur du "semaphore",
# RC: la ressource critique 

#
# Etat Processus:
#   - L* : actif (et reveil eventuel) après demande mutex Mu et attente (lock(Mu)>)
#   - *L : actif et reprise effective après obtention mutex Mu (lock(Mu)<)
#   - L : inactif/endormi en attente sur mutex Mu
#   - S : signal(F)
#   - W : wait(F), empiler et endormir
#   - W* : signal(F) effectué par un autre processus, depiler
#   - *W (ou *L) : acquisition du mutex et reprise
#   - RC : operation sur RC
#   - E+ : incrémentation du compteur E
#   - E- : décrémentation du compteur E
#   - F : fin



#
# test 2 avec alternance Ping Pong avec sémaphores
#
def testAlternance():
    # liste des noms de threads à créer
    NomsThreads = ["PONG","PING"]
    # puis essayez avec:
    # NomsThreads = ["PONG","PING","PING","PONG","PING","PONG","PONG","PING"]
    threads = []

    # boucle de répétition de chaque thread
    NbCoups = 10

    # ressource critique:
    global chaine_ping_pong
    chaine_ping_pong = ''

    # Les semaphores
    semaphore_ping = Semaphore_moniteur(1)
    semaphore_pong = Semaphore_moniteur(0)



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
    
    	# prise d'un jeton dans le semaphore ping (resp. pong)
            tprint( '{nom} : Demande P(semaphore_{noml})'.format(nom=nom, noml=nom.lower()) )
            P(semaphore_ping)
    
            # Debut de section critique
            tprint( '{nom} : Debut de section critique'.format(nom=nom))
    
            time.sleep(random.randint(0, 3))
            verifier_chaine_ping_pong(nom,i)
    
            tprint( '{nom} : Fin de section critique'.format(nom=nom))
    	# fin de section critique
    
    	# liberation d'un jeton dans le semaphore pong (resp. ping)
            V(semaphore_pong)
            tprint( '{nom} : V(semaphore_{noml})'.format(nom=nom, noml=nom.lower()) )
                
        tprint( '{nom} : Fin du thread'.format(nom=nom))
    
    
    # Threads de type Pong
    def thread_pong(nom) :
        global chaine_ping_pong
        tprint( '{nom} : Debut du thread nom={nom}, pid={pid}, tid={tid}'.format(nom=nom, pid=multiprocessing.current_process().pid, tid=threading.get_ident()))
    
        for i in range(NbCoups):
            time.sleep(random.randint(0, 3))
    
    	# prise d'un jeton dans le semaphore ping (resp. pong)
            tprint( '{nom} : Demande P(semaphore_{noml})'.format(nom=nom, noml=nom.lower()) )
            P(semaphore_pong)
    
            # Debut de section critique
            tprint( '{nom} : Debut de section critique'.format(nom=nom))
    
            time.sleep(random.randint(0, 3))
            verifier_chaine_ping_pong(nom,i)
    
            tprint( '{nom} : Fin de section critique'.format(nom=nom))
    	# fin de section critique
    
    	# liberation d'un jeton dans le semaphore pong (resp. ping)
            V(semaphore_ping)
            tprint( '{nom} : V(semaphore_{noml})'.format(nom=nom, noml=nom.lower()) )
                
        tprint( '{nom} : Fin du thread'.format(nom=nom))



      
    # Création des Thread
    thread_main = dict(PING=thread_ping, PONG=thread_pong)
    for nom in NomsThreads:
        threads.append(threading.Thread(target=thread_main[nom], args=(nom,)))
    # ou
    # threads = [threading.Thread(target=thread_main[nom], args=(nom,)) for nom in NomsThreads]

    tprint('Debut du test avec {nom}'.format(nom=NomsThreads))

    # Démarrage des threads
    for t in threads:
        t.start()

    # Attente de terminaison des threads
    for t in threads:
        t.join()

    tprint('Fin du test')


# Test 2 : Exemple de trace d'éxécution de l'alternance (chronogramme)

# A COMPLETER.....
# on obtient
#
#
#: Processus  ::: Moniteur semaphore ping Si        ::: Moniteur semaphore pong So        ::: Comment
#: Pi  :: Po  ::: Moniteur Si :: Mutex Si :: Var Si ::: Moniteur So :: Mutex So :: Var So ::: Comment
#:PE :Pi::PE :Po:::MP:MPE:MF    ::Mu:MuF    ::C :F   :::MP:MPE:MF    ::Mu:MuF    ::C :F   ::: Comment
#:   :  ::   :  :::  :   :      ::1 :       ::1 :     :::  :   :      ::1 :       ::0 :     ::: Etat initial
#:   :  ::PSo:L*:::  :   :      ::1 :       ::1 :     :::  :   :      ::0 :       ::0 :     ::: Po L* : début P(So) pong, lock(So.Mu)>
#:   :  ::PSo:*L:::  :   :      ::1 :       ::1 :     :::Po:P  :      ::0 :       ::0 :     ::: Po *L : lock(So.Mu)<
#:PSi:L*::PSo:  :::  :   :      ::0 :       ::1 :     :::Po:P  :      ::0 :       ::0 :     ::: Pi L* : début P(Si) ping, lock(Si.Mu)>
#:PSi:*L::PSo:  :::Pi:P  :      ::0 :       ::1 :     :::Po:P  :      ::0 :       ::0 :     ::: Pi *L : lock(Si.Mu)<
#:PSi:  ::PSo:C-:::Pi:P  :      ::0 :       ::1 :     :::Po:P  :      ::0 :       ::-1:     ::: Po C- : P(So) -> So.C--  (So.C==-1)
#:PSi:  ::PSo:WU:::Pi:P  :      ::0 :       ::1 :     :::Po:P  :      ::0 :       ::-1:Po   ::: Po WU : So.C<=0 => W : Po attend sur So.F wait(So.F) + U: unlock(So.Mu)
#:PSi:  ::PSo:  :::Pi:P  :      ::0 :       ::1 :     :::  :   :      ::1 :       ::-1:Po   ::: Po en attente sur P(So)  (unlock(So.Mu) -> pas de processus en attente à reveiller)
#:PSi:C-::PSo:  :::Pi:P  :      ::0 :       ::0 :     :::  :   :      ::1 :       ::-1:Po   ::: Pi C- : P(Si) -> Si.C--  (Si.C==0)
#:PSi:U ::PSo:  :::Pi:P  :      ::1 :       ::0 :     :::  :   :      ::1 :       ::-1:Po   ::: Pi U : Si.C>=0 donc poursuite + unlock(Si.Mu)

# A COMPLETER .....

#
# Avec :
# Processus={Pi,Po}, Pi (Ping) et Po (Pong)
# PE: nom du point d'entrée (PSi, VSi ou PSo, VSo)
# MP: Processus en cours dans le moniteur (théorique)
# Si: moniteur semaphore Si (semaphore ping)
# PSi, VSi : points d'entrée de Si
# So moniteur semaphore Si (semaphore pong)
# PSo, VSo : points d'entrée de So
# MPE: nom du point d'entrée en cours dans le moniteur (théorique) (PSi, VSi ou PSo, VSo)
# MF: Liste d'attente en entrée du moniteur (théorique) ~ MuF
# Mu: valeur du Mutex d'accès au moniteur(accès réel)
# MuF: liste d'attente du Mutex d'accès au moniteur(accès réel)
# F: condition/liste attente "semaphore",
# C: compteur du "semaphore",


#
# Etat Processus:
#   - L* : demande mutex P(Mu) (lock(Mu)) avec attente éventuelle
#   - L  : attente passive mutex Mu (processus empilé dans MuF et endormi)
#   - U  : libération mutex V(Mu) (unlock(Mu)
#   - S : signal(F)
#   - W : wait(F), empiler et endormir
#   - W* : signal(F) effectué par un autre processus, => depiler
#   - *W (ou *L) : acquisition du mutex et reprise
#   - C+ : incrémentation du compteur C
#   - C- : décrémentation du compteur C
#   - PO, PI (Ping, Pong)
#   - F : fin





if __name__ == "__main__" :
    testEM()
    testAlternance()
