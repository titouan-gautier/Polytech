import java.io.Serializable ;

public class Ville implements Serializable {
   
   static int compteur = 1 ;
   
   int index ;
   int distance ;
   String name ;
   
   Ville(String _name){
      name = _name ;
      distance = 0;
      index = compteur ;
      compteur ++ ;
   }
   
   @Override
   public String toString(){ return name + "(" + index + ")" ; }
   
}
