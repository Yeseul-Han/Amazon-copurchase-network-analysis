# Time-Aware Link Prediction on Amazon Co-Purchase Networks

This project implements a **Time-Aware Link Prediction** framework to predict future product associations in Amazon's co-purchase network. Unlike static graph analysis, this approach strictly respects chronological order to prevent information leakage, providing a more realistic evaluation for recommendation systems.

## Key Features
- **Temporal Splitting**: Implemented a strict cutoff-time based split using review timestamps to simulate real-world future prediction.
- **Graph Construction**: Built product graphs from Amazon "5-core" metadata (Electronics, Home & Kitchen, All Beauty).
- **Network Analysis**: Extracted the Largest Connected Component (LCC) and analyzed graph density and connectivity.
- **Baseline Modeling**: Evaluated four classical link prediction algorithms:
  - Adamic-Adar (AA)
  - Common Neighbors (CN)
  - Jaccard Coefficient
  - Preferential Attachment (PA)

## Methodology
- **Nodes**: Individual products (ASINs).
- **Edges**: Formed when products are frequently reviewed together by the same users.
- **Weights**: Co-occurrence frequency derived from timestamps.
- **Evaluation Metrics**: Average Precision (AP), Area Under Curve (AUC), and Precision@100.

## Results Summary
The **Adamic-Adar (AA)** and **Common Neighbors (CN)** models showed the most stable performance across categories. Specifically, the 'Home & Kitchen' category achieved a **Precision@100 of 0.92**, demonstrating high accuracy in predicting top-tier product recommendations.

| Category | Model | AP | AUC | P@100 |
| :--- | :--- | :--- | :--- | :--- |
| Electronics | AA | 0.76 | 0.70 | 0.91 |
| Home & Kitchen | PA | 0.77 | 0.77 | 0.92 |

## Tech Stack
- **Language**: Python (Google Colab)
- **Libraries**: NetworkX, Pandas, NumPy, Matplotlib
- **Dataset**: Amazon Product Review Dataset

## Contributors
- Yeseul Han
- Xi Lu
- Erfan YousefMoumji
  
## API Service

This project has been extended into a production-style RESTful API service using FastAPI.

### Additional Tech Stack
- **Backend**: FastAPI, Uvicorn
- **Architecture**: In-memory graph loading at startup for fast response

### Project Structure
```
├── notebook/
│   └── Amazon_CoPurchase_Network_Analysis.ipynb  # Original analysis (Google Colab)
├── api/                                           # FastAPI backend service
│   ├── app/
│   │   ├── main.py                  # App entry point, graph loading on startup
│   │   ├── api/
│   │   │   └── recommendations.py   # Recommendation endpoints
│   │   ├── services/
│   │   │   ├── data_loader.py       # Data loading & graph construction
│   │   │   └── recommend_service.py # CN / Jaccard / AA / PA algorithms
│   │   └── store/
│   │       └── graph_store.py       # In-memory graph store
│   ├── .env.example
│   └── requirements.txt
└── README.md
```

### Getting Started
```bash
cd api
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API documentation.

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/recommend/{asin}` | Get Top-K product recommendations |
| GET | `/health` | Server health check |

### Example
```bash
curl -X GET "http://localhost:8000/recommend/B00000J3II?category=Electronics&algorithm=AA&top_k=5"
```
```json
{
  "asin": "B00000J3II",
  "category": "Electronics",
  "algorithm": "AA",
  "recommendations": [
    { "asin": "B00005AT7Y", "score": 1.4427 },
    { "asin": "B0000300QQ", "score": 1.2795 }
  ]
}
```
---
