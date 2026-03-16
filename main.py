from Graph_class import DirectedWeightedGraph

graph = DirectedWeightedGraph()
graph.readFile('./Graphs/graph_test2.txt')
L, P = graph.floydWarshall()

graph.display_graph()
