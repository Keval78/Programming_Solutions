import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class Tree_construction {
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
            int n = in.scanInt();
            int m = in.scanInt();
            if(m > (n*(n+1))/2 || m < n+(n-1)){
                out.println("-1");
                return;
            }
            int curr = n;
            int parrentVertices = 1;
            int curVertice = 2;
            while(m>0){
                // out.println("m: "+m+",cur: "+curr+",cV: "+curVertice);
                if(m-curr>(curr-1)){
                    m-=curr;
                    out.println(parrentVertices+" "+curVertice);
                }
                else if(m-curr<(curr-1)){
                    m-=1;
                    parrentVertices--;
                    out.println(parrentVertices+" "+curVertice);
                }
                else{
                    m-=(curr+curr-1);
                    parrentVertices = curVertice-1;
                    // out.println("IN m: "+m+",cur: "+curr+",cV: "+curVertice);
                    for(int i=0;i<n-curVertice+1;i++){
                        out.println(parrentVertices+" "+(curVertice+i));
                    }
                }
                curr--;
                curVertice++;
                parrentVertices++;
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
