#include <bits/stdc++.h>

using namespace std;
const long long M = 1000000000;
const int N = 100;
vector<long long> v_odd[N], v_even[N];
vector<int> spf(N);

void f() {
	for (int i = 1; i < N; ++i) {
		spf[i] = i;
	}

	for (int i = 2; i*i < N; ++i) {
		if (spf[i] == i) {
			for (int j = i*i; j < N; j += i) {
				spf[j] = min(spf[j], i);
			}
		}
		for(int i=0;i<N;i++)
		{
			cout<<spf[i]<<"    ";
		}
		cout<<endl;
	}
}

int main(int argc, char const *argv[]) {
 f();
 return 0;
}
