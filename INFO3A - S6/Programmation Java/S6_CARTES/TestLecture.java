import java.io.File;
import java.io.ObjectInputStream;
import java.io.FileInputStream;


class TestLecture {
   
   public static void main(String[] args){
      try {
         File fichier =  new File("/tmp/maville.ser") ;
         
         // ouverture d'un flux sur un fichier
         ObjectInputStream ois =  new ObjectInputStream(new FileInputStream(fichier)) ;
         
         // désérialization de l'objet
         Ville v = (Ville)ois.readObject() ;
         
         // Pour vérification
         System.out.println(v) ;
         
         
      }
      catch (Exception e)
         { System.out.println (e) ; }
		
   }
   
   

}
