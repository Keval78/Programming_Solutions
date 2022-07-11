import java.util.*;
class TestClass
{
  public static void main(String []args)
  {
    Scanner sc =new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr = new int[n];
    for(int i=0;i<n;i++)
    {
      arr[i]=sc.nextInt();
    }
    HashMap<Integer,Long> hm = new HashMap<Integer,Long>();
    ArrayList<Integer> arrli = new ArrayList<Integer>(101);
    for(int i=0;i<n;i++)
    {
      if(hm.containsKey(arr[i]))
        hm.put(arr[i],hm.get(arr[i])+1);
      else
      {
        hm.put(arr[i],(long)1);
        arrli.add(arr[i]);
      }
    }
    long total=0;
    long sum=0;
    int m=arrli.size();
    //System.out.println(m);
    //System.out.println(arrli);
    for(int i=0;i<m;i++)
    {
      if(hm.get(arrli.get(i))>=2)
      {
        //System.out.print(i);
        for(int j=0;j<m;j++)
        {
          //System.out.println(j);
          if(i!=j)
          {
          sum=arrli.get(i)*2+arrli.get(j);
          if(sum%arrli.get(i)!=0 && sum%arrli.get(j)==0)
          {
            total+=hm.get(arrli.get(i))*(hm.get(arrli.get(i))-1)*hm.get(arrli.get(j))*3;
          }
        }
        }
      }
      for(int j=i+1;j<m;j++)
      {
        for(int k=j+1;k<m;k++)
        {
          sum=arrli.get(i)+arrli.get(j)+arrli.get(k);
          int count=0;
          if(sum%arrli.get(i)==0)
            count++;
          if(sum%arrli.get(j)==0)
            count++;
          if(sum%arrli.get(k)==0)
            count++;
          if(count==1)
          {
            total+=6*hm.get(arrli.get(i))*hm.get(arrli.get(j))*hm.get(arrli.get(k));
          }
        }
      }
    }
    System.out.println(total);
  }
}
