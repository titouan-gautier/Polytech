class Automate {
    static boolean achat(Personne p, Film f){
        if (p.age < f.age_min) {
            notif_refus(p);
            return false ;
        }
        else {
            notif_acceptation(p);
            return true;
        }
    }

    static void notif_refus(Personne p){
        System.out.println ("Desole " + appellation(p) + ".") ;
    }

    static void notif_acceptation(Personne p){
        System.out.println ("Bienvenue " + appellation(p) + ".") ;
    }

    static String appellation(Personne p){
        if (p.age < 18){ return p.nom ; }
        else return "Monsieur" ;
    }
}
