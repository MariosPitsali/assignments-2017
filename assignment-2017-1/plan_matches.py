input_filename = "graph_file.txt"
matches =[]
times = []
with open(input_filename) as graph_input:
    for line in graph_input:
        nodes = [str(x) for x in line.split()]
        for i in nodes:
            times.append(i)
        matches.append(nodes)
g = {} #graph declaration{day: matches}
def find_max(lst):
#finds max edges adjacent to a node, since it is proven max or max+1 is the max number of colours/days needed
    max = 0
    for i in lst:
        if lst.count(i)>max:
            max=lst.count(i)
    return max
length = find_max(times)
print matches
def in_graph_line(g,a,b,key):
#is any of the players playing that day?
    for pair in g[key]:
        if a in pair or b in pair:
            return True
        else:
            return False
for match in matches:
    a=match[0]
    b=match[1]
    #since we know it's exactly two opponents
    for i in range (0,max+1):
        t=i
        is_in_line = in_graph_line(g,a,b,t)
        while is_in_line:
            t = t+1
            is_in_line =in_graph_line(g,a,b,t)
        else:
            g[t].append()
            break

    



