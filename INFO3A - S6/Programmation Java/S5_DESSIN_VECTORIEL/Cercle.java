import java.awt.*;

public class Cercle extends Rectangle implements Figure{

    Cercle(int _x, int _y, int l, int h) {
        super(_x, _y, l, h);
    }

    @Override
    public void draw(Graphics2D g) {
        g.drawOval(x,y,largeur,hauteur);
    }
}
