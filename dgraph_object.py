from dataclasses import dataclass
import math
import matplotlib.pyplot as plot
import numpy as np
import random


@dataclass
class dGraph:
    edges : list
    nodes : int
    transfers_from : list
    transfers_to : list


def transfers_from_nodes(weighted_dgraph):
    node_count = weighted_dgraph.nodes
    final_list = []
    for i in range(node_count):
        connecting_edges = []
        for j in weighted_dgraph.edges:
            if j[0] == i:
                connecting_edges.append(j)
        final_list.append(connecting_edges)
    weighted_dgraph.transfers_from = final_list

def transfers_to_nodes(weighted_dgraph):
    node_count = weighted_dgraph.nodes
    final_list = []
    for i in range(node_count):
        connecting_edges = []
        for j in weighted_dgraph.edges:
            if j[1] == i:
                connecting_edges.append(j)
        final_list.append(connecting_edges)
    weighted_dgraph.transfers_to = final_list

def edge_to_index(weighted_dgraph, tf_edge_list, node):
    final_list = []
    node_component = tf_edge_list[node]
    for i in node_component:
        location_index = weighted_dgraph.edges.index(i)
        final_list.append(location_index)
    return final_list

