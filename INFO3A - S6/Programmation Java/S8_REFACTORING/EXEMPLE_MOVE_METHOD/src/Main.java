public class Main {

    static int somme(List s){
        try {
            return (s.head() + somme(s.tail()));
        }
        catch (Exception e) { return 0 ;}
    }

   public static void main(String[] args){
       List o = new Cons(1, new Cons(2, new Cons(3,new Empty())));

       System.out.println(somme(o)) ;
   }
}
