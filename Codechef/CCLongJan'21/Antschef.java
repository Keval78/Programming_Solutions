import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

public class Antschef {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int t = 0;
	    if(sc.hasNextInt())
            t = sc.nextInt();
        while(t-- > 0){
            int n = 0,m=0;
            ArrayList<Integer> antPositions = new ArrayList<Integer>();
            if(sc.hasNextInt())
                n = sc.nextInt();
            for(int i=0; i<n; i++){
                if(sc.hasNextInt())
                    m = sc.nextInt();
                for(int j=0; j<m; j++){
                    antPositions.add(sc.nextInt());
                }
            }
            LinkedHashSet<Integer> uniquevalues= new LinkedHashSet<Integer>(antPositions);
            int countminus = 0, countplus = 0;
            for(Integer i : uniquevalues){
                if(i < 0)
                    countminus++;
                else
                    countplus++;
            }
            int minval = Math.min(countminus, countplus);
            int maxval = Math.max(countminus, countplus);
            System.out.println( ((countminus * (countminus - 1))/2) + ((countplus * (countplus - 1))/2) + minval - (((maxval-minval)*(maxval-minval-1))/2) );
        }
    }
    
}
