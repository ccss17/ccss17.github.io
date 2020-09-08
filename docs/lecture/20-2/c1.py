class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 

    def add_edge(self, src, dest): 
        def _add_edge(n, m):
            node = AdjNode(n) 
            node.next = self.graph[m] 
            self.graph[m] = node 
        _add_edge(dest, src)
        _add_edge(src, dest)

    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 

if __name__ == "__main__": 
	V = 5
	graph = Graph(V) 
	graph.add_edge(0, 1) 
	graph.add_edge(0, 4) 
	graph.add_edge(1, 2) 
	graph.add_edge(1, 3) 
	graph.add_edge(1, 4) 
	graph.add_edge(2, 3) 
	graph.add_edge(3, 4) 

	graph.print_graph() 