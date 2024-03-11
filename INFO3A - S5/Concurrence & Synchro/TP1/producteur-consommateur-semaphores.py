import threading
import tampon_lifo
tprint = print
# A décommenter pour synchroniser l'affichage tprint()
from tprint import tprint

#
#   Problème des "Producteurs Consommateurs"
#   Solution à l'aide de sémaphores
#


#
# Ressources critiques
#
# Tampon
tailleMaxTampon = 2
tampon = tampon_lifo.Tampon_lifo(tailleMaxTampon)

# Sémaphores
# A completer

#
# Threads Producteurs et Consommateurs
#

# Fonction principales des threads "producteurs" 
def producteur(nom)  :

    element=nom[1:]
 
    # A completer
    
    # code en E.M. sur mutex
    tprint("        {nom} depose \"{element}\" dans le tampon...".format(nom=nom, element=element))
    tampon_lifo.tampon_deposer(tampon, element)
    tprint("        {nom} a fini de deposee \"{element}\" dans le tampon...".format(nom=nom, element=element))
    #tprint("        {nom} tampon = {tampon}".format(nom=nom, tampon=tampon.lifo))
    # fin d'E.M.
    
    # A completer


# Fonction principales des threads "consommateurs" 
def consommateur(nom)  :

    # A completer

    # code en E.M. sur mutex
    tprint("        {nom} retire un element du tampon...".format(nom=nom))
    element = tampon_lifo.tampon_retirer(tampon)
    tprint("        {nom} a fini de retirer \"{element}\" du tampon...".format(nom=nom, element=element))
    #tprint("        {nom} tampon = {tampon}".format(nom=nom, tampon=tampon.lifo))
    # fin d'E.M.
    
    # A completer
    
    return element



# Exemple d'utilisation

def test_prod_cons_avec_semaphores():


    # Fonction principales de création et de démarrage des threads 
    nomsThreads  =  ["c1","p1", "p2", "p3", "p4", "c2", "c3", "c4 "]
    threads = []

    for nomT in nomsThreads  :
        if nomT[0]=='p' :
            thread_main = producteur
        else :
           thread_main = consommateur
        threads.append( threading.Thread(target=thread_main, name=nomT, args=(nomT,)))

    tprint("Debut du test")
    
    for t in threads :  
        t.start()
        tprint("{name} demarre".format(name=t.name))

    for t in threads :
        t.join()
        tprint("{name} est terminé".format(name=t.name))

    tprint("Fin du test")



if __name__ == "__main__" :
    test_prod_cons_avec_semaphores()



# Exemple de trace d'exécution (chronogramme)
# A COMPLETER
#
# on obtient
#
#:C1     :C2     :C3     ::P1     :P2     :P3     ::Mu        ::Sv        ::Sp        ::t   ::Comment
#:       :       :       ::       :       :       ::E  :F     ::E  :F     ::E  :F     ::    ::
#: -     : -     : -     :: -     : -     : -     ::1  :      ::0  :      ::2  :      ::    ::État initial
#:P(Sv)* :       :       ::       :       :       ::1  :      ::-1 :C1    ::2  :      ::    ::C1: P(Sv) : Sv.E<0 => C1 empilé sur Sv.F et endormi
#:W      :P(Sv)* :       ::P(Sp)  :       :       ::1  :      ::-2 :C1 C2 ::1  :      ::    ::C2: P(Sv) : Sv.E<0 => C2 empilé sur Sv.F et endormi // P1: P(Sp)
#:W      :W      :       ::P(Mu)  :P(Sp)  :       ::0  :      ::-2 :C1 C2 ::0  :      ::    ::P1: P(Mu)  // P2 : P(Sp)
 # completez ...
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#:       :       :       ::       :       :       ::   :      ::   :      ::   :      ::    ::
#
#
# Avec :
# Processus={C1,C2,C3,P1,P2,P3}
# TailleMax := 2
# Semaphores : Mu (Mutex), Sv (SnbOccup), Sp (SnbLibre)
# Pour Semapore S dans {Mu,Si,So} )
#    S.E : le compteur  du semaphore S
#    S.F : la liste d’attente FIFO des processus bloqués sur le sémaphore S
#
# Etat Processus:
#   - P(S)* : P(S) avec empilement et  attente
#   - W : attente passive (processus endormi/bloqué/en attente)
#   - *P(S) : fin d’attente sur P(S) et reprise
#   - P(S) = P(S) sans attente ( = P(S)*  + * P(S) )
#   - V(S) : V(S) avec dépilement éventuel
#   - D, R: opérations en section critique (Déposer, Retirer)
#   - F : fin