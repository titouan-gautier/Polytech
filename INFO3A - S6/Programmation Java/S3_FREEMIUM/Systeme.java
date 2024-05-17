import java.util.ArrayList;

public class Systeme {
    ArrayList<Utilisateur> listeUtilisateur;
    private static Integer id;

    Systeme() {
        this.listeUtilisateur = new ArrayList<Utilisateur>();
        id = 0;
    }

    public Utilisateur newUtilisateur(String nom, String prenom) {
        Utilisateur newUser = new Utilisateur(id,nom,prenom);
        id += 1;
        this.listeUtilisateur.add(newUser);
        return newUser;
    }
}
