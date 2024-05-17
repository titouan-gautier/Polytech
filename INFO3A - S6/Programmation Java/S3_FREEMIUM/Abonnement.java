abstract public class Abonnement {

    abstract public BanqueMusique.Sound ecouter(int morceau) throws Forbidden;
    abstract public String changerAbonnement(Utilisateur u);

}
