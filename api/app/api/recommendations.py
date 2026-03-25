from fastapi import APIRouter, HTTPException, Query
from app.store.graph_store import graph_store
from app.services.recommend_service import get_recommendations, SCORERS

router = APIRouter()

@router.get("/{asin}")
def recommend(
    asin: str,
    category: str = Query(..., description="Electronics / All_Beauty / Home_and_Kitchen"),
    algorithm: str = Query("AA", description="CN / Jaccard / AA / PA"),
    top_k: int = Query(10, ge=1, le=100),
):
    if category not in graph_store.graphs:
        raise HTTPException(404, detail=f"No category: {category}")
    G = graph_store.graphs[category]
    if asin not in G.nodes:
        raise HTTPException(404, detail=f"No asin: {asin}")
    results = get_recommendations(G, asin, algorithm, top_k)
    return {"asin": asin, "category": category, "algorithm": algorithm, "recommendations": results}