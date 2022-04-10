import pandas as pd
from os.path import exists
import networkx as nx
import numpy as np

def bipartite_graph(track_path,artist_path,df):
    if not exists(track_path):
        track_df = df.copy()
        track_df.drop(['count', 'userid'], axis = 1, inplace=True)
        track_df.drop_duplicates('track-id', inplace=True)
        track_df.reset_index(drop=True, inplace=True)
        track_df.to_csv(track_path)
    else : 
        track_df = pd.read_csv(track_path, index_col=0)

    if not exists(artist_path):
        artist_df = df.copy()
        artist_df.drop(['count', 'userid', 'track-name', 'track-id'], axis = 1, inplace=True)
        artist_df.drop_duplicates('artist-id', inplace=True)
        artist_df.reset_index(drop=True, inplace=True)
        artist_df.to_csv(artist_path)
    else : 
        artist_df = pd.read_csv(artist_path, index_col=0)
    return track_df,artist_df

def graph_generator(user_track_edges,track_artist_edges,user,track,artist):

    #We generate the bipartite graph
    G= nx.Graph()
    edges_1 = np.array(user_track_edges[['userid', 'track-id','count']].values)
    edges_2 = np.array(track_artist_edges[['artist-id', 'track-id']].values)
    G.add_nodes_from(user['#id'], bipartite=0)
    G.add_nodes_from(track['track-id'], bipartite=1)
    G.add_nodes_from(artist['artist-id'], bipartite=2)
        
    G.add_weighted_edges_from(edges_1)
    #weighted graph
    G.add_edges_from(edges_2)
    return G

# We can remove artist with no more edges
def remove_low_degree_nodes(test_graph, train_graph, val_graph,test_gt_graph):
    tst_graph, t_graph, v_graph ,tst_gt_graph= test_graph.copy(), train_graph.copy(), val_graph.copy(),test_gt_graph.copy()
    to_be_removed = []
    for  x, d in t_graph.nodes(data=True):
        try:
            if d['bipartite'] != 2:
                if t_graph.degree(x) <= 3:
                    to_be_removed.append(x)
        except:
            to_be_removed.append(x)
    t_graph.remove_nodes_from(to_be_removed)
    v_graph.remove_nodes_from(to_be_removed)
    tst_graph.remove_nodes_from(to_be_removed)
    tst_gt_graph.remove_nodes_from(to_be_removed)
    return tst_graph, t_graph, v_graph,tst_gt_graph

# We can remove artist with no more edges
def remove_low_artists(test_graph, train_graph, val_graph,test_gt_graph):
    tst_graph, t_graph, v_graph ,tst_gt_graph= test_graph.copy(), train_graph.copy(), val_graph.copy(),test_gt_graph.copy()
    to_be_removed = [x for  x, d in t_graph.nodes(data=True) if (t_graph.degree(x) ==0 and d['bipartite'] == 2)]
    t_graph.remove_nodes_from(to_be_removed)
    v_graph.remove_nodes_from(to_be_removed)
    tst_graph.remove_nodes_from(to_be_removed)
    tst_gt_graph.remove_nodes_from(to_be_removed)
    return tst_graph, t_graph, v_graph,tst_gt_graph