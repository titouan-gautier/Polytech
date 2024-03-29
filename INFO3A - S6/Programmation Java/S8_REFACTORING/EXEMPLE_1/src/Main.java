public class Main {
   public static void main(String[] args){
       A o = new B (1, new B(2, new B(3,new C())));
       System.out.println(o.m()) ;
   }
}
