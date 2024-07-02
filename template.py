import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/data_loader.py",
    f"{project_name}/data_preprocessor.py",
    f"{project_name}/model_saver.py",  
    f"{project_name}/model_loader.py",
    f"{project_name}/model_trainer.py",
    f"{project_name}/recommender.py",
    "app.py",
    "test.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]




for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")