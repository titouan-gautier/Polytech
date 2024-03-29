import java.io.File;
import java.io.ObjectOutputStream;
import java.io.FileOutputStream;
import java.io.Serializable ;

class TestEcriture {


   public static void main(String[] args){
      try {
         File fichier =  new File("/tmp/maville.ser") ;
         
         // ouverture d'un flux sur un fichier
         ObjectOutputStream oos =  new ObjectOutputStream(new FileOutputStream(fichier)) ;
         
         // création d'un objet à sérializer
         Ville v =  new Ville ("Paris") ;
         
         // sérialization de l'objet
         oos.writeObject(v) ;
      }
      catch (Exception e)
         { System.out.println (e) ; }
		
      
   }
 
}
