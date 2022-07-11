import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class Andpref {
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
                int arr[] = new int[n];
                ArrayList<ArrayList<Integer>> vals = new ArrayList<>(21);
                for(int i=0;i<21;i++){
                    vals.add(new ArrayList());
                }
                for(int i=0;i<n;i++){
                    int val = in.scanInt();
                    arr[i] = val;
                    for(int j=1;j<=20;j++){
                        if ((val & (1 << (j - 1))) > 0){
                            vals.get(j).add(val);
                        }
                    }
                }
                int row = vals.size();
                int sum = 0;
                int lastMax = 0;
                for (int i = 0; i < row; i++) {
                    int col = vals.get(i).size();
                    sum = 0;
                    for (int j = 0; j < col; j++) {
                        sum += vals.get(i).get(j);
                    }
                    if (sum>0)
                        out.println("sum: "+sum);
                    if(lastMax < sum)
                        lastMax = sum;
                }
                out.println(lastMax);
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

