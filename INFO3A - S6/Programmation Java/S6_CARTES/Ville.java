import java.io.Serializable ;

class Ville implements Serializable {
   
   static int compteur = 1 ;
   
   int index ;
   String name ;
   
   Ville(String _name){
      name = _name ;
      index = compteur ;
      compteur ++ ;
   }
   
   @Override
   public String toString(){ return name + "(" + index + ")" ; }
   
}
