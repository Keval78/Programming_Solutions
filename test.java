import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class test {
    public static void main(String[] args) throws Exception{
        InputStream inputStream = new FileInputStream("/Users/jeetu/Desktop/Programming/input.txt");//System.in;
        OutputStream outputStream = new FileOutputStream("/Users/jeetu/Desktop/Programming/output.txt"); //System.out;
        ScanReader in = new ScanReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Solver solver = new Solver();
        int t = in.scanInt();
        solver.solve(t, in, out);
        out.close();
    }
 
    static class Solver {
        public void solve(int testNumber, ScanReader in, PrintWriter out) {
            int t = testNumber;
            while(t-- > 0){
                int n = in.scanInt();
                int[] count1 = new int[26];
                int[] count2 = new int[26];
                
                String s1 = in.scanString();
                String s2 = in.scanString();
                int mismatch = 0;

                for(int j=0;j<n;j++){
                    if(s1.charAt(j)-'a' >= 0 && s1.charAt(j)-'a' < 26)
                        count1[s1.charAt(j)-'a']++;
                    if(s2.charAt(j)-'a' >= 0 && s2.charAt(j)-'a' < 26)
                        count2[s2.charAt(j)-'a']++;
                    if(s1.charAt(j)!=s2.charAt(j))
                        mismatch++;
                }
                boolean flag = true;
                for(int j=0;j<26;j++){
                    if(count2[j] != count1[j])
                        flag = false;
                }
                if(flag){
                    if(mismatch==2 || mismatch==5)
                    out.println("NO");
                    else
                    out.println("YES");
                }else{
                    out.println("NO");
                }
            }
            // out.println(((t*(t+1))/2)+" ");
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

        public char scanChar() {
            int c = scan();
            while (isWhiteSpace(c)) c = scan();
            return (char) c;
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

        public String scanString() {
            int c = scan();
            while (isWhiteSpace(c)) c = scan();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = scan();
            } while (!isWhiteSpace(c));
            return res.toString();
        }
        
        public long scanLong() {
            long integer = 0;
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

        public void scanInt(int[] A, int size) {
            for (int i = 0; i < size; i++) A[i] = scanInt();
        }
 
    }

    static class CodeHash {
        public static void Radix_Sort(int a[]) {
 
            int multiplier = 1, len = a.length, max = Integer.MIN_VALUE;
            int b[] = new int[len];
            int bucket[];
            for (int i = 0; i < len; i++) if (max < a[i]) max = a[i];
            while (max / multiplier > 0) {
                bucket = new int[10];
                for (int i = 0; i < len; i++) bucket[(a[i] / multiplier) % 10]++;
                for (int i = 1; i < 10; i++) bucket[i] += (bucket[i - 1]);
                for (int i = len - 1; i >= 0; i--) b[--bucket[(a[i] / multiplier) % 10]] = a[i];
                for (int i = 0; i < len; i++) a[i] = b[i];
                multiplier *= 10;
            }
 
        }
 
        public static int lbound(int array[], int l, int h, long x) {
            while (l < h) {
                int mid = (l + h) / 2;
                if (array[mid] >= x) h = mid;
                else l = mid + 1;
            }
            return l;
        }
 
        public static int ubound(int array[], int l, int h, long x) {
            while (l < h) {
                int mid = (l + h) / 2;
                if (array[mid] <= x) l = mid + 1;
                else h = mid;
            }
            return l;
        }
 
    }
}
