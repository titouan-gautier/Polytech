import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class Carte {

    HashMap<Ville, ArrayList<Pairs<Ville,Integer>>> carte;

    Carte() {
        this.carte = new HashMap<>();
    }

    public void addVille(Ville ville) {
        this.carte.put(ville, new ArrayList<>());
    }

    public void addRoute(Ville start, Ville end, int dist) {
        this.carte.get(start).add(new Pairs<Ville,Integer>(end, dist));
    }

    public Integer djikstraa(Ville start, Ville end) {

        @SuppressWarnings("unchecked")
        HashMap<Ville, ArrayList<Pairs<Ville, Integer>>> tempCarte = (HashMap<Ville, ArrayList<Pairs<Ville, Integer>>>) this.carte.clone();

        Set<Ville> visited = new HashSet<>();





    }

}
