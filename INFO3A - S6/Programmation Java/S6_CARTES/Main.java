import java.util.HashMap;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException {
        Carte carte = new Carte();

        // Création des instances de Ville
        Ville paris = new Ville("Paris");
        Ville rouen = new Ville("Rouen");
        Ville leMans = new Ville("Le Mans");
        Ville tours = new Ville("Tours");
        Ville angers = new Ville("Angers");
        Ville poitiers = new Ville("Poitiers");
        Ville nantes = new Ville("Nantes");
        Ville rennes = new Ville("Rennes");
        Ville brest = new Ville("Brest");

        // Création des instances de Node
        Node nodeParis = new Node(paris);
        Node nodeRouen = new Node(rouen);
        Node nodeLeMans = new Node(leMans);
        Node nodeTours = new Node(tours);
        Node nodeAngers = new Node(angers);
        Node nodePoitiers = new Node(poitiers);
        Node nodeNantes = new Node(nantes);
        Node nodeRennes = new Node(rennes);
        Node nodeBrest = new Node(brest);

        nodeParis.appendVoisin(new HashMap<Node, Float>() {{
            put(nodeRouen, 1.2f);
            put(nodeLeMans, 1.8f);
        }});

        nodeRouen.appendVoisin(new HashMap<Node, Float>() {{
            put(nodeLeMans, 1.9f);
            put(nodeRennes, 2.8f);
        }});

        nodeLeMans.appendVoisin(new HashMap<Node, Float>() {{
            put(nodeAngers, 0.95f);
            put(nodeTours, 1.1f);
        }});

        nodeTours.appendVoisin(new HashMap<Node, Float>() {{
            put(nodeAngers, 1.2f);
            put(nodePoitiers, 0.8f);
        }});

        nodeNantes.appendVoisin(new HashMap<Node, Float>() {{
            put(nodeAngers, 0.95f);
            put(nodePoitiers, 2.1f);
            put(nodeRennes, 1.05f);
        }});

        nodeRennes.appendVoisin(new HashMap<Node, Float>() {{
            put(nodeBrest, 2.4f);
        }});

        carte.appendNode(new LinkedList<>() {{
            add(nodeParis);
            add(nodeRouen);
            add(nodeLeMans);
            add(nodeTours);
            add(nodeAngers);
            add(nodePoitiers);
            add(nodeNantes);
            add(nodeRennes);
            add(nodeBrest);
        }});

        Carte carte_copy = carte.clone();

        Chemin chemin = carte_copy.getChemin(nodeBrest,nodeTours);
        System.out.println(chemin);


    }
}
