import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism as iso
import time

def createMolecular(name, core=False):
    ##get connecting file
    if(core):
        f = open("graph/core/" + name +"core.adjlist")
    else:
        f = open("graph/"+name+".adjlist")
    ##get node count
    datas = f.readlines()
    node_Num = len(datas)
    ##create all nodes
    G=nx.Graph()
    for i in range(node_Num):
      G.add_node(i+1)
    ##create all bonds
    for line in datas:
        data = line.split()
        fromNode = int(data[0])
        for num in data[1:]:
            toNode = int(num)
            G.add_edge(fromNode,toNode)
    return G


Mgraph = nx.line_graph(createMolecular("MTT2"))
subGraph = nx.line_graph(createMolecular("TON"))

start =time.clock()
GM = iso.GraphMatcher(Mgraph,subGraph)
print(GM.subgraph_is_isomorphic())
end = time.clock()
print('Running time: %s Seconds'%(end-start))
# nx.draw(MTT)
# nx.draw_random(MTT)
# nx.draw_circular(MTT)
# nx.draw_spectral(LTAcore)
# plt.show()
