input_filename = "graph_file.txt"

g = {}
with open(input_filename) as graph_input:
    for line in graph_input:
        # split line and convert line parts to integers
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        # if a node is not already in the graph
        # we must create a new empty list 
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        # we need to append the "to" node
        # to the existing list for the "from" node
        g[nodes[0]].append(nodes[1])
