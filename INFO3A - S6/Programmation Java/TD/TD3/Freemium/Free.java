package Freemium;

public class Free extends Utilisateurs {

    int soundListen;

    Free(String nom, String prenom) {
        super(nom, prenom);
        this.soundListen = 0;
    }
}
