import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism as iso

LTAcore = open("graph/core/LTAcore.adjlist", 'rb')
UFIcore = open("graph/core/UFIcore.adjlist", 'rb')

EMTcore = open("graph/core/EMT.adjlist", 'rb')
EMT01 = open("graph/core/EMT01.adjlist", 'rb')
EMT = open("graph/EMT.adjlist", 'rb')

LTA = open("graph/LTA.adjlist", 'rb')
OWE = open("graph/OWE.adjlist", 'rb')
UFI = open("graph/UFI.adjlist", 'rb')

M = open("graph/M2.adjlist", 'rb')

LTAcore = nx.read_adjlist(LTAcore)
UFIcore = nx.read_adjlist(UFIcore)
EMTcore = nx.read_adjlist(EMTcore)

OWE = nx.read_adjlist(OWE)
LTA = nx.read_adjlist(LTA)
UFI = nx.read_adjlist(UFI)
EMT = nx.read_adjlist(EMT)
EMT01 = nx.read_adjlist(EMT01)

M = nx.read_adjlist(M)

GM = iso.GraphMatcher(EMTcore,EMT01)
print(GM.subgraph_is_isomorphic())


# nx.draw(UFI)
# nx.draw_random(UFI)
# nx.draw_circular(UFI)
# nx.draw_spectral(UFI)
# plt.show()
