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
public class Ptuples {
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
            int n = 1000000;
            boolean prime[] = new boolean[n + 1];
            int arr[] = new int[n+1];
            for (int i = 0; i <= n; i++)
                prime[i] = true;
            sieveOfEratosthenes(prime,in,out);
            HashSet<Integer> set = new HashSet<Integer>();
            for (int i = 2; i <= n; i++)
            {
                if (prime[i] == true)
                    set.add(i);
            }
            for(Integer s:set){
                for(Integer i:set){
                    if(set.contains(i+s)){
                        arr[i+s]=1;
                    }
                }
            }
            int sum = 0;
            for(int i=0;i<=n;i++){
                sum += arr[i];
                arr[i] = sum;
            }
            while(t-- > 0){
                n = in.scanInt();
                out.println(arr[n]);
            }
        }

        static void sieveOfEratosthenes(boolean[] prime, ScanReader in, PrintWriter out)
        {
            int n = prime.length - 1;
            for (int p = 2; p * p <= n; p++) 
            {
                if (prime[p] == true) 
                {
                    for (int i = p * p; i <= n; i += p)
                        prime[i] = false;
                }
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

