import os
from pathlib import Path

CONFIG_PATH_IN_TEST_DIRECTORY = "test_config.json"
CONFIG_PATH_OUTSIDE_TEST_DIRECTORY = "tests/test_config.json"


def get_test_config_path_text() -> str:
    if "tests" in os.getcwd():
        return CONFIG_PATH_IN_TEST_DIRECTORY
    else:
        return CONFIG_PATH_OUTSIDE_TEST_DIRECTORY


def _get_base_folder() -> Path:
    if "tests" in os.getcwd():
        return Path()
    else:
        return Path("tests/")


def get_path_to(intended_path: str) -> Path:
    return Path(_get_base_folder()).joinpath(intended_path)
