#include<bits/stdc++.h>
using namespace std;

int main()
{
  int n,m,count;
  cin>>n;
  while(n--)
  {
    cin>>m;
    int m1=m-(m%2);
    int m2=m-(m%4);
    count=m1/2 - m2/4
    cout<<count<<endl;
  }
}
