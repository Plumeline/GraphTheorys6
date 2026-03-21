from Graph_class import DirectedWeightedGraph



k = 14 #Total number of graph of the form graphN.txt


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
                            w = 5 #Must be odd
                            for v in range(graph.nb_vertices):
                                size = len(str(v))
                                print(f"{'':>{(w-size)//2}}", end="")
                                print(str(v), end="")
                                print(f"{'':>{(w-size)//2 + (size+1)%2}}", end="")

                            print(" "*14, end="")

                            for v in range(graph.nb_vertices):
                                size = len(str(v))
                                print(f"{'':>{(w-size)//2}}", end="")
                                print(str(v), end="")
                                print(f"{'':>{(w-size)//2 + (size+1)%2}}", end="")
                            print()

                            print(" "*9 + "+" + "-"*(w*graph.nb_vertices) + "+" + " "*12 + "+" + "-"*(w*graph.nb_vertices) + "+")

                            for v in range(graph.nb_vertices):
                                if v+1 == (graph.nb_vertices + 1)//2:
                                    print(" L :", end="")
                                else:
                                    print("    ", end="")

                                print(" "*(4-len(str(v))) + str(v) + " |", end="")
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
                                
                                print(" "*(4-len(str(v))) + str(v) + " |", end="")
                                for elem in range(graph.nb_vertices):
                                    path = list_P[i][v][elem]
                                    size = len(str(path))
                                    print(f"{'':>{(w-size)//2}}", end="")
                                    print(str(path), end="")
                                    print(f"{'':>{(w-size)//2 + (size+1)%2}}", end="")
                                print("|")
                            print(" "*9 + "+" + "-"*(w*graph.nb_vertices) + "+" + " "*12 + "+" + "-"*(w*graph.nb_vertices) + "+")
                            print("\n")

                        if (graph.has_absorbant_cycle(list_L[len(list_L)-1])):
                            print(" This graph contains at least one absorbant cycle ! \n \n")
                        else:
                            print (" This graph contains no absorbant cycle. \n \n")
                        
                        if num_graph == 14:
                            print("Correspondance table :")
                            len_str = 30
                            list_correspondance = [(0, "Kuala Lumpur (Malaysia)"), (1, "Penang (Malaysia)"), (2, "Ipoh (Malaysia)"), (3, "Johor Bahru (Malaysia)"), (4, "Singapore (Singapore)"),
                                                    (5, "Melaka (Malaysia)"), (6, "Bangkok (Thailand)"), (7, "Hat Yai (Thailand)"), (8, "Kuantan (Malaysia)"), (9, "Kuala Terengganu (Malaysia)"),
                                                    (10, "Kota Bharu (Malaysia)"), (11, "Alor Setar (Malaysia)"), (12, "Phuket (Thailand)"), (13, "Surat Thani (Thailand)"), (14, "Hua Hin (Thailand)")]
                            print("_"*(13 + len_str))
                            print("| Vertex : |" + " "*(((len_str-5))//2) + "Place" + " "*((len_str-5)//2) + " |")
                            for corr in list_correspondance:
                                print(
                                    "|" + " " * ((11 - len(str(corr[0]))) // 2) + str(corr[0]) +
                                    " " * (10 - len(str(corr[0])) - ((11 - len(str(corr[0]))) // 2)) + "|" +
                                    " " * ((len_str - len(corr[1])) // 2) + corr[1] +
                                    " " * ((len_str - len(corr[1]) + 1) // 2) + "|")
                            print("_"*(13 + len_str))
                                




if __name__ == "__main__":

    #if you want to update execution_traces, or re-create the files, just set this to True and run the main
    execution_traces = False 



    if execution_traces :

        for graph_num in range (1, k+1):
        
            graph = DirectedWeightedGraph()
            graph.readFile(f"./Graphs/graph"+ str(graph_num) + ".txt")
            list_L, list_P = graph.floydWarshall()

            with open("./Exec_traces/graph"+ str(graph_num) + ".txt", "w", encoding="utf-8") as g:
                for i in range(graph.nb_vertices + 1): # the number of iteration
                                g.write(f"Iteration {i} \n")

                                g.write(f" "*10)
                                w = 5
                                for v in range(graph.nb_vertices):
                                    g.write(f"{'':>{(w+1)//2 - len(str(v))//2 - 1}}")
                                    g.write(str(v))
                                    g.write(f"{'':>{w - (w+1)//2 -len(str(v))//2}}")

                                g.write(" "*14)

                                for v in range(graph.nb_vertices):
                                    g.write(f"{'':>{(w+1)//2 - len(str(v))//2 - 1}}")
                                    g.write(str(v))
                                    g.write(f"{'':>{w - (w+1)//2 -len(str(v))//2}}")
                                g.write("\n\n")

                                g.write(" "*9 + "+" + "-"*(w*graph.nb_vertices) + "+" + " "*12 + "+" + "-"*(w*graph.nb_vertices) + "+" + "\n")

                                for v in range(graph.nb_vertices):
                                    if v+1 == (graph.nb_vertices + 1)//2:
                                        g.write(" L :")
                                    else:
                                        g.write("    ")

                                    g.write(" "*(4-len(str(v))) + str(v) + " |")
                                    for elem in range(graph.nb_vertices):
                                        weight = list_L[i][v][elem]
                                        size = len(str(weight))
                                        g.write(f"{'':>{(w-size)//2}}")
                                        g.write(str(weight))
                                        g.write(f"{'':>{(w-size)//2 + (size+1)%2}}")
                                    
                                    g.write("|   ")
                                    if v+1 == (graph.nb_vertices + 1)//2:
                                        g.write(" P :")
                                    else:
                                        g.write("    ")
                                    
                                    g.write(" "*(4-len(str(v))) + str(v) + " |")
                                    for elem in range(graph.nb_vertices):
                                        path = list_P[i][v][elem]
                                        size = len(str(path))
                                        g.write(f"{'':>{(w-size)//2}}")
                                        g.write(str(path))
                                        g.write(f"{'':>{(w-size)//2 + (size+1)%2}}")
                                    g.write("|\n")
                                g.write(" "*9 + "+" + "-"*(w*graph.nb_vertices) + "+" + " "*12 + "+" + "-"*(w*graph.nb_vertices) + "+\n")
                                g.write("\n")

                                if (graph.has_absorbant_cycle(list_L[len(list_L)-1])):
                                    g.write(" This graph contains at least one absorbant cycle ! \n \n")
                                else:
                                    g.write (" This graph contains no absorbant cycle. \n \n")



    main()

    