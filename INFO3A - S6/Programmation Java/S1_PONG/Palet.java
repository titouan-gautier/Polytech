public class Palet implements MovingObject {

    float x ;
    float y ;

    float vx ;
    float vy ;

    int marge ;
    
   Palet(){
      x = 30 ;
      y = 30 ;
      vx = 2 ;
      vy = 2 ;
      marge = 15 ;
   }

    boolean sortie_x (float px){ return (px< (marge)) || (px>(320 - marge)) ; }
    boolean sortie_y (float py){ return (py< (marge)) || (py>(200 - marge)) ; }
    
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

    public float getX(){ return x ; }
    public float getY(){ return y ; }
    
}
