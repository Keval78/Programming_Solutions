import java.util.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Wipl
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
        int t = 0;
	    if(sc.hasNextInt())
            t = sc.nextInt();
        while(t-- > 0){
            int n = 0, k = 0;
            if(sc.hasNextInt())
                n = sc.nextInt();
            if(sc.hasNextInt())
                k = sc.nextInt();
            int a[] = new int[n];
            long suma = 0;
            for(int i=0;i<n;i++){
                if(sc.hasNextInt()){
                    a[i] = sc.nextInt();
                }
            }
            Arrays.sort(a);
            suma=a[n-1];
            HashSet<Integer> uniquevalues= new HashSet<Integer>();
            uniquevalues.add(a[n-1]);
            int ind = -1;
            for(int i=n-2;i>=0;i--){
                HashSet<Integer> addUniquevalues= new HashSet<Integer>();
                suma=suma+a[i];
                for (int val : uniquevalues) {
                    addUniquevalues.add(val);
                    addUniquevalues.add(a[i]);
                    addUniquevalues.add(val+a[i]);
                    if( ((val+a[i]>=k) && (suma-val-a[i]>=k)) || ((a[i]>=k) && (suma-a[i]>=k)) ){
                        ind=n-i;
                        break;
                    }
                }
                if(ind!=-1)
                    break;
                uniquevalues = addUniquevalues;
            }
            System.out.println(ind);
        }
	}
}
