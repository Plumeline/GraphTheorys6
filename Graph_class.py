class DirectedWeightedGrapgh :
    def __init__(self, nb_vertices, nb_edges, vertices, edges, weights):
        self.nb_vertices = nb_vertices
        self.nb_edges = nb_edges
        self.vertices = vertices # Simple list
        self.edges = edges # Set of couple (vertex1, vertex2) representing a directed edge from vertex1 to vertex2
        self.weights = weights # Dictionnary associating each couple from the list of edges to a weight

