import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism as iso

# LTAcore = nx.line_graph(nx.read_adjlist("graph/core/LTAcore.adjlist"))
LTAcore = nx.read_adjlist("graph/core/LTAcore.adjlist")
# LTA = nx.line_graph(nx.read_adjlist("graph/LTA.adjlist"))
#
# FAUcore = nx.line_graph(nx.read_adjlist("graph/core/FAUcore.adjlist"))
# FAU = nx.line_graph(nx.read_adjlist("graph/FAU.adjlist"))

# UFIcore = nx.line_graph(nx.read_adjlist("graph/core/UFIcore.adjlist"))
UFIcore = nx.read_adjlist("graph/core/UFIcore.adjlist")
UFI = nx.read_adjlist("graph/UFI.adjlist")

# EMTcore = nx.line_graph(nx.read_adjlist("graph/core/EMT.adjlist"))
# EMT = nx.line_graph(nx.read_adjlist("graph/EMT.adjlist"))

# M = nx.line_graph(nx.read_adjlist("graph/M.adjlist"))
M = nx.read_adjlist("graph/M.adjlist")
######
# TON = nx.line_graph(nx.read_adjlist("graph/TON.adjlist"))
# MTT = nx.line_graph(nx.read_adjlist("graph/MTT.adjlist"))


TON = nx.read_adjlist("graph/TON.adjlist") 
MTT = nx.read_adjlist("graph/MTT.adjlist")

GM = iso.GraphMatcher(UFI,UFIcore)

print(GM.subgraph_is_isomorphic())

# print(list(LTAcore.edges()))

# nx.draw(UFI)
# nx.draw_random(UFI)
# nx.draw_circular(UFI)
# nx.draw_spectral(UFI)
# plt.show()
