# mlproject-init

**CLI Tool to Scaffold Reproducible Machine Learning Project Structures**

This tool generates a complete, modular ML project structure with standard folders, 
a dynamic README, and environment variable templates that is ready for local or 
cloud-based development.

---

## Features

- Create consistent, production-ready ML repo structure in seconds
- CLI-driven with `--name` and `--path` arguments
- Auto-generates:
  - `README.md` with project name and structure
  - `.env.example` with dynamic `EXPERIMENT_NAME`
  - Placeholder files for `train.py`, `evaluate.py`, `predict.py`, etc.
  - Default `config.yaml` and `requirements.txt`
- Supports future packaging, Docker, MLflow, and API integration

---

## Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/mlproject-init.git
cd mlproject-init
pip install -e .
```
After installation, you can run `mlproject-init` globally from your terminal.

---

## ⚙️ Usage

```bash
mlproject-init --name your-project-name --path /your/output/directory
```

**Example:**

```bash
mlproject-init --name air-quality --path ~/projects
```

**Resulting structure:**

```
air-quality/
├── README.md
├── .env.example
├── config.yaml
├── requirements.txt
├── src/
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── model.py
│   ├── features.py
│   └── api_client.py
├── notebooks/
│   └── eda.ipynb
├── app/
│   └── main.py
├── data/
├── scripts/
├── docker/
│   └── Dockerfile
├── mlruns/
```

---

## `.env.example` Contents

```env
# Secrets and access
API_KEY=your_api_key_here

# Project configuration
MODEL_TYPE=xgboost
ENVIRONMENT=dev
DEBUG=True
USE_GPU=False
EXPERIMENT_NAME=air-quality
LOG_LEVEL=INFO
```

---

## Why Use This Tool?

- Reuse the same ML structure across personal, academic, or client projects
- Save time scaffolding and focus on modeling
- Improve project consistency, collaboration, and maintainability
- Ideal for bootstrapping Kaggle, research, or portfolio builds

---

## Author

**S. Wallace**  


