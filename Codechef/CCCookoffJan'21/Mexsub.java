import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class Mexsub {
    public static void main(String[] args) throws Exception{
        InputStream inputStream = new FileInputStream("/Users/jeetu/Desktop/Programming/input.txt");//System.in;
        OutputStream outputStream = new FileOutputStream("/Users/jeetu/Desktop/Programming/output.txt"); //System.out;
        ScanReader in = new ScanReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Solver solver = new Solver();
        solver.solve(1, in, out);
        out.close();
    }

    static class Solver {
        public void solve(int testNumber, ScanReader in, PrintWriter out) {
            int t = in.scanInt();
            while(t-- > 0){
                int n = in.scanInt();
                int m = in.scanInt();
                int count1 = 0;
                int count2 = 0;
                for(int i=0;i<n;i++){
                    for(int j=0;j<m;j++){
                        char c = in.scanChar();
                        if(i%2==0){
                            if(j%2 == 0){
                                if(c=='*'){
                                    count1++;//Type1 incr
                                }else{
                                    count2++;//Type incr
                                }
                            }else{
                                if(c=='.'){
                                    count1++;//Type1 incr
                                }else{
                                    count2++;//Type incr
                                }
                            }
                        }else{
                            if(j%2 == 0){
                                if(c=='.'){
                                    count1++;//Type1 incr
                                }else{
                                    count2++;//Type incr
                                }
                            }else{
                                if(c=='*'){
                                    count1++;//Type1 incr
                                }else{
                                    count2++;//Type incr
                                }
                            }
                        }
                    }
                }
                out.println(Math.min(count1, count2));
            }
        }
 
    }
 
    static class ScanReader {
        private byte[] buf = new byte[4 * 1024];
        private int index;
        private BufferedInputStream in;
        private int total;
 
        public ScanReader(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }
 
        private int scan() {
            if (index >= total) {
                index = 0;
                try {
                    total = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (total <= 0) return -1;
            }
            return buf[index++];
        }
 
        public int scanInt() {
            int integer = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    integer *= 10;
                    integer += n - '0';
                    n = scan();
                }
            }
            return neg * integer;
        }
        
        public char scanChar() {
            int c = scan();
            while (isWhiteSpace(c)) c = scan();
            return (char) c;
        }
 
        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }
 
    }
}

