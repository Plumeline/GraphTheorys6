from typing import Dict
import math
from copy import deepcopy

class DirectedWeightedGraph :
    def __init__(self):

        self.graph = {}
        self.nb_vertices = 0
        self.nb_edges = 0

    def readFile(self, file):
        '''
        Reads a graph from a file and stores it in the graph attribute as an adjacency list
        '''
        with open(file, "r", encoding="utf-8") as f:

            # Reading and verify validity of line 1
            line1 = f.readline().split()

            if len(line1) != 1:
                print(f"Incorrect file format for {file} : the line 1 is not in a valid format")
                return None
            try:
                nb_vertices = int(line1[0])
            except ValueError:
                print(f"Incorrect file format for {file} : the line 1 is not in a valid format")
                return None

            if nb_vertices < 0:
                print(f"Incorrect file format for {file} : the fst line 1 is a negative number")
                return None

            # Reading and verify validity of line 2
            line2 = f.readline().split()

            if len(line2) != 1:
                print(f"Incorrect file format for {file} : the line 2 is not in a valid format")
                return None

            try:
                nb_edges = int(line2[0])
            except ValueError:
                print(f"Incorrect file format for {file} : the line 2 is not in a valid format")
                return None

            if nb_edges < 0:
                print(f"Incorrect file format for {file} : the line 2 is a negative number")
                return None

            # Reading all the other lines
            all_lines = f.readlines()
            if len(all_lines) != nb_edges:
                if len(all_lines) > 0 and all_lines[-1] == "\n":
                    print(f"Incorrect file format for {file} : Remove the empty lines at the end of the file")
                    return None
                print(
                    f"Incorrect file format for {file} : The actual number of edges does not correspond to supposed number of edges")
                return None

            # Initialize an empty dictionary for each vertex to handle disconnected nodes
            graph = {i: {} for i in range(nb_vertices)}

            for i in range(0, len(all_lines)):
                all_lines[i] = all_lines[i].split()

                # Checking format validity
                if len(all_lines[i]) != 3:
                    print(f"Incorrect file format for {file} : the line {i + 2} is not in a valid format")
                    return None
                try:
                    vertex1 = int(all_lines[i][0])
                    vertex2 = int(all_lines[i][1])
                    weight = float(all_lines[i][2])
                except ValueError:
                    print(f"Incorrect file format for {file} : the line {i + 2} is not in a valid format")
                    return None

                # Checking values validity
                if vertex1 < 0 or vertex1 >= nb_vertices:
                    print(f"Incorrect file format for {file} : in line {i + 2}, the first vertex does not exist")
                    return None
                if vertex2 < 0 or vertex2 >= nb_vertices:
                    print(f"Incorrect file format for {file} : in line {i + 2}, the second vertex does not exist")
                    return None

                # Check if vertex2 is already a key in the inner dictionary of vertex1
                if vertex2 in graph[vertex1]:
                    print(f"Incorrect file format for {file} : in line {i + 2}, the edge already exists")
                    return None

                graph[vertex1][vertex2] = weight

        self.nb_vertices = nb_vertices
        self.nb_edges = nb_edges
        self.graph = graph


    def display_graph(self):
        '''
        displays the graph in the adjacency matrix format with vertical pipes and horizontal lines
        '''
        vertices = list(self.graph.keys())
        w = 9  # Width of each column box

        # print the header row with vertical pipes
        print(f"{'':>{w}}|", end="")
        for v in vertices:
            size = len(str(v))
            print(f"{'':>{(w-size)//2}}", end="")
            print(str(v), end="")
            print(f"{'':>{(w-size)//2 + (size+1)%2}}|", end="")
        print()

        # print a horizontal separator line
        total_columns = 1 + len(vertices)
        for _ in range(total_columns):
            print("-" * (w) + "+", end="")
        print()

        # print each row with vertical pipes
        for row_vertex in vertices:
            # Print the row label
            print(" " * (w-1-len(str(row_vertex))), end="")
            print(str(row_vertex), end="")
            print(" |", end="")

            # print the weights or 0
            for col_vertex in vertices:
                if col_vertex in self.graph[row_vertex]:
                    weight = self.graph[row_vertex][col_vertex]
                    size = len(str(weight))
                    print(f"{'':>{(w-size)//2}}", end="")
                    print(str(weight), end="")
                    print(f"{'':>{(w-size)//2 + (size+1)%2}}|", end="")

                else:
                    print(f"{'':>{(w-1)//2}}", end="")
                    print('-', end="")
                    print(f"{'':>{(w-1)//2}}|", end="")
            # move to the next line
            print()


    def floydWarshall(self):

        # self.graph = {}
        # self.nb_vertices = 0
        # self.nb_edges = 0
        #{[A] : { [B] : 4, [C] : 9}}

        graph_dict: Dict = self.graph.copy()

        # matrix of the weights of the shortest path
        L = [[math.inf for _ in range(self.nb_vertices)] for _ in range(self.nb_vertices)]

        # matrix of the path itself
        P = [[[] for _ in range(self.nb_vertices)] for _ in range(self.nb_vertices)]

        list_L = []
        list_P = []

        for (vertex, dict_edges) in graph_dict.items():

            L[vertex][vertex] = 0
            P[vertex][vertex] = [vertex]

            for key in dict_edges.keys():
                L[vertex][key] = dict_edges[key]
                P[vertex][key] = [vertex]

        list_L.append(deepcopy(L))
        list_P.append(deepcopy(P))
        # FLOYD WARSHALL (L AND P MATRICES)
        # L is matrix_shortest_path_added_weights
        # P is matrix_intermediate_node

        for intermediate_node in range(self.nb_vertices):
            for i in range(self.nb_vertices):
                for j in range(self.nb_vertices):

                    new_distance = L[i][intermediate_node] + L[intermediate_node][j]

                    if new_distance < L[i][j]:
                        L[i][j] = new_distance
                        P[i][j] = deepcopy(P[intermediate_node][j])


                    elif new_distance == L[i][j] and L[i][j] != math.inf and intermediate_node != i and intermediate_node != j:
                        for pred in P[intermediate_node][j]:
                            if pred not in P[i][j]:
                                P[i][j].append(pred)

            list_L.append(deepcopy(L))
            list_P.append(deepcopy(P))

        return (list_L, list_P)


    def has_absorbant_cycle(self, L):
        for i in range(self.nb_vertices):
            if L[i][i] < 0:
                return True
        return False

    """
    def display_all_path(self, P):
        for i in range(self.nb_vertices):
            for j in range(self.nb_vertices):
                if P[i][j] is not None:
                    path = []
                    current_node = j
                    while current_node != i:
                        path.append(current_node)
                        current_node = P[i][current_node]
                    path.append(i)
                    path.reverse()
                    print(f"Shortest path from {i} to {j} : " + str(path))
                else:
                    print(f"No path from {i} to {j}")
    """

    def display_all_path(self, P):
        for i in range(self.nb_vertices):
            for j in range(self.nb_vertices):
                if len(P[i][j]) > 0:
                    paths_to_explore = [[j]]
                    while len(paths_to_explore) > 0:
                        current_path = paths_to_explore.pop()
                        current_node = current_path[-1]
                        if current_node == i:
                            current_path.reverse()
                            print(f"Shortest path from {i} to {j} : " + str(current_path))
                        else:
                            for pred in P[i][current_node]:
                                paths_to_explore.append(current_path + [pred])
                else:
                    print(f"No path from {i} to {j}")