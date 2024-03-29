public class Message {
    Langue a;

    Message(Langue fr) {
        this.a = fr;
    }

    void print() {
        System.out.println(this.a.Hello());
    }
}
