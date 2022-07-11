import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class Frogs {
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
                int weight[] = new int[n];
                int jump[] = new int[n];
                // int w=0,x=0,y=0,z=0;
                HashMap<Integer,Integer> map = new HashMap<>();
                for(int i=0;i<n;i++){
                    weight[i] = in.scanInt();
                    map.put(weight[i], i);
                }
                Arrays.sort(weight);
                for(int i=0;i<n;i++){
                    jump[i] = in.scanInt();
                }

                int count = 0;
                int last = 0;
                int total = 0;
                for(int i=0;i<n-1;i++){
                    int ind = map.get(weight[i]);
                    int nextInd = map.get(weight[i+1]);
                    while( (jump[ind]*last)+ind >= (jump[nextInd]*count)+nextInd ){
                        count++;
                    }
                    last = count;
                    total += count;
                    count = 0;
                }
                out.println(total);
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
 
        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }
 
    }
}


