import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Fairelct
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int t = 0;
	    if(sc.hasNextInt())
            t = sc.nextInt();
        while(t-- > 0){
            int n = 0,m = 0;
            if(sc.hasNextInt())
                n = sc.nextInt();
            if(sc.hasNextInt())
                m = sc.nextInt();
            int a[] = new int[n];
            int b[] = new int[m];
            long suma = 0,sumb = 0;
            for(int i=0;i<n;i++){
                if(sc.hasNextInt()){
                    a[i] = sc.nextInt();
                    suma += a[i];
                }
            }
            for(int i=0;i<m;i++){
                if(sc.hasNextInt()){
                  b[i] = sc.nextInt();
                  sumb += b[i];
                }
            }
            Arrays.sort(a);
            Arrays.sort(b);
            int i=0;
            for(i=0;i<Math.min(n,m);i++){
                if(suma <= sumb){
                  if(a[i]<b[i]){
                    suma -= a[i];
                    suma += b[m-i-1];
                    sumb -= b[m-i-1];
                    sumb += a[i];
                  }else
                    break;
                }else
                  break;
            }
            if(suma > sumb){
              System.out.println(i);
            }else{
              System.out.println("-1");
            }
        }
	}
}
