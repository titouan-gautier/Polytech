import javax.swing.* ;
import java.awt.* ;


class MaFenetre extends JFrame {
    MaFenetre(Figure r){
	setSize(320,200+50);
	setContentPane(new Paneau(r)) ;
    }
}





class Paneau extends JPanel {

    Figure p ;

    Paneau(Figure p){
	this.p=p ;
    }

    @Override
    public void paintComponent (Graphics g){
	if (g instanceof Graphics2D)
	    p.draw((Graphics2D) g) ;
	else throw new RuntimeException();
    }
    
}




class Test {

    public static void main(String[] args){

        Figure g = new GroupeFigure(new Rectangle(10, 10, 100 , 50),
                                    new Cercle(10, 10, 100 , 50));

        Figure test1 = new ColoredFigure(
                Color.blue,
                new GroupeFigure(
                        new Rectangle(10, 10, 100 , 50),
                        new Cercle(10, 10, 100 , 50)
                )
        );

        Figure test2 = new GroupeFigure(
                new ColoredFigure(
                        Color.blue,
                        new Cercle(10, 10, 100 , 50)
                ),
                new Rectangle(10, 10, 100 , 50)
        );

        Figure test3 = new BoldFigure(
                new BasicStroke((float) 3),
                new ColoredFigure(
                        Color.red,
                        new Rectangle(10, 10, 100 , 50)
                )
        );

        MaFenetre fen = new MaFenetre(test3) ;
        fen.setVisible(true);
        fen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
    
}
