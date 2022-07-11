#include <iostream>
using namespace std;
long long int fact(int n)
{
    long long int f=1;
    while(n>0)
    {
        f*=(n--);
        f%=1000000007;
    }
    return f;
}
int main()
{
   int n;
   cin>>n;
   long long int arr[2001][1002]={0};
   for(int i=1;i<1001;i++)
   {
       arr[2*i-1][i]=1;
   }
   for(int i=1;i<1002;i++)
   {
       for(int j=(2*i-1)+1;j<2001;j++)
       {
           if(i==1)
                arr[j][i]=j;
            else
            {
                arr[j][i]=arr[j-1][i]+arr[j-2][i-1];
                arr[j][i]%=1000000007;
            }
       }
   }
   for(int i=0;i<1002;i++)
   {
       long long int f=fact(i);
       for(int j=0;j<2001;j++)
       {
           arr[j][i]*=f;
       }
   }
   for(int i=0;i<1002;i++)
   {
       for(int j=0;j<2001;j++)
       {
           arr[j][i]+=arr[j][i-1];
           arr[j][i]%=1000000007;
       }
   }
   /*for(int i=0;i<=10;i++)
   {
       for(int j=0;j<=10;j++)
       {
           cout<<arr[i][j]<<"   ";
       }
       cout<<"\n";
   }*/
   cout<<arr[n][1001]<<"\n";
   return 0;
}
