import java.util.* ;

class Systeme {
   List <Utilisateur> lesUtilisateurs ;

   Systeme(){
      lesUtilisateurs = new LinkedList<>();
   }

   void payerTous(int montant){
      for (Utilisateur u : lesUtilisateurs){
         u.payer(montant);
      }
   }

   Utilisateur get(EMail a){
      throw new UnsupportedOperationException(); // FIXME
   }
}
