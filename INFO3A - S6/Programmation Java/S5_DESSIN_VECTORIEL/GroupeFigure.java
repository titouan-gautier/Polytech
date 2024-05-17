import java.awt.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;

public class GroupeFigure implements Figure{

    ArrayList<Figure> figures;

    GroupeFigure(Figure ... figures){
        this.figures = new ArrayList<Figure>();
        Collections.addAll(this.figures, figures);
    }

    public void add(Figure figure){
        figures.add(figure);
    }

    public void remove(Figure figure){
        figures.remove(figure);
    }

    public ArrayList<Figure> getFigures() {
        return figures;
    }

    @Override
    public void draw(Graphics2D g) {
        figures.forEach(figure -> figure.draw(g));
    }
}
