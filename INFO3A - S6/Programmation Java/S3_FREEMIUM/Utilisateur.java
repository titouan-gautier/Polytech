import java.util.ArrayList;

public class Utilisateur {

    private final Integer id;
    private String nom;
    private String prenom;
    private ArrayList<String> favoris;
    private Abonnement offre;
    private CarteBancaire cb;

    public Utilisateur(int id, String nom, String prenom) {
        this.id = id;
        this.nom = nom;
        this.prenom = prenom;
        this.favoris = new ArrayList<String>();
        this.offre = new Freemium();
        this.cb = null;
    }

    public Integer getId() {
        return id;
    }

    public String getNom() {
        return nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public ArrayList<String> getFavoris() {
        return favoris;
    }

    public Abonnement getOffre() {
        return offre;
    }

    public CarteBancaire getCb() {
        return cb;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public void setFavoris(ArrayList<String> favoris) {
        this.favoris = favoris;
    }

    public void setOffre(Abonnement offre) {
        this.offre = offre;
    }

    public void setCb(CarteBancaire cb) {
        this.cb = cb;
    }

    public String addFavoris(Integer morecau) throws Forbidden {
        try {
            BanqueMusique.Sound s = BanqueMusique.getFile(morecau);
        } catch (Exception e) {
            return "Morceau inexistant";
        }
        this.favoris.add(morecau.toString());
        return "Morceau %s ajouté aux favoris !".formatted(morecau);
    }

    @Override
    public String toString() {
        return "%s %s".formatted(this.prenom, this.nom);
    }

    public String getDetails() {
        return ("Nom: %s \n" +
                "Prenom: %s \n" +
                "ID: %d \n" +
                "Offre: %s \n" +
                "Favoris: %s").formatted(this.nom,
                this.prenom,
                this.id,
                this.offre.toString(),
                this.favoris.toString());
    }

}
