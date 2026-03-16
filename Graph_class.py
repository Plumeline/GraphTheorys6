from typing import Dict
import math

class DirectedWeightedGraph :
    def __init__(self):

        self.graph = {}
        self.nb_vertices = 0
        self.nb_edges = 0

    def readFile(self, file):
        '''
        Reads a file and returns a tuple containing:
        - the number of vertices
        - the number of edges
        - the graph represented as a nested dictionary { vertex1 : { vertex2 : weight, ... }, ... }
        If the file is not in a valid format, returns None and prints an error message.
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

            # --- NEW STRUCTURE INITIALIZATION ---
            # Initialize an empty dictionary for each vertex to handle disconnected nodes safely
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

                # --- UPDATED DUPLICATE CHECK ---
                # Check if vertex2 is already a key in the inner dictionary of vertex1
                if vertex2 in graph[vertex1]:
                    print(f"Incorrect file format for {file} : in line {i + 2}, the edge already exists")
                    return None

                # --- UPDATED ASSIGNMENT ---
                graph[vertex1][vertex2] = weight

        self.nb_vertices = nb_vertices
        self.nb_edges = nb_edges
        self.graph = graph


    def display_graph(self):
        '''
        Displays the graph in the adjacency matrix format with vertical pipes and horizontal lines.
        '''
        vertices = list(self.graph.keys())
        w = 9  # Width of each column box

        # Print the header row with vertical pipes
        print(f"{'':>{w}}|", end="")
        for v in vertices:
            print(f"{'':>{(w+1)//2 - len(str(v))//2 - 1}}", end="")
            print(str(v), end="")
            print(f"{'':>{w - (w+1)//2 -len(str(v))//2}}|", end="")
        print()

        # Print a horizontal separator line
        total_columns = 1 + len(vertices)
        for _ in range(total_columns):
            print("-" * (w) + "+", end="")
        print()

        # Print each row with vertical pipes
        for row_vertex in vertices:
            # Print the row label
            print(" " * (w-2), end="")
            print(str(row_vertex), end="")
            print(" |", end="")

            # Print the weights or 0
            for col_vertex in vertices:
                if col_vertex in self.graph[row_vertex]:
                    weight = self.graph[row_vertex][col_vertex]
                    print(f"{'':>{(w+1)//2 - len(str(weight))//2 - 1}}", end="")
                    print(str(weight), end="")
                    print(f"{'':>{w - (w+1)//2 -len(str(weight))//2}}|", end="")

                else:
                    print(f"{'':>{(w+1)//2 - 1}}", end="")
                    print('0', end="")
                    print(f"{'':>{w - (w+1)//2}}|", end="")
            # Move to the next line
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
        P = [[None for _ in range(self.nb_vertices)] for _ in range(self.nb_vertices)]
        

        for (vertex, dict_edges) in graph_dict.items():
            for key in dict_edges.keys():
                L[vertex][key] = dict_edges[key]
                P[vertex][key] = vertex

            L[vertex][vertex] = 0
        
        # FLOYD WARSHALL (L AND P MATRICES)
        # L is matrix_shortest_path_added_weights
        # P is matrix_intermediate_node

        for intermediate_node in range(self.nb_vertices):
            for i in range(self.nb_vertices):
                for j in range(self.nb_vertices):
                    if L[i][intermediate_node] + L[intermediate_node][j] < L[i][j] :
                        L[i][j] = L[i][intermediate_node] + L[intermediate_node][j]
                        P[i][j] = P[intermediate_node][j]
        
        return (L, P)
    

    def has_absorbant_cycle(self, L):
        for i in range(self.nb_vertices):
            if L[i][i] < 0:
                return True
        return False
    
