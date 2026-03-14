from typing import Dict
import math


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

    def floydWarshall(self):

        # self.graph = {}
        # self.nb_vertices = 0
        # self.nb_edges = 0
        #{[A] : { [B] : 4, [C] : 9}}

        graph_dict: Dict = self.graph.copy()
        vertices = graph_dict.keys()
        matrix_shortest_path_added_weights = []
        matrix_intermediate_node = []

        
        # Basically, create a matrix nb_vertices * nb_vertices
        matrix_shortest_path_added_weights = [[math.inf for _ in range(self.nb_vertices)] for _ in range(self.nb_vertices)]
        for (vertex, dict_edges) in graph_dict.items():
            for key in dict_edges.keys():
                matrix_shortest_path_added_weights[vertex][key] = dict_edges[key]



        
        



vertices = [0, 1, 2]
edges = [(0,1), (1,2)]
weights = {(0,1) : 2, (1,2) : 4}
graph1 = DirectedWeightedGraph(vertices, edges, weights)  
graph1.display_graph()


