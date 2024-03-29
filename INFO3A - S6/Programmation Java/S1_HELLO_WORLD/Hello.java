class Hello {

    public static void main(String[]a) {
        Langue fr = new French();
        Message msg = new Message(fr);
        msg.print();
    }
}
