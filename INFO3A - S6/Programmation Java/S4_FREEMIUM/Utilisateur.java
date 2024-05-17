class Utilisateur {
   Email email ;
   String nom ;

   Utilisateur (Email email, String nom) {
      this.email = email ;
      this.nom = nom ;
   }

   void payer(int montant){
      System.out.println("Facturation : " + nom + " " + montant);
   }

   @Override
   public String toString() {
      return this.nom;
   }
}
