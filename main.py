from Graph_class import DirectedWeightedGraph



k = 13 #Total number of graph of the form graphN.txt


def main():
    print("-------------------- MAIN MENU --------------------")

    run = 1    
    while run == 1:
        print("- Enter 0 : EXIT")
        print("- Enter 1 : CHOOSE A GRAPH")
        run = input()
        if not run.isdigit():
            print("Incorrect input")
            run = 1
        elif int(run) != 0 and int(run) != 1:
            print("Incorrect input")
            run = 1
        else:
            run = int(run)
            if run == 1:
                num_graph = input("Choose the number of the graph : ")
                if not num_graph.isdigit():
                    print("Incorrect input")
                else:
                    num_graph = int(num_graph)
                    if num_graph < 1 or num_graph > k:
                        print("Incorrect input")
                    else:

                        graph = DirectedWeightedGraph()
                        graph.readFile(f'./Graphs/graph{num_graph}.txt')

                        print()
                        print(f"                          GRAPH {num_graph}")
                        print()
                        graph.display_graph()

                        list_L, list_P = graph.floydWarshall()


                        # Printing in a good-looking way the matrices L and P at each step
                        for i in range(graph.nb_vertices + 1): # the number of iteration
                            print(f"Iteration {i}")
                            print()
                            print(f" "*10, end="")
                            w = 5
                            for v in range(graph.nb_vertices):
                                print(f"{'':>{(w+1)//2 - len(str(v))//2 - 1}}", end="")
                                print(str(v), end="")
                                print(f"{'':>{w - (w+1)//2 -len(str(v))//2}}", end="")

                            print(" "*14, end="")

                            for v in range(graph.nb_vertices):
                                print(f"{'':>{(w+1)//2 - len(str(v))//2 - 1}}", end="")
                                print(str(v), end="")
                                print(f"{'':>{w - (w+1)//2 -len(str(v))//2}}", end="")
                            print()

                            print(" "*9 + "+" + "-"*(w*graph.nb_vertices) + "+" + " "*12 + "+" + "-"*(w*graph.nb_vertices) + "+")

                            for v in range(graph.nb_vertices):
                                if v+1 == (graph.nb_vertices + 1)//2:
                                    print(" L :", end="")
                                else:
                                    print("    ", end="")

                                print(f"{str(v):>{4}} |", end="")
                                for elem in range(graph.nb_vertices):
                                    weight = list_L[i][v][elem]
                                    size = len(str(weight))
                                    print(f"{'':>{(w-size)//2}}", end="")
                                    print(str(weight), end="")
                                    print(f"{'':>{(w-size)//2 + (size+1)%2}}", end="")
                                
                                print("|   ", end="")
                                if v+1 == (graph.nb_vertices + 1)//2:
                                    print(" P :", end="")
                                else:
                                    print("    ", end="")
                                
                                print(f"{str(v):>{4}} |", end="")
                                for elem in range(graph.nb_vertices):
                                    path = list_P[i][v][elem]
                                    size = len(str(path))
                                    print(f"{'':>{(w-size)//2}}", end="")
                                    print(str(path), end="")
                                    print(f"{'':>{(w-size)//2 + (size+1)%2}}", end="")
                                print("|")
                            print(" "*9 + "+" + "-"*(w*graph.nb_vertices) + "+" + " "*12 + "+" + "-"*(w*graph.nb_vertices) + "+")
                            print("\n")
                


if __name__ == "__main__":
    main()