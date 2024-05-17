public class Forbidden extends Exception{

    String msgError;

    Forbidden(String msgError) {
        this.msgError = msgError;
    }

    @Override
    public String toString() {
        return msgError;
    }

}
