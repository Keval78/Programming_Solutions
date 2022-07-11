#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	long long int n;
	while(t--)
	{
		cin>>n;
		int i,temp=1;
		for (i = 2; i * i <= (n+1); i++)
			if ((n+1) % i == 0)
			{
				temp=0;break;
			}
		(n!=1 && temp==1) ? cout<<"NO"<<endl : cout<<"YES"<<endl;
	}
}
