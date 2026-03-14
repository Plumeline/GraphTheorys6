from Graph_class import DirectedWeightedGraph

graph = DirectedWeightedGraph()
graph.readFile('./Graphs/graph_test2.txt')
L, P = graph.floydWarshall()

for line in L:
    print(line)
for line in P:
    print(line)
