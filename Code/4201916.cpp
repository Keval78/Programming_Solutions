#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
const int maxn = 1e6 + 20;
ll a[maxn];
int main()
{
	int n;
	ll l , r;
	scanf("%d%lld%lld", &n, &l, &r);
	for(int i = 0; i < n; i++)
	    scanf("%lld", &a[i]);
	sort(a , a + n);
	n = unique(a , a + n) - a;
	ll g = 0;
	for(int i = 1; i < n; i++)
		g = __gcd(g , a[i] - a[0]);
	vector<ll> div;
	vector<ll> div2;
	for(ll i = 1; i * i <= g; i++)
		if(g % i == 0)
		{
			div.pb(i);
			if(i * i != g)
				div2.pb(g / i);
		}
	//sort(div.begin() , div.end());
	reverse(div2.begin() , div2.end());
	reverse(div1.begin() , div1.end());
  div.insert(div.end(), div2.begin(), div2.end());

	if(!g)
	    cout << r + a[0] << endl;
	l += a[0];
	r += a[0];
	for(auto ans : div)
		if((r / ans * ans) >= l)
			return cout << ans << endl , 0;
}
/*
Half
*/
