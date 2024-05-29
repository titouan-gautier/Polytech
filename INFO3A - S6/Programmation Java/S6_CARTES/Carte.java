import java.util.*;

public class Carte implements Cloneable {

    LinkedList<Node> carte;

    Carte() {
        this.carte = new LinkedList<>();
    }

    public void appendNode(LinkedList<Node> nodeList) {
        this.carte.addAll(nodeList);
    }

    public Chemin getChemin(Node villeA, Node villeB) {
        Chemin chemin = new Chemin();
        getCheminProcess(villeA,villeB,chemin);
        return chemin;
    }

    public boolean getCheminProcess(Node villeA, Node villeB, Chemin chemin) {
        chemin.chemin.add(villeA);
        chemin.visited.add(villeA);

        if (villeA.equals(villeB)) {
            return true;
        }

        for (Map.Entry<Node,Float> voisin : villeA.voisin.entrySet()) {
            if (!chemin.visited.contains(voisin.getKey())) {
                if (getCheminProcess(voisin.getKey(), villeB, chemin)) {
                    return true;
                }
            }
        }

        return false;
    }

    @Override
    protected Carte clone() throws CloneNotSupportedException {

        Carte clonedCarte = (Carte) super.clone();
        clonedCarte.carte = new LinkedList<>();
        HashMap<Node, Node> map = new HashMap<>();

        for (Node node : this.carte) {
            Node clonedNode = node.clone();
            map.put(node, clonedNode);
            clonedCarte.carte.add(clonedNode);
        }

        for (Node node : this.carte) {
            Node clonedNode = map.get(node);
            for (Map.Entry<Node, Float> entry : node.voisin.entrySet()) {
                clonedNode.voisin.put(map.get(entry.getKey()), entry.getValue());
            }
        }

        return clonedCarte;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Carte) {
            for (Node node1 : this.carte) {
                boolean bool = false;
                for (Node node2 : ((Carte) obj).carte) {
                    if (node1.equals(node2)) {
                        bool = true;
                        break;
                    }
                }
                if (!bool) {
                    return false;
                }
            }
        }
        return true;
    }

    @Override
    public String toString() {
        String str= "";

        for(Node n : carte) {
            str += n.toString() + "\n";
        }

        return str;
    }

}
