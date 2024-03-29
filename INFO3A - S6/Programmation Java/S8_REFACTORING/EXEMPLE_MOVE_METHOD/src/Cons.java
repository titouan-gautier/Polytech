class Cons extends List {

    int val;

    List next;

    Cons(int v, List s){
        this.val =v ;
        this.next = s;
    }

    int head(){ return this.val; }

    List tail () { return this.next; }
}
