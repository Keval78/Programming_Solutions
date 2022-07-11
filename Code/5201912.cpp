#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long t,x,y,a,b;
    cin>>t;
    while(t--)
    {
        cin>>x>>y>>a>>b;
        if(x*y == a+b)
            cout<<"Yes\n";
        else
            cout<<"No\n";
    }
    return 0;
}
