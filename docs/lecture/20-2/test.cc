#include <bits/stdc++.h> 
using namespace std; 

class Graph
{
    int V;
    vector<int> * adj;
    void _dfs(int v, bool visited[]);
public:
    Graph(int V);
    void addEdge(int u, int v);
    void dfs(int v);
}

Graph::Graph(int V)
{
    this->V = V;
    this->adj = new vector<int>[V];
}

void Graph::addEdge(int u, int v) 
{ 
    u -= 1;
    v -= 1;
	adj[u].push_back(v); 
	// adj[v].push_back(u); 
} 

void Graph::_dfs(int i, bool visited[])
{
    visited[i] = true;
    cout << i << " ";
    for (auto v: this->adj[i])
        if(!visited[v])
            this->_dfs()
}

void printGraph(vector<int> adj[], int V) 
{ 
	for (int v = 0; v < V; ++v) 
	{ 
		cout << "\n Adjacency list of vertex "
			<< v + 1 << "\n head "; 
		for (auto x : adj[v]) 
            cout << "-> " << x + 1; 
		printf("\n"); 
	} 
} 

int main() 
{ 
	// int V = 5; 
	// vector<int> adj[V]; 
	// addEdge(adj, 0, 1); 
	// addEdge(adj, 0, 4); 
	// addEdge(adj, 1, 2); 
	// addEdge(adj, 1, 3); 
	// addEdge(adj, 1, 4); 
	// addEdge(adj, 2, 3); 
	// addEdge(adj, 3, 4); 
	// printGraph(adj, V); 
	int V = 5; 
	vector<int> adj[V]; 
	addEdge(adj, 1, 2); 
	addEdge(adj, 3, 2); 
	addEdge(adj, 3, 4); 
	addEdge(adj, 4, 5); 
	addEdge(adj, 5, 2); 
	addEdge(adj, 2, 4); 
	printGraph(adj, V); 
	return 0; 
} 
