# Livo AI RAG Evaluation - Golden Dataset

<p align="center">
  <img src="https://img.shields.io/badge/assignment-Option%20B-blue" alt="Assignment Option B" />
  <img src="https://img.shields.io/badge/difficulty-Intermediate-blue" alt="Difficulty" />
  <img src="https://img.shields.io/badge/language-Python-blue" alt="Language" />
  <img src="https://img.shields.io/badge/status-Complete-green" alt="Status" />
</p>

This repository contains a **Golden Dataset for RAG (Retrieval-Augmented Generation) Evaluation** submitted as part of the **Livo AI SWE Intern Assessment** (Option B: Golden Dataset for RAG).

---

## Why I'm Interested in Livo AI

I'm drawn to Livo AI because of the intersection of technology and business impact. Livo AI builds AI products and automation systems for real clients across CA firms, pharma companies, insurance players, and nonprofits. This means my work would directly impact:

- **Document Processing Pipelines**: Automating the extraction, classification, and routing of large volumes of business documents.
- **Enterprise Search**: Building intelligent search systems that help organizations find information faster.
- **Agentic Systems**: Creating AI agents that can autonomously handle multi-step workflows.
- **Client-Facing Portals**: Developing web applications that directly serve end-users.

**This assignment resonated with me because it combines technical depth with business relevance.** The RAG evaluation demonstrates:
1. Understanding of core AI/ML concepts (neural networks, transformers)
2. Practical evaluation methodology (precision, recall, F1, MRR, NDCG)
3. Production-ready code quality

---

## Project Structure

```
livo-ai-rag-evaluation/
├── README.md                  # This file
├── qa_dataset.json            # Golden dataset with QA pairs
├── evaluator.py               # RAG evaluation script
├── rag_evaluator.py           # Full RAG evaluator with embedding
├── requirements.txt           # Python dependencies
├── config.yaml                # Configuration file
├── results/
│   └── evaluation_results.json  # Evaluation results
├── visualizations/
│   └── metrics_dashboard.png   # Visual dashboard
└── docs/
    ├── Livo_AI_RAG_Golden_Dataset.pdf  # Submission PDF
    └── metrics_dashboard.png
```

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/livo-ai-rag-evaluation.git
cd livo-ai-rag-evaluation

# Install dependencies
pip install -r requirements.txt

# Run evaluation
python3 evaluator.py

# View results
cat results/evaluation_results.json
```

---

## QA Dataset Overview

The dataset contains **5 carefully curated question-answer pairs** from educational videos on neural networks and deep learning:

| ID | Topic | Source | Difficulty |
|----|-------|--------|------------|
| qa_001 | Activation Functions & 3Blue1Brown - Neural Networks | Foundational |
| qa_002 | Attention Mechanism | 3Blue1Brown - Transformers | Advanced |
| qa_003 | Image Processing | 3Blue1Brown - Neural Networks | Foundational |
| qa_004 | ML vs Deep Learning | CampusX (Hindi) | Intermediate |
| qa_005 | Self-Attention | 3Blue1Brown - Transformers | Advanced |

---

## Technical Implementation

### RAG Evaluator Features

- **TF-IDF Embedding**: Lightweight document embedding for retrieval
- **Cosine Similarity**: Semantic matching between queries and documents
- **Evaluation Metrics**: Precision, Recall, F1-Score, MRR, NDCG
- **Multi-source Support**: Works with any JSON dataset
- **Visualization**: Automatic metric dashboard generation

### Configuration

Edit `config.yaml` to customize:
- Number of top documents to retrieve
- Embedding model settings
- Output paths

---

## Evaluation Metrics Explained

| Metric | Description | Range |
|--------|-------------|-------|
| Precision | Fraction of retrieved docs that are relevant | 0-1 |
| Recall | Fraction of relevant docs that were retrieved | 0-1 |
| F1-Score | Harmonic mean of precision and recall | 0-1 |
| MRR | Mean Reciprocal Rank | 0-1 |
| NDCG | Normalized Discounted Cumulative Gain | 0-1 |

---

## Videos Covered

| Video | Channel | Topic | Questions |
|------|--------|-------|---------|
| [But what is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk) | 3Blue1Brown | Neural Networks | 2 |
| [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) | 3Blue1Brown | Transformers | 2 |
| [What is Deep Learning?](https://www.youtube.com/watch?v=fHF22Wxuyw4) | CampusX | Deep Learning (Hindi) | 1 |

---

## Contact

**Name**: Manish Bhakti Sagar
**Email**: manishbhakti881@gmail.com
**LinkedIn**: [https://www.linkedin.com/in/manish-bhakti-sagar-823404234/]  
**GitHub**: [https://github.com/Manish881-hub]

---

## License

MIT License - Feel free to use this code for your own projects.
