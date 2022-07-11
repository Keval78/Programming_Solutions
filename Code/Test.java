import java.util.*;
import java.lang.Math;
public class Test{
 static class Graph
	{
		int V;
		LinkedList<Integer> adjListArray[];
		Graph(int V)
		{
			this.V = V;
			adjListArray = new LinkedList[V];
			for(int i = 0; i < V ; i++){
				adjListArray[i] = new LinkedList<>();
			}
		}
	}
 static void addEdge(Graph graph, int src, int dest)
	{
		graph.adjListArray[src].add(dest);
	}
	/*static void printGraph(Graph graph)
	{
		for(int v = 0; v < graph.V; v++)
		{
			System.out.println("Adjacency list of vertex "+ v);
			System.out.print("head");
			for(Integer pCrawl : graph.adjListArray[v]){
				System.out.print(" -> "+pCrawl);
			}
			System.out.println("\n");
		}
	}*/
	static int findSum(Graph graph,int[] arr1,int[] arr,int s)
	{
		for(Integer pCrawl : graph.adjListArray[s]){
			arr1[s]+=findSum(graph,arr1,arr,pCrawl);
		}
		arr1[s]+=arr[s];
		return arr1[s];
	}
	public static void main(String args[])
	{
		int N,Q,p,q;
		Scanner sc = new Scanner(System.in);
		N=sc.nextInt();
		Q=sc.nextInt();
		Graph graph = new Graph(N);
		for(long i=0;i<N-1;i++)
		{
		    p=sc.nextInt();
		    q=sc.nextInt();
		    addEdge(graph, p-1, q-1);
		}
		int[] arr = new int[N];
		int[] arr1 = new int[N];
		for(int i=0;i<N;i++)
		{
			int temp=sc.nextInt();
			int result=0;
			int lim=(int)(Math.sqrt(temp));
			for(int j=1;j<=lim;j++)
			{
				if(temp%j==0)
				{
					if(j==(temp/j))
						result+=(j%3);
					else
						result+=((j+(temp/j))%3);
				}
			}
			if(result%3==0)
				arr[i]=1;
			//System.out.println(arr[i]);
		}
		findSum(graph,arr1,arr,0);
		while(Q--!=0)
		{
			int i,x;
			i=sc.nextInt();
			if(i==1)
			{
				x=sc.nextInt();
				int temp=sc.nextInt();
				int result=0;
				int lim=(int)(Math.sqrt(temp));
				for(int j=1;j<=lim;j++)
				{
					if(temp%j==0)
					{
						if(j==(temp/j))
							result+=(j%3);
						else
							result+=((j+(temp/j))%3);
					}
				}
				if(result%3==0)
				{
					if(arr[x-1]==1)
						continue;
					else{
						arr[x-1]=1;
						for(i=0;i<N;i++)
							arr1[i]=0;
						findSum(graph,arr1,arr,0);
					}
				}
				if(result%3!=0)
				{
					if(arr[x-1]==0)
						continue;
					else{
						arr[x-1]=0;
						for(i=0;i<N;i++)
							arr1[i]=0;
						findSum(graph,arr1,arr,0);
					}
				}
			}
			else{
				x=sc.nextInt();
				System.out.println(arr1[x-1]);
			}
		}
	}
}
