public class Main {
    public static void main(String[] args) throws Forbidden {
        Systeme newSysteme = new Systeme();

        Utilisateur moi = newSysteme.newUtilisateur("Titouan","Gautier");
        System.out.println(moi.getDetails());

        System.out.println();

        System.out.println(moi.getOffre().ecouter(1));
        System.out.println(moi.getOffre().ecouter(2));
        System.out.println(moi.getOffre().ecouter(3));

        System.out.println();

        System.out.println(moi.addFavoris(6));
        System.out.println(moi.addFavoris(4));

        System.out.println();

        System.out.println(moi.getDetails());

        System.out.println();

        System.out.println(moi.getOffre().changerAbonnement(moi));

        System.out.println(moi.getOffre().ecouter(1));
        System.out.println(moi.getOffre().ecouter(2));
        System.out.println(moi.getOffre().ecouter(3));
        System.out.println(moi.getOffre().ecouter(1));
        System.out.println(moi.getOffre().ecouter(2));
        System.out.println(moi.getOffre().ecouter(3));


    }
}
