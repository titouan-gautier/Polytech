import java.awt.event.KeyEvent;

public class Barre implements MovingObject{

    int x ;
    int y ;

    int vx ;
    int vy ;

    int marge ;

    Barre(int x, int y){
        this.x = x ;
        this.y = y ;
        this.vx = 2 ;
        this.vy = 2 ;
        this.marge = 15 ;
    }
    @Override
    public int getX() {
        return this.x;
    }

    @Override
    public int getY() {
        return this.y;
    }

    @Override
    public void deplace() {

    }
}
