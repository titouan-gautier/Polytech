import javax.swing.* ;
import java.awt.* ;


class MaFenetre extends JFrame {

   JPanel pan ;

   MaFenetre(){
	setSize(320,200+50);
	pan = new Paneau(new Palet()) ; 
/*	pan = new Paneau(new Pulsar()) ; */
	setContentPane(pan) ;
    }
}



class Paneau extends JPanel {

   MovingObject p ;

   Paneau(MovingObject p){
	super();
	this.p=p ;
   }

   @Override
   public void paintComponent (Graphics g){
	final Rectangle r = p.getRect() ;
	g.fillRect (r.x, r.y, r.width, r.height);
	p.deplace() ;
   }
}



public class Jeu {

   public static void main(String[] args) throws InterruptedException {

	System.setProperty("sun.java2d.opengl", "true"); /* pour animation fluide */

	MaFenetre fen = new MaFenetre() ;

	fen.setVisible(true);

	fen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	while (true){
	    fen.repaint() ; 
		Thread.sleep(50);
	}

   }
}
