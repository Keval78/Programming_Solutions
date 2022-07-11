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
public class Prigame {
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
            int[] primeCount = new int[1000003];
            sieveOfEratosthenes(1000002, primeCount);
            while(t-- > 0){
                int x = in.scanInt();
                int y = in.scanInt();
                if(y==1){
                    if(x>2)
                        out.println("Divyam");
                    else
                        out.println("Chef");
                } else {
                    int n = primeCount[x];
                    if(n<=y)
                        out.println("Chef");
                    else
                        out.println("Divyam");
                }
            }
        }

        void sieveOfEratosthenes(int n, int[] primeCount)
        {
            boolean prime[] = new boolean[n + 1];
            for (int i = 0; i <= n; i++)
                prime[i] = true;
 
            for (int p = 2; p * p <= n; p++) 
            {
                if (prime[p] == true) 
                {
                    for (int i = p * p; i <= n; i += p)
                        prime[i] = false;
                }
            }
            int count = 0;
            for (int i = 2; i <= n; i++)
            {
                if (prime[i] == true)
                    count += 1;
                primeCount[i] = count;
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
