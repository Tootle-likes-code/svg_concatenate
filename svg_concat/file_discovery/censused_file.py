from dataclasses import dataclass
from pathlib import Path


@dataclass
class CensusedFile:
    name: str
    path: Path

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash(self.path)
