import multiprocessing
import threading
import time
import random
tprint = print
# A décommenter pour synchroniser l'affichage tprint()
from tprint import tprint

#
# Implémentation d'une alternance "ping pong" avec les moniteurs python (Lock et Condition)
#

def verifier_chaine_ping_pong(moniteur,nom,i):
    moniteur.chaine_ping_pong = moniteur.chaine_ping_pong + nom.upper() + ' '
    tprint( '{nom} : \t (i={i}) chaine_ping_pong={chaine_ping_pong}'.format(nom=nom.upper(), i=i, chaine_ping_pong=moniteur.chaine_ping_pong) )
    if moniteur.chaine_ping_pong == "PONG " or moniteur.chaine_ping_pong.endswith("PING PING ") or moniteur.chaine_ping_pong.endswith("PONG PONG ") :
        tprint( '{nom} : \t ERREUR !'.format(nom=nom.upper()) )



#
# Définition du Moniteur Ping Pong
#

# definition des donnees du moniteur (variables d'etat, conditions, mutex) :
class Moniteur_PingPong():
    def __init__(self):
        # les ressources critiques (ou variables d'etat")
        self.chaine_ping_pong=""
        self.tour="ping"
        # a compléter: mutex, conditions

# point d'entrée du moniteur :
def moniteur_ping(moniteur, i):
    nom = "ping"
    tprint("{nom} débute".format(nom=nom))
    # a compléter: EM
    
    # a compléter : attendre (=wait) jusqu'à son tour (si nom != moniteur.tour ....)

    time.sleep(random.randint(0, 3))
    verifier_chaine_ping_pong(moniteur,nom.upper(),i)

    # a compléter : changer le  tour 
        
    # a compléter : réveiller (=signal) le processus dont s'est le tour si endormi 
    
    tprint("{nom} termine".format(nom=nom))
    # a compléter: EM


# point d'entrée du moniteur :
def moniteur_pong(moniteur, i):
    nom = "pong"
    tprint("{nom} débute".format(nom=nom))
    # a compléter: EM
    
    # a compléter : attendre (=wait) jusqu'à son tour (si nom != moniteur.tour ....)

    time.sleep(random.randint(0, 3))
    verifier_chaine_ping_pong(moniteur,nom.upper(),i)

    # a compléter : changer le  tour 
        
    # a compléter : réveiller (=signal) le processus dont s'est le tour si endormi 
    
    tprint("{nom} termine".format(nom=nom))
    # a compléter: EM


# fin de definition du moniteur





#
# test alternance Ping Pong
#
def alternance():
    # liste des noms de threads à créer
    NomsThreads = ["PONG","PING"]
    # puis essayez avec:
    # NomsThreads = ["PONG","PING","PING","PONG","PING","PONG","PONG","PING"]
    threads = []

    # boucle de répétition de chaque thread
    NbCoups = 10

    # ressources critiques dans le moniteur
    moniteur = Moniteur_PingPong()
    



    # Threads de type Ping
    def thread_ping() :
        global chaine_ping_pong
        nom="PING"
        tprint( '{nom} : Debut du thread nom={nom}'.format(nom=nom))

        for i in range(NbCoups):
            moniteur_ping(moniteur, i)

        tprint( '{nom} : Fin du thread'.format(nom=nom))


    # Threads de type Pong
    def thread_pong() :
        global chaine_ping_pong
        nom="PONG"
        tprint( '{nom} : Debut du thread nom={nom}'.format(nom=nom))

        for i in range(NbCoups):
            moniteur_pong(moniteur, i)

        tprint( '{nom} : Fin du thread'.format(nom=nom))


      
    # Création des Thread
    thread_main = dict(PING=thread_ping, PONG=thread_pong)
    for nom in NomsThreads:
        threads.append(threading.Thread(target=thread_main[nom]))
    # ou
    # threads = [threading.Thread(target=thread_main[nom]) for nom in NomsThreads]

    tprint('Debut du test avec {nom}'.format(nom=NomsThreads))

    # Démarrage des threads
    for t in threads:
        t.start()

    # Attente de terminaison des threads
    for t in threads:
        t.join()

    tprint('Fin du test')


if __name__ == "__main__" :
    alternance()

# Test 2 : Exemple de trace d'éxécution de l'alternance (chronogramme)

# on obtient
#

#: Processus        :::       Moniteur Ping Pong                     ::: Comment
#: Pi     :: Po     ::: Moniteur Si :: Mutex    :: Conditions et Var ::: 
#:PE :Pi  ::PE :Po  :::MPE:MP:MF    ::Mu:MuF    ::Cpi    :Cpo    :T  :::
#:   :    ::   :    :::   :  :      ::1 :       ::       :       :pi :::  Etat initial
#:   :    ::Mpo:L*  :::   :  :      ::0 :       ::       :       :pi ::: Po L* : début Mpo pong, lock(Mu)>
#:   :    ::Mpo:*L  :::Mpo:Po:      ::0 :       ::       :       :pi ::: Po *L : lock(Mu)<
#:Mpi:L*  ::Mpo:    :::Mpo:Po:      ::-1:Pi     ::       :       :pi ::: Pi L* : début Mpi ping, lock(Mu)>
#:Mpi:    ::Mpo:    :::Mpo:Po:Pi    ::-1:Pi     ::       :       :pi ::: Pi : attend sur Mu
#:Mpi:    ::Mpo:WoU :::Mpo:Po:Pi    ::-1:Pi     ::       :Po     :pi ::: Po WoU : tour==ping => wait(Cpo) : Po attend sur Cpo + U: unlock(Mu)
#:Mpi:*L  ::Mpo:    :::Mpi:Pi:      ::0 :       ::       :Po     :pi ::: Pi reprise moniteur
#:Mpi:PING::Mpo:    :::Mpi:Pi:      ::0 :       ::       :Po     :pi ::: Pi PING : tour==ping => PING
#:Mpi:T   ::Mpo:    :::Mpi:Pi:      ::0 :       ::       :Po     :po ::: Pi T : tour:=pong 
#:Mpi:So  ::Mpo:Wo* :::Mpi:Pi:      ::0 :       ::       :Po     :po ::: Pi So : signal(Cpo) -> reveil Po dans Cpo
#:Mpi:    ::Mpo:L*  :::Mpi:Pi:      ::-1:Po     ::       :       :po ::: Po L* : lock(Mu)>
#:Mpi:    ::Mpo:    :::Mpi:Pi:Po    ::-1:Po     ::       :       :po ::: Po : attend sur Mu
#:Mpi:U   ::Mpo:    :::Mpi:Pi:Po    ::0 :       ::       :       :po ::: Pi U : fin Mpi unlock(Mu) -> reveil Po dans MuF 
#:   :    ::Mpo:*L  :::Mpo:Po:      ::0 :       ::       :       :po ::: Po *L : lock(Mu)< -> reprise Mpo moniteur 

# A COMPLETER .....

#
# Avec :
# Processus={Pi,Po}, Pi (Ping) et Po (Pong)
# PE: nom du point d'entrée (Mpi ou Mpo)
    
# Mpi, Mpo : points d'entrée du moniteur (pour moniteur_ping ou moniteur_pong) 
# MP: Processus en cours dans le moniteur (théorique)
# MPE: nom du point d'entrée en cours dans le moniteur (théorique) (Mpi ou Mpo)
# MF: Liste d'attente en entrée du moniteur (théorique) ~ MuF
# Mu: valeur du Mutex d'accès au moniteur(accès réel)
# MuF: liste d'attente du Mutex d'accès au moniteur(accès réel)
# T: tour (pi ou po, pour ping ou pong)
# Cpi : condition attente tour ping
# Cpo : condition attente tour pong
#
# Etat Processus:
#   - L* : demande mutex P(Mu) (lock(Mu)) avec attente éventuelle (processus empilé dans MuF et endormi)
#   - *L  : obtention mutex Mu (après reveil eventuel)
#   - L = L* + *L 
#   - U  : libération mutex V(Mu) (unlock(Mu) avec reveil eventuel
#   - So, Wo,  Wo*, *Wo : actions sur condition Cpo
#     - So : signal(Cpo), dépiler et reveiller
#     - Wo : wait(Cpo), empiler et endormir
#     - Wo* : signal(Cpo) effectué par un autre processus, => attente reprise moniteur
#     - *Wo (ou *L) : acquisition du mutex et reprise dans moniteur
#   - Si, Wi,  Wi*, *Wi : idem sur condition Cpi
#   - T : modification de la RC tour
#   - PONG, PING (Ping, Pong)
#   - F : fin
