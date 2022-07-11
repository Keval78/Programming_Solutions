import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.InputStream;
public class Teamname {
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
                ArrayList<int[]> firstChar = new ArrayList<int[]>();
                HashMap<String, Integer> map = new HashMap<String, Integer>();
                int j=0;
                for(int i=0;i<n;i++){
                    char c = in.scanChar();
                    String commonWord = in.scanString();
                    if(!map.containsKey(commonWord)){
                        map.put(commonWord,j);
                        firstChar.add(new int[27]);
                        if(firstChar.get(j)[c-'a'] == 0)
                            firstChar.get(j)[26] += 1;
                        firstChar.get(j)[c-'a'] = 1;
                        j++;
                    } else {
                        int ind = map.get(commonWord);
                        if(firstChar.get(ind)[c-'a'] == 0)
                            firstChar.get(ind)[26] += 1;
                        firstChar.get(ind)[c-'a'] = 1;
                    }
                }

                long count = 0;
                for(int i=0; i<firstChar.size();i++){
                    for(int k=i+1; k<firstChar.size();k++){
                        int count1 = firstChar.get(i)[26];
                        int count2 = firstChar.get(k)[26];
                        for(int h=0;h<26;h++){
                            if(firstChar.get(i)[h] == 1 && firstChar.get(k)[h] == 1){
                                count1 -= 1;
                                count2 -= 1;
                            }
                        }
                        count += (count1*count2);
                    }
                }
                out.println(count*2);
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
 
        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }
 
    }
}

