import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism as iso

LTAcore = open("graph/core/LTAcore.adjlist", 'rb')
UFIcore = open("graph/core/UFIcore.adjlist", 'rb')

LTA = open("graph/LTA.adjlist", 'rb')
OWE = open("graph/OWE.adjlist", 'rb')

M = open("graph/M.adjlist", 'rb')

LTAcore=nx.read_adjlist(LTAcore)
UFIcore=nx.read_adjlist(UFIcore)

OWE=nx.read_adjlist(OWE)
LTA = nx.read_adjlist(LTA)

M = nx.read_adjlist(M)

GM = iso.GraphMatcher(M,LTAcore)
print GM.subgraph_is_isomorphic()


# nx.draw(LTAcore)
# nx.draw_random(LTAcore)
# nx.draw_circular(M)
# nx.draw_spectral(LTAcore)
# plt.show()
