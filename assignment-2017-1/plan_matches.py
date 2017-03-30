input_filename = "graph_file.txt"

g = {}
lines = 0
with open(input_filename) as graph_input:
    for line in graph_input:
        lines = lines +1
        nodes = [str(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
m = {}
for i in range(0,lines):
    m[i]=[]

print m, g

for key in g:
    for i in g[key]:
        print i + key