#include<bits/stdc++.h>
using namespace std;

void addEdge(vector<int> adj[], int u, int v)
{
	adj[u].push_back(v);
	adj[v].push_back(u);
}

void DFSUtil(int u, vector<int> adj[], vector<bool> &visited)
{
	visited[u] = true;
	cout << u << " ";
	for (int i=0; i<adj[u].size(); i++)
		if (visited[adj[u][i]] == false)
			DFSUtil(adj[u][i], adj, visited);
}
void DFS(vector<int> adj[], int V)
{
	vector<bool> visited(V, false);
	for (int u=0; u<V; u++)
		if (visited[u] == false)
			DFSUtil(u, adj, visited);
}

int main()
{
	long long int N,Q,p,q;
	cin>>N>>Q;
	vector<int> adj[5];
	for(long long int i=0;i<N-1;i++)
	{
	    cin>>p>>q;
			cout<<i;
	    addEdge(adj, p, q);
	}
	DFS(adj, N);
	return 0;
}
