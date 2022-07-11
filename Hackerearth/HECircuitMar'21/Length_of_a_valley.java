import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class Length_of_a_valley {
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
                int[] arr = new int[n];
                int[] ans = new int[n];
                for(int i=0;i<n;i++){
                    arr[i] = in.scanInt();
                }
                int i=0;
                while(i<(n-1)){
                    if((i+1)<n && arr[i+1] > arr[i]){
                        int count = 1;
                        int start = i;
                        while((i+1)<n && arr[i+1] > arr[i]){
                            count++;
                            i++;
                        }
                        for(int j=start; j<=i; j++){
                            ans[j] = count--;
                            if(j==start && j!=0 && arr[j-1] > arr[j]){
                                ans[j]+=ans[j-1];
                            }
                        }
                    }
                    if((i+1)<n && arr[i+1] < arr[i]){
                        if(i==0){
                            ans[i] = 1;
                        }
                        ans[i+1] = ans[i]+1;
                    }
                    i++;
                }

                for(i=0;i<n;i++){
                    out.print(ans[i]+" ");
                }
                out.println();
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

