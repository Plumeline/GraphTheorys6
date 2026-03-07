def readFile(file : str) :
    '''
    Reads a file and returns a tuple containing :
    - the number of vertices
    - the number of edges
    - the list of vertices
    - the set of edges
    - the dictionary of weights
    If the file is not in a valid format, returns None and prints an error message.
    '''
    with open(file, "r", encoding="utf-8") as f:

        # Reading and verify validity of line 1
        line1 = f.readline().split()

        if len(line1) != 1 :
            print(f"Incorrect file format for {file} : the line 1 is not in a valid format")
            return None
        try:
            nb_vertices = int(line1[0])
        except:
            print(f"Incorrect file format for {file} : the line 1 is not in a valid format")
            return None
            
        if nb_vertices < 0:
            print(f"Incorrect file format for {file} : the fst line 1 is a negative number")
            return None
        

        #Reading and verify validity of line 2
        line2 = f.readline().split()

        if len(line2) != 1 :
            print(f"Incorrect file format for {file} : the line 2 is not in a valid format")
            return None
    
        try:
            nb_edges = int(line2[0])
        except:
            print(f"Incorrect file format for {file} : the line 2 is not in a valid format")
            return None
            
        if nb_edges < 0:
            print(f"Incorrect file format for {file} : the line 2 is a negative number")
            return None
        

        # Reading all the other lines
        all_lines = f.readlines()
        if len(all_lines) != nb_edges:
            if all_lines[-1][0] == "\n":
                print(f"Incorrect file format for {file} : Remove the empty lines at the end of the file")
                return None
            print(f"Incorrect file format for {file} : The actual number of edges does not correspond to supposed number of edges")
            return None
        
        vertices = [i for i in range(nb_vertices)]
        edges = set()
        weights = {}
        for i in range(0, len(all_lines)):
            all_lines[i] = all_lines[i].split()

            # Checking format validity
            if len(all_lines[i]) != 3:
                print(f"Incorrect file format for {file} : the line {i+2} is not in a valid format")
                return None
            try:
                vertex1 = int(all_lines[i][0])
                vertex2 = int(all_lines[i][1])
                weight = float(all_lines[i][2])
            except:
                print(f"Incorrect file format for {file} : the line {i+2} is not in a valid format")
                return None
            
            # Checking values validity
            if vertex1 < 0 or vertex1 >= nb_vertices:
                print(f"Incorrect file format for {file} : in line {i+2}, the first vertex does not exist")
                return None
            if vertex2 < 0 or vertex2 >= nb_vertices:
                print(f"Incorrect file format for {file} : in line {i+2}, the second vertex does not exist")
                return None
            if (vertex1, vertex2) in edges:
                print(f"Incorrect file format for {file} : in line {i+2}, the edge already exists")
                return None
            
            edges.add((vertex1, vertex2))
            weights[(vertex1, vertex2)] = weight

    return (nb_vertices, nb_edges, vertices, edges, weights)





graph1 = readFile("Graphs/test_graph.txt")

print(graph1)