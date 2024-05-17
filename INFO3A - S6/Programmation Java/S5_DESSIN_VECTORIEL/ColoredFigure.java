import java.awt.*;
import java.util.ArrayList;
import java.util.Collections;

public class ColoredFigure extends Decorateur implements Figure{

    Color c;

    ColoredFigure(Color c,Figure ... figures){
        super(figures);
        this.c = c;
    }

    @Override
    public void draw(Graphics2D g) {
        g.setColor(c);
        this.figures.forEach(figure -> figure.draw(g));
    };
}
