import java.awt.*;

public class BoldFigure extends Decorateur implements Figure {

    Stroke s;

    BoldFigure(Stroke s, Figure ... figures) {
        super(figures);
        this.s = s;
    }

    @Override
    public void draw(Graphics2D g) {
        g.setStroke(s);
        this.figures.forEach(figure -> figure.draw(g));
    }
}
