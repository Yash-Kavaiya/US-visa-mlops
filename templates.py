import os
from pathlib import Path
import time
from tqdm import tqdm

# Ask for project name
project_name = input("Enter the project name: ")

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

start_time = time.time()

for filepath in tqdm(list_of_files, desc="Processing files"):
    filepath = Path(filepath)
    filedir = filepath.parent

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create .gitkeep file in empty directories
    if not any(filedir.iterdir()):
        with open(filedir / '.gitkeep', 'w') as f:
            pass

    # Create empty files if they don't exist or are empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            print(f"Created file: {filepath}")
    else:
        print(f"File already exists: {filepath}")

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.2f} seconds")
