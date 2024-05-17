public class Main {
    public static void main(String[] args) {
        Systeme s = new Systeme();
        Utilisateur un = s.createUser("titgautier@gmail.com","Titouan GAUTIER");
        Utilisateur deux = s.createUser("eliasboussaoui@gmail.com","Elias Boussaoui");

        Email email1 = new Email("titgautier","gmail","com");
        Email email2 = new Email("eliasboussaoui","gmail","com");

        System.out.println(s.get(email2));
    }
}
