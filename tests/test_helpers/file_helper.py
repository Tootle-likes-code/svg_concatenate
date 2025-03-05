import os
from pathlib import Path


def get_path(file_path: str) -> Path:
    if "tests" in os.getcwd():
        return Path(file_path)
    else:
        return Path(f"tests/{file_path}")
