package Freemium;

public class Utilisateurs {
    private static int id = 0;

    String nom;
    String prenom;
    int idUtilisateur;
    Sound[] favoris;

    Utilisateurs(String nom, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
        this.idUtilisateur = id;
        this.favoris = new Sound[10];

        id += 1;
    }
}

