//A WIDA Project
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<sstream>
#include<cstdlib>
using namespace std;
//#pragma GCC			optimize("Ofast,no-stack-protector,unroll-loops,fast-math")
#define LL			long long
#define IOS()		ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define ms(a,b)		memset(a,b,sizeof (a))
#define FOR(i,a,b)	for(int i=(a);i<=(b);i++)
#define FOR2(i,a,b)	for(int i=(a);i<=(b);i+=2)
#define FORD(i,a,b)	for(int i=(a);i>=(b);i--)
#define sz(a)		int((a).size())
#define mp			make_pair
#define bugl()		cout<<"=========="<<endl;
#define bug(x)		cout<<"cout<<"<<x<<endl;
#define bug2(x,y)	cout<<"cout<<"<<x<<" and "<<y<<endl;
#define bugl2(x,y)	cout<<"==========cout<<"<<x<<" and "<<y<<endl;
#define bug3(x,y,z)	cout<<"cout<<"<<x<<" "<<y<<" and "<<z<<endl;
#define bugl3(x,y,z)cout<<"==========cout<<"<<x<<" "<<y<<" and "<<z<<endl;
#define EL			"\n"
const LL MAX18=1e18+5;
const int MOD=1e9+5;
const int MAX9=1e9+5;
const int MAX=1e6+5;
const int MAX5=1e5+5;
inline LL mygcd(LL x,LL y) {return x%y==0?y:mygcd(y,x%y);}
inline LL mylcm(LL x,LL y) {return x/mygcd(x,y)*y;}
inline LL mymax(LL x,LL y) {return x<y?y:x;}
inline LL mymin(LL x,LL y) {return x>y?y:x;}
inline double mymax(double x,double y)		{return x>y?y:x;}
inline double mymin(double x,double y)		{return x>y?y:x;}
inline LL mypow(LL n,LL k,int p=MOD)		{LL r=1;for(;k;k>>=1){if(k&1)r=r*n%p;n=n*n%p;}return r;}
inline void addmod(int&a,int val,int p=MOD) {if((a=(a+val))>=p)a-=p;}
inline void submod(int&a,int val,int p=MOD) {if((a=(a-val)) <0)a+=p;}
//===============================================================
LL T,ans,n,a[MAX],b[MAX],c[MAX],x;
//===============================================================
int main(){
	IOS();
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
	#endif
	cin>>T;
	while(T-->0){
		cin>>n;
		ans=MAX18;
		FOR(i,1,n){
			cin>>x;
			a[(x+1)/2]=i;
		}
		FOR(i,1,n){
			cin>>x;
			b[x/2]=i;
		}
		FORD(i,n-1,1){ // Prefix
			b[i]=min(b[i],b[i+1]);
		}
		FOR(i,1,n){
			ans=min(ans,a[i]+b[i]-2);
		}
		if(ans!=MAX18) cout<<ans<<EL;
		else cout<<0<<endl;
	}
	return 0;
}