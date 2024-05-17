public class Premium extends Abonnement{
    private Integer prix;

    Premium() {
        prix = 15;
    }

    public void setPrix(Integer prix) {
        this.prix = prix;
    }

    @Override
    public BanqueMusique.Sound ecouter(int morceau) throws Forbidden {
        return BanqueMusique.getFile(morceau);
    }

    @Override
    public String changerAbonnement(Utilisateur u) {
        u.setOffre(new Freemium());
        return "Vous êtes passé à l'abonnement Freemium";
    }

    public void payer(CarteBancaire cb) {
        cb.paye(prix);
    }

    @Override
    public String toString() {
        return "Premium";
    }
}
