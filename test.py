import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism as iso

LTAcore = open("LTAcore.adjlist", 'rb')
LTA = open("LTA.adjlist", 'rb')
OWE = open("OWE.adjlist", 'rb')
M = open("M.adjlist", 'rb')

LTAcore=nx.read_adjlist(LTAcore)
OWE=nx.read_adjlist(OWE)
LTA = nx.read_adjlist(LTA)
M = nx.read_adjlist(M)

GM = iso.GraphMatcher(LTA,LTAcore)
print(GM.is_isomorphic())

# print(nx.is_isomorphic(LTAcore,LTA))

# nx.draw(LTAcore)
# nx.draw_random(LTAcore)
# nx.draw_circular(LTAcore)
# nx.draw_spectral(LTAcore)
# plt.show()