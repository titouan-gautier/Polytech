import java.awt.*;
import java.util.ArrayList;
import java.util.Collections;

abstract public class Decorateur implements Figure{

    ArrayList<Figure> figures;

    Decorateur(Figure ... figures){
        this.figures = new ArrayList<Figure>();
        Collections.addAll(this.figures, figures);
    }

    abstract public void draw(Graphics2D g);
}
