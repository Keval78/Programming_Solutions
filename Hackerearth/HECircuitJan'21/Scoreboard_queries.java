import java.io.OutputStream;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.HashMap;
public class Scoreboard_queries {
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
                int q = in.scanInt();
                int[] scores = new int[n];
                HashMap<Integer, Integer> uniqueScores = new HashMap<Integer, Integer>();
                for(int i=0;i<n;i++){
                    scores[i] = in.scanInt();
                    if(uniqueScores.containsKey(scores[i])){
                        uniqueScores.put(scores[i], uniqueScores.get(scores[i])+1);
                    }else{
                        uniqueScores.put(scores[i], 1);
                    }
                }
                int answer = uniqueScores.size() + 1;
                for(int i=0;i<q;i++){
                    int ind = in.scanInt()-1;
                    int val = in.scanInt();
                    
                    int temp = uniqueScores.get(scores[ind]) - 1;
                    uniqueScores.put(scores[ind], temp);
                    if(temp == 0)
                        answer--;
                    
                    scores[ind] = val;
                    if(uniqueScores.containsKey(scores[ind])){
                        uniqueScores.put(scores[ind], uniqueScores.get(scores[ind])+1);
                    }else{
                        uniqueScores.put(scores[ind], 1);
                    }
                    if(uniqueScores.get(scores[ind]) == 1)
                        answer++;
                    out.println(answer);
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
