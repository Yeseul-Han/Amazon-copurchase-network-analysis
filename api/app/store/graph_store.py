import networkx as nx
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class GraphStore:
    graphs: Dict[str, nx.Graph] = field(default_factory=dict)
    is_ready: bool = False

graph_store = GraphStore()