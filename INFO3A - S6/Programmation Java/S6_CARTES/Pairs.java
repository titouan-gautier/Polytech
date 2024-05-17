public class Pairs<K, V> {
    private final K key;
    private final V value;

    public Pairs(K key, V value) {
        this.key = key;
        this.value = value;
    }

    @Override
    public String toString() {
        return "{" + key + ", " + value + "}";
    }
}