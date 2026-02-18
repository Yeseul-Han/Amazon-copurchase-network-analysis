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

---
