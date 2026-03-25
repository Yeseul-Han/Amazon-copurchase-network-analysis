import numpy as np
import networkx as nx
from typing import List, Dict

def score_cn(G, u, v):
    return float(len(set(G[u]) & set(G[v])))

def score_jaccard(G, u, v):
    n_u, n_v = set(G[u]), set(G[v])
    union = n_u | n_v
    return len(n_u & n_v) / len(union) if union else 0.0

def score_aa(G, u, v):
    return sum(1 / np.log(len(G[z]))
               for z in set(G[u]) & set(G[v]) if len(G[z]) > 1)

def score_pa(G, u, v):
    return float(len(G[u]) * len(G[v]))

SCORERS = {"CN": score_cn, "Jaccard": score_jaccard, "AA": score_aa, "PA": score_pa}

def get_recommendations(G: nx.Graph, asin: str, algorithm: str, top_k: int) -> List[Dict]:
    if algorithm not in SCORERS:
        raise ValueError(f"Unsupportable Algorithm: {algorithm}")
    scorer = SCORERS[algorithm]
    neighbors = set(G[asin])
    candidates = set()
    for nbr in neighbors:
        candidates |= set(G[nbr])
    candidates -= neighbors
    candidates.discard(asin)
    scored = []
    for c in candidates:
        try:
            s = scorer(G, asin, c)
        except Exception:
            s = 0.0
        scored.append({"asin": c, "score": round(s, 4)})
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]