from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from app.store.graph_store import graph_store
from app.services.data_loader import load_all_graphs
from app.api import recommendations

load_dotenv()  # loading .env file

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Graph is loading...")
    load_all_graphs(graph_store)
    graph_store.is_ready = True
    print("Ready!")
    yield

app = FastAPI(title="Amazon Co-Purchase API", lifespan=lifespan)
app.include_router(recommendations.router, prefix="/recommend", tags=["recommend"])

@app.get("/health")
def health():
    return {"status": "ok" if graph_store.is_ready else "loading",
            "categories": list(graph_store.graphs.keys())}