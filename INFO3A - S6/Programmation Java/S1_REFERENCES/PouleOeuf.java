class Position {
   int x ;
   int y ;
   Position (int x, int y){
      this.x = x ;
      this.y = y ;
   }
   @Override
   public String toString(){
      return x + "," + y ; // conversion implicite
   }
   void deplace(int x, int y){
      this.x = this.x + x ;
      this.y = this.y + y ;
   }
}

class Oeuf {
   Position p;
   Oeuf(Position p){
      this.p = p ;
   }
   void deplace(int x, int y){
      p.deplace(x,y);
   }
}

class Poule {
   Position p ;
   Poule (int x, int y) {
      this.p = new Position(x,y) ;
   }
   void showPosition(){
      System.out.println(p.toString());
   }
   Oeuf ponds(){
      return new Oeuf(this.p);
   }
}

class MesTests {
   public static void main(String[] args){
      Poule jacotte = new Poule (1,2);
      Oeuf neuf = jacotte.ponds();
      neuf.deplace (10,10);
      jacotte.showPosition();
   }
}
