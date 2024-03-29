class Utilisateur {
   EMail id ;
   String nom ;

   Utilisateur (EMail _id, String _nom){
      this.id = _id ;
      this.nom = _nom ;
   }

   void payer(int montant){
      System.out.println("Facturation : " + nom + " " + montant); 
   }
}
