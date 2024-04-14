public class Liste {

    Cell head;
    Cell tail;
    int size;

    Liste() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public void addCell(Cell cell) {

        if (this.head == null) {
            this.head = cell;
        } else {
            cell.prev = this.tail;
            this.tail.next = cell;
        }

        this.tail = cell;
        this.size++;
    }

    @Override
    public String toString() {

        String str = "[";
        Cell cell = this.head;

        while (cell != null) {
            str += cell.val + ", ";
            cell = cell.next;
        }

        str += "]";

        return str;
    }

}
