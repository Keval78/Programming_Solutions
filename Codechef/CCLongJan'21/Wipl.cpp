#include <bits/stdc++.h>
#define in(n,arr) for(int i=0; i<n ; ++i) cin >> arr[i]
#define out(n,arr) for(int i=0; i<n ; ++i) cout << arr[i] << " "
#define ll long long int
const ll MAX = 1e9;
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    #ifndef ONLINE_JUDGE
        freopen("../input.txt","r",stdin);
        freopen("../output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    while(t--){
        int n,k;
        cin >> n >> k;
        int height[n+1];
        int suffix[n+1];
        int dp[n+1][k+1];

        for(int i=0;i<n;i++){
            cin >> height[i];
        }
        sort(height,height+n);
        suffix[n]=0;
        for(int i=n-1;i>=0;i--){
            suffix[i]=suffix[i+1]+height[i];
        }
        for(int i=0;i<=n;i++)
            for(int j=0;j<=k;j++)
                dp[i][j]=MAX;
        dp[n][0]=0;
        for(int i=n-1;i>=0;i--){
            for(int j=k;j>=0;j--){
                if(j<=height[i]){
                    dp[i][j] = height[i];
                    continue;
                }
                if(dp[i+1][j-height[i]] == MAX)
                    dp[i][j] = MAX;
                else
                    dp[i][j] = min(dp[i+1][j],dp[i+1][j-height[i]]+height[i]);
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<=k;j++)
                cout<< dp[i][j] <<" ";
            cout<<"\n";
        }
        int flag = 0;
        for(int i=n-1;i>=0;i--){
            if(suffix[i]-dp[i][k]>=k){
                cout<<n-i<<"\n";
                flag=1;
                break;
            }
        }
        if(flag==1){
            continue;
        }
        cout<< -1 <<"\n";
    }

}