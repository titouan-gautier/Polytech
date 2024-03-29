public class Palet implements MovingObject {

    int x ;
    int y ;

    int vx ;
    int vy ;

    int marge ;
    
   Palet(){
      x = 30 ;
      y = 30 ;
      vx = 2 ;
      vy = 2 ;
      marge = 15 ;
   }

    boolean sortie_x (int px){ return (px< (marge)) || (px>(320 - marge)) ; }
    boolean sortie_y (int py){ return (py< (marge)) || (py>(200 - marge)) ; }
    
    public void deplace(){
	if ( sortie_x (x + vx) ) {
	    vx = (-1) * vx ;
	}
	else {
	    x = x + vx ;
	}
	
	if ( sortie_y (y + vy) ) {
	    vy = (-1) * vy ;
	}
	else {
	    y = y + vy ;
	}
    }

    public int getX(){ return x ; }
    public int getY(){ return y ; }
    
}
