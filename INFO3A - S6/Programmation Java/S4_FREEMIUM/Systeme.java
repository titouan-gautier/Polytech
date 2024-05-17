import jdk.jshell.execution.Util;

import java.util.* ;

class Systeme {
   Hashtable<Email,Utilisateur> lesUtilisateurs;

   Systeme() {
      lesUtilisateurs = new Hashtable<Email,Utilisateur>();
   }

   void payerTous(int montant) {
      Enumeration<Email> e = lesUtilisateurs.keys();

      while (e.hasMoreElements()) {
         lesUtilisateurs.get(e.nextElement()).payer(montant);
      }
   }

   Utilisateur createUser(String email,String nom) {
      String[] splitEmail = email.split("@");
      String[] splitDomain = splitEmail[1].split("\\.");

      String name = splitEmail[0];
      String domain = splitDomain[0];
      String domainName = splitDomain[1];

      Email newEmail = new Email(name,domain,domainName);
      Utilisateur user = new Utilisateur(newEmail,nom);
      this.lesUtilisateurs.put(newEmail,user);

      return user;
   }

   Utilisateur get(Email a){
      return this.lesUtilisateurs.get(a);
   }

}
