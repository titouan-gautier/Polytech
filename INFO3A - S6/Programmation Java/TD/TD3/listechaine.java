interface Liste {
    int max() throws Impossible;
}

class Impossible extends Exception {
    Impossible(String msg) {
        super(msg);
    }
}

class Cellule implements Liste {

    int val;
    Liste next;

    Cellule(int v, Liste next) throws Impossible {
        if (next == null) {
            throw new Impossible("Impossible");
        }
        this.val = v;
        this.next = next;
    }

    public int max() {
        int tmp;
        try {
            tmp = this.next.max();
            return Math.max(tmp, this.val);
        } catch (Impossible e) {
            return this.val;
        }

    }

}

class Vide implements Liste {
    public int max() throws Impossible {
        //return Integer.MIN_VALUE;
        throw new Impossible("Impossible");
    }
}
