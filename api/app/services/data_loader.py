import os, gzip, json
from collections import defaultdict
from itertools import combinations
import numpy as np
import pandas as pd
import networkx as nx
from app.store.graph_store import GraphStore

DATA_DIR = os.getenv("DATA_DIR", "./data")

# From Colab

def load_partial_json(path, max_lines=100000):
    data = []
    with gzip.open(path, 'rb') as f:
        for i, line in enumerate(f):
            if i >= max_lines:
                break
            data.append(json.loads(line))
    return pd.DataFrame(data)

def build_copurchase_graph(df, min_weight=2):
    user_reviews = defaultdict(set)
    for _, row in df.iterrows():
        user_reviews[row['reviewerID']].add(row['asin'])
    edge_weights = defaultdict(int)
    for products in user_reviews.values():
        if len(products) < 2:
            continue
        for a, b in combinations(sorted(products), 2):
            edge_weights[(a, b)] += 1
    G = nx.Graph()
    for (a, b), w in edge_weights.items():
        if w >= min_weight:
            G.add_edge(a, b, weight=w)
    return G

def extract_gcc(G):
    if G.number_of_nodes() == 0:
        return G.copy()
    if nx.is_connected(G):
        return G
    gcc_nodes = max(nx.connected_components(G), key=len)
    return G.subgraph(gcc_nodes).copy()

# for FastAPI

def load_all_graphs(store: GraphStore):
    categories = {
        "Electronics":      "Electronics_5.json.gz",
        "All_Beauty":       "All_Beauty_5.json.gz",
        "Home_and_Kitchen": "Home_and_Kitchen_5.json.gz",
    }
    for name, filename in categories.items():
        path = os.path.join(DATA_DIR, filename)
        print(f"Loading: {name} ...")
        df = load_partial_json(path)
        G  = build_copurchase_graph(df)
        store.graphs[name] = extract_gcc(G)
        print(f"{name} Complete - Node #: {store.graphs[name].number_of_nodes()}")