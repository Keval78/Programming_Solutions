#include<bits/stdc++.h>
#define LL long long int
using namespace std;
LL a[1000001], b[1000001];
int main()	{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    LL n , k;
    cin >> n;
    cin >> k;
    for(int i = 1; i <= 2 * n; i++) {
        cin >> a[i];
    }
    int cnt1 = 0;
    for(int i = 1; i <= 2 * n; i += 2) {
        if(a[i] < a[i + 1])
            ++cnt1;
    }
    int cnt2 = 0;
    for(int i = 2; i <= 2 * n; i += 2) {
        if(a[i] < a[i - 1])
            ++cnt2;
    }
    if(cnt1 >= cnt2) {
        for(int i = 1; i <= 2 * n; i += 2)
            cout << i << " ";
        cout << endl;
        for(int i = 2; i <= 2 * n; i += 2)
            cout << i << " ";
    }
    else {
        for(int i = 2; i <= 2 * n; i += 2)
            cout << i << " ";
        cout << endl;
        for(int i = 1; i <= 2 * n; i += 2)
            cout << i << " ";
    }
}
