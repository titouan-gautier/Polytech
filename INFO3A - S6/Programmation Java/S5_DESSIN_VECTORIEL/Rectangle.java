import java.awt.Graphics2D ;


class Rectangle implements Figure {

    int x  ;
    int y  ;

    int largeur  ;
    int hauteur ;

    Rectangle(int _x, int _y, int l, int h){
	x = _x ;
	y = _y ;
	largeur = l;
	hauteur = h ;
    }

    @Override
    public void draw(Graphics2D g){
        g.drawRect(x,y,largeur,hauteur);
    }

}
