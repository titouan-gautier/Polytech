import java.util.Scanner;

public class Freemium extends Abonnement {

    private int nb_ecoute;
    private int ecoute_max;

    Freemium() {
        this.nb_ecoute = 0;
        this.ecoute_max = 3;
    }

    public void setEcoute_max(int ecoute_max) {
        this.ecoute_max = ecoute_max;
    }

    @Override
    public BanqueMusique.Sound ecouter(int morceau) throws Forbidden {

        if (this.nb_ecoute < this.ecoute_max) {
            this.nb_ecoute += 1;
            return BanqueMusique.getFile(morceau);
        }

        throw new Forbidden("Nombre d'écoute max dépassé");
    }

    @Override
    public String changerAbonnement(Utilisateur u) {

        if (u.getCb() == null) {
            int num_carte;
            int date;
            int pictogramme;

            Scanner scanner = new Scanner(System.in);

            System.out.print("Veuillez entrer votre numéro de carte : ");
            num_carte = Integer.parseInt(scanner.nextLine());

            System.out.print("Veuillez entrer la date d'expiration de la carte : ");
            date = Integer.parseInt(scanner.nextLine());

            System.out.print("Veuillez entrer le pictograme de la carte : ");
            pictogramme = Integer.parseInt(scanner.nextLine());

            u.setCb(new CarteBancaire(num_carte, date, pictogramme));

        }

        Premium p = new Premium();
        p.payer(u.getCb());
        u.setOffre(p);

        return "Vous êtes passé à l'abonnement Premium";

    }

    @Override
    public String toString() {
        return "Freemium";
    }
}
