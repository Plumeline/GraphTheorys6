class DirectedWeightedGraph :
    def __init__(self, vertices, edges, weights):

        self.vertices = vertices # Simple list
        self.edges = edges # Set of couple (vertex1, vertex2) representing a directed edge from vertex1 to vertex2
        self.weights = weights # Dictionnary associating each couple from the list of edges to a weight
        self.nb_vertices = len(self.vertices)
        self.nb_edges = len(self.edges)

    def display_graph(self):
        print("  ", end="")
        for i in range (self.nb_vertices):
            print(self.vertices[i], end=" ")
        
        print("")
        
        for j in range(self.nb_vertices):
            print(self.vertices[j], end=" ")
            
            for x in range (self.nb_vertices):
                if ((j, x) in self.edges):
                    print(self.weights[(j,x)], end=" ")
                else:
                    print("0", end=" ")
            
            print("")


vertices = [0, 1, 2]
edges = [(0,1), (1,2)]
weights = {(0,1) : 2, (1,2) : 4}
graph1 = DirectedWeightedGraph(vertices, edges, weights)  
graph1.display_graph()


