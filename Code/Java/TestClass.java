import java.util.*;
class TestClass{
  public static void main(String args[])throws Exception{
    Scanner sc = new Scanner(System.in);
    int length_array=sc.nextInt();
    int key=sc.nextInt();
    int[] array = new int[length_array];
    for(int i=0;i<length_array;i++)
    {
      array[i]=sc.nextInt();
    }
    int special_count=0;
    for(int k=0;k<length_array;k++)
    {
      int count=0;
      for(int j=0;j<length_array;j++)
      {
        if(array[j]>array[k])
          count+=1;
        if(count>key)
          break;
      }
      if(count>=key){
        special_count+=array[k];
      }
      System.out.println(special_count);
      sc.close();
    }
  }
}
