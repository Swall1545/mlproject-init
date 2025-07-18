# S. Wallace
# mlproject_init.py

import os
import argparse
from pathlib import Path

# Template string for the README file with placeholders for project name
README_TEMPLATE = """# {project_name} - Machine Learning Project

This project follows a modular, reproducible ML pipeline structure.

## Project Structure

```
{project_name}/
├── README.md
├── requirements.txt or environment.yml
├── config.yaml
├── .env.example
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── model.py
│   ├── features.py
│   └── api_client.py
├── app/
│   └── main.py
├── data/
├── scripts/
│   └── (helper scripts or cron jobs)
├── docker/
│   └── Dockerfile
└── mlruns/ or wandb/
```

## Descriptions
- `README.md`: Project overview and instructions
- `requirements.txt`: Python dependencies
- `config.yaml`: Model and runtime configuration
- `notebooks/`: EDA and prototyping
- `src/`: Modular Python scripts
- `app/`: FastAPI or Streamlit frontend
- `data/`: Local data files
- `scripts/`: Automation or download scripts
- `docker/`: Containerization setup
- `mlruns/`: MLflow tracking logs

## Dependencies
- Python 3.8+
- See `requirements.txt` for full list

To install dependencies:
```bash
pip install -r requirements.txt
```
Or, if using Conda:
```bash
conda create -n myenv --file requirements.txt
conda activate myenv
```
"""
ENV_TEMPLATE = """# Secrets and access
API_KEY=your_api_key_here

# Project configuration
MODEL_TYPE=xgboost
ENVIRONMENT=dev
DEBUG=True
USE_GPU=False
EXPERIMENT_NAME={project_name}
LOG_LEVEL=INFO
"""

# Folders to be created in the project
FOLDERS = [
    "notebooks", "src", "app", "data", "scripts", "docker", "mlruns"
]

# TEMPLATE: Files to be created and their default contents
FILES = {
    # README Content generated from README_TEMPLATE, formatted with the project name argument
    "README.md": None,
    "requirements.txt": "pandas\nnumpy\nscikit-learn\nxgboost\nmlflow\nfastapi\n", # Default
    "config.yaml": "model:\n  type: xgboost\n  learning_rate: 0.1\n",   # Default
    ".env.example": """ # Secrets and access
    API_KEY=your_api_key_here
    
    # Project configuration
    MODEL_TYPE=xgboost
    ENVIRONMENT=dev
    DEBUG=True
    USE_GPU=False
    EXPERIMENT_NAME={project_name}
    LOG_LEVEL=INFO
    """,
    "src/train.py": "# Train script placeholder",
    "src/evaluate.py": "# Evaluate script placeholder",
    "src/predict.py": "# Predict script placeholder",
    "src/model.py": "# Model definitions",
    "src/features.py": "# Feature engineering",
    "src/api_client.py": "# External API interface",
    "app/main.py": "# FastAPI or Streamlit app",
    "notebooks/eda.ipynb": "",
    "docker/Dockerfile": "# Base Dockerfile"
}

# Main function to generate the entire project scaffold
def init_project(name: str, path: str):
    """
        Creates a fully scaffolded machine learning project folder.

        Args:
            name (str): Name of the project folder to create.
            path (str): Destination path where the project will be created.

        Returns:
            None
        """
    root = Path(path) / name  # Combine path and name into a full directory path
    print(f"Creating project in: {root.resolve()}")
    root.mkdir(parents=True, exist_ok=True)  # Create the main project folder

    for folder in FOLDERS:
        (root / folder).mkdir(parents=True, exist_ok=True)  # Create subfolders

    for rel_path, content in FILES.items():
        full_path = root / rel_path  # Full path to file
        full_path.parent.mkdir(parents=True, exist_ok=True)  # Make sure folder exists
        with open(full_path, "w") as f:
            if rel_path == "README.md":
                f.write(README_TEMPLATE.format(project_name=name))  # Insert dynamic README
            elif rel_path == ".env.example":        # Insert dynamic Environmental Var (.env)
                f.write(ENV_TEMPLATE.format(project_name=name))
            else:
                f.write(content or "")  # Write placeholder or empty file

    print("Project structure generated successfully.")

# Entry point function for CLI execution
def init_project_cli():
    """Wrapper function for CLI execution via setup.py"""
    parser = argparse.ArgumentParser(description="Create a standard ML project structure.")
    parser.add_argument("--name", type=str, required=True, help="Project folder name")
    parser.add_argument("--path", type=str, default=".", help="Destination path")
    args = parser.parse_args()  # Parse CLI arguments
    init_project(args.name, args.path)  # Call main scaffold function

# Run directly from command line = not imported
if __name__ == "__main__":
    init_project_cli()  # Launch CLI entry point