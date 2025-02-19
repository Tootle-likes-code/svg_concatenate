from abc import ABC, abstractmethod
from pathlib import Path


class Filter(ABC):
    @classmethod
    @abstractmethod
    def create_dummy_instance(cls):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def is_valid(self, file_name: Path) -> bool:
        pass

    @abstractmethod
    def merge(self, other_filter: "Filter") -> None:
        pass

    @abstractmethod
    def to_json(self) -> dict:
        pass
