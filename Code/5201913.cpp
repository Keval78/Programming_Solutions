#include<bits/stdc++.h>
using namespace std;
#define ll long long
const ll N = 1000010;
ll mod=1e9+7, dp[N][2];
int main()
{
    ll n,c0=0,c1=0,tp0,tp1,x;
    cin>>n;
    for(int j=0;j<n;j++)
    {
        cin>>x;
        tp0 = dp[x][0], tp1 = dp[x][1];
        dp[x][1] = (dp[x][1]+c1+dp[x-1][0]+dp[x][0]+dp[x+1][0])%mod;
        dp[x][0] = (dp[x][0]+1+c0-dp[x-1][0]-dp[x][0]-dp[x+1][0]+3*mod)%mod;
        c0 = (c0+dp[x][0]-tp0+mod)%mod;
        c1 = (c1+dp[x][1]-tp1+mod)%mod;
        cout<<c0<<"  "<<c1<<"  "<<tp0<<"  "<<tp1<<endl;
        for(int i=0;i<n;i++)
        {
          for(int k=0;k<2;k++)
            cout<<dp[i][k]<<"   ";
          cout<<endl;
        }
    }
    cout<<c1<<endl;
    return 0;
}
