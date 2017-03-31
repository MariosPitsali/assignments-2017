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

for day in range(0, length+1):
    g[day]=[]

def in_graph_line(g,a,b,key):
#is any of the players playing that day?
    is_there = None
    if g[key]!=[]:
        for pair in g[key]:
            print "Examines pair", pair
            if a in pair or b in pair:
                is_there = True
            else:
                is_there = False
    else:
        return False
    return is_there

for match in matches:
    a=match[0]
    print a
    b=match[1]
    print b
    #since we know it's exactly two opponents
    for i in range (0,length+1):
        t=i
        is_in_line = in_graph_line(g,a,b,t)
        print "Goes to day", t
        print is_in_line
        while is_in_line:
            t = t+1
            print "Goes to day", t
            is_in_line =in_graph_line(g,a,b,t)
            print is_in_line
        else:
            g[t].append([a, b])
            print "Graph is", g
            break
   



