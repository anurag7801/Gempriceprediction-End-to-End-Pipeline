import os
from pathlib import Path


list_of_files = [
    ".gihub/workflows/ci.yaml",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_evaluation.py",
    "src/components/model_trainer.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "src/logger/__init__.py",
    "src/logger/logging.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/pipeline/__init__.py",
    "src/pipeline/prediction_pipeline.py",
    "src/pipeline/training_pipeline.py",
    "templates/index.html",
    "tests/integration/__init__.py",
    "tests/unit/__init__.py",
    "app.py",
    "init_setup.sh",
    "pyproject.toml",
    "requirements_dev.txt",
    "requirements.txt",
    "setup.cfg",
    "setup.py",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #create an empty file