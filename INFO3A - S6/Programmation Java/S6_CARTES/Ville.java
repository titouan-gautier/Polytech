import java.io.Serializable ;

public class Ville implements Serializable, Cloneable {
   
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

    @Override
    public Ville clone() throws CloneNotSupportedException {
        return (Ville) super.clone();
    }
}
