import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class Chemin {
    List<Node> chemin;
    Set<Node> visited;

    Chemin() {
        this.chemin = new LinkedList<>();
        this.visited = new HashSet<>();
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        for (int e=0; e< chemin.size() - 1; e++) {
            str.append(chemin.get(e).current.toString()).append(" -> ");
        }

        str.append(chemin.get(chemin.size() - 1).current.toString());

        return str.toString();
    }

}
