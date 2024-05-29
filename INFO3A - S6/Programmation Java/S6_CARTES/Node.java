import java.util.HashMap;
import java.util.Map;

public class Node implements Cloneable {

    Ville current;
    HashMap<Node,Float> voisin;
    Boolean visited;

    Node(Ville ville) {
        this.current = ville;
        this.voisin = new HashMap<>();
        this.visited = false;
    }

    public void appendVoisin(HashMap<Node,Float> voisin) {
        this.voisin.putAll(voisin);
        for (Map.Entry<Node,Float> e : voisin.entrySet()) {
            e.getKey().voisin.put(this, e.getValue());
        }
    }

    public Node nearestNode() {
        Float dist_min = Float.MAX_VALUE;
        Node nearest = null;
        for (Map.Entry<Node,Float> e : voisin.entrySet()) {
            if (e.getValue() < dist_min) {
                dist_min = e.getValue();
                nearest = e.getKey();
            }
        }

        return nearest;
    }

    public Node nearestNodeNotVisited() {
        Float dist_min = Float.MAX_VALUE;
        Node nearest = null;
        for (Map.Entry<Node,Float> e : voisin.entrySet()) {
            if (e.getValue() < dist_min && !e.getKey().visited) {
                dist_min = e.getValue();
                nearest = e.getKey();
            }
        }

       if (nearest == null) {
           return this.nearestNode();
       }

        return nearest;
    }

    @Override
    protected Node clone() throws CloneNotSupportedException {
        Node clonedNode = (Node) super.clone();
        clonedNode.voisin = new HashMap<>();
        return clonedNode;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Node) {
            if (this.current != ((Node) obj).current) {
                return false;
            }

            for (Map.Entry<Node,Float> list1 : this.voisin.entrySet()) {
                boolean bool = false;
                for (Map.Entry<Node,Float> list2 : ((Node) obj).voisin.entrySet()) {
                    if (list1.getKey().current.name == list2.getKey().current.name && list1.getValue() == list2.getValue()) {
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
        String str = "";
        for (Map.Entry<Node,Float> v : voisin.entrySet()) {
            str += v.getKey().current.toString() + " est à " + v.getValue().toString() + " de " + current + "\n";
        }
       return str;
    }

}
