#include<iostream>
#include<list>
#include<bits/stdc++.h>
using namespace std;
vector<long int> in(100005,0);
vector<long int> out(100005,0);
long int c=0;
#include <bits/stdc++.h>
using namespace std;
long int getMid(long int s, long int e) { return s + (e -s)/2; }
long int getSumUtil(long int *st, long int ss, long int se, long int qs, long int qe, long int si)
{
	if (qs <= ss && qe >= se)
		return st[si];
	if (se < qs || ss > qe)
		return 0;
	long int mid = getMid(ss, se);
	return getSumUtil(st, ss, mid, qs, qe, 2*si+1) +
		getSumUtil(st, mid+1, se, qs, qe, 2*si+2);
}
void updateValueUtil(long int *st, long int ss, long int se, long int i, long int diff, long int si)
{
	if (i < ss || i > se)
		return;
	st[si] = st[si] + diff;
	if (se != ss)
	{
		long int mid = getMid(ss, se);
		updateValueUtil(st, ss, mid, i, diff, 2*si + 1);
		updateValueUtil(st, mid+1, se, i, diff, 2*si + 2);
	}
}
void updateValue(long int arr[], long int *st, long int n, long int i, long int new_val)
{
	if (i < 0 || i > n-1)
	{
		cout<<"Invalid Input";
		return;
	}
	long int diff = new_val - arr[i];
	arr[i] = new_val;
	updateValueUtil(st, 0, n-1, i, diff, 0);
}
long int getSum(long int *st, long int n, long int qs, long int qe)
{
	if (qs < 0 || qe > n-1 || qs > qe)
	{
		cout<<"Invalid Input";
		return -1;
	}

	return getSumUtil(st, 0, n-1, qs, qe, 0);
}
long int constructSTUtil(long int arr[],long int ss, long int se, long int *st, long int si)
{
	if (ss == se)
	{
		st[si] = arr[ss];
		return arr[ss];
	}
long int mid = getMid(ss, se);
	st[si] = constructSTUtil(arr, ss, mid, st, si*2+1) +
			constructSTUtil(arr, mid+1, se, st, si*2+2);
	return st[si];
}

long int *constructST(long int arr[], long int n)
{
	long int x = (long int)(ceil(log2(n)));
	long int max_size = 2*(long int)pow(2, x) - 1;
	long int *st = new long int[max_size];
	constructSTUtil(arr, 0, n-1, st, 0);
	return st;
}

class Graph
{
	long int V;
	list<long int> *adj;

	void DFSUtil(long int v, bool visited[]);
public:
	Graph(long int V);
	void addEdge(long int v, long int w);
	void DFS(long int v);
};

Graph::Graph(long int V)
{
	this->V = V;
	adj = new list<long int>[V];
}

void Graph::addEdge(long int v, long int w)
{
	adj[v].push_back(w);
}

void Graph::DFSUtil(long int v, bool visited[])
{
	visited[v] = true;
	c++;
	in[v]=c;
	//cout << v << " ";
	list<long int>::iterator i;
	for (i = adj[v].begin(); i != adj[v].end(); ++i)
		if (!visited[*i])
			DFSUtil(*i, visited);
	out[v]=c;
}
void Graph::DFS(long int v)
{
	bool *visited = new bool[V];
	for (long int i = 0; i < V; i++)
		visited[i] = false;
	DFSUtil(v, visited);
}
int main()
{
	long long int n,q1,p,q;
	cin>>n>>q1;
	Graph g(n);
	for(long int i=0;i<n-1;i++)
	{
		cin>>p>>q;
		g.addEdge(p-1,q-1);
	}
	g.DFS(0);
	/*for(int i=0;i<n;i++)
	{
		cout<<in[i]<<" ";
	}
	cout<<"\n";
	for(int i=0;i<n;i++)
	{
		cout<<out[i]<<" ";
	}*/
	long int arr1[n],arr[n];
	long int temp;
	for(long int i=0;i<n;i++)
	{
		cin>>arr1[i];
	}
	for(long int i=0;i<n;i++)
	{
		arr[in[i]-1]=arr1[i];
	}
	/*cout<<"\n";
	for(int i=0;i<n;i++)
	{
		cout<<arr[i]<<" ";
	}*/
	for(long int i=0;i<n;i++)
	{
		long int result=0;
		temp=(long int)(sqrt(arr[i]));
		for(long int j=1;j<=temp;j++)
		{
			if(arr[i]%j==0)
			{
				if(j==arr[i]/j)
					result+=j%3;
				else
					result+=(j+(arr[i]/j))%3;
			}
		}
		if(result%3==0)
			arr[i]=1;
		else
			arr[i]=0;
	}
	long int *st = constructST(arr, n);
	while(q1--)
	{
		cin>>temp;
		if(temp==2)
		{
			long int ind;
			cin>>ind;
			cout<<getSum(st, n,in[ind-1]-1,out[ind-1]-1)<<"\n";
		}
		else{
			long int x,y;
			cin>>x>>y;
			long int result=0;
			result=0;
			long int temp=(long int)(sqrt(y));
			for(long int j=1;j<=temp;j++)
			{
				if(y%j==0)
				{
					if(j==y/j)
						result+=j%3;
					else
						result+=(j+(y/j))%3;
				}
			}
			if(result%3==0)
				updateValue(arr, st, n, in[x-1]-1, 1);
			else
				updateValue(arr, st, n, in[x-1]-1, 0);
		}
		for(int i=0;i<n;i++)
		{
			cout<<arr[i]<<"  ";
		}
	}
	return 0;
}
