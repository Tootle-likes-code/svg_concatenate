from abc import ABC, abstractmethod


class Criterion(ABC):
    @abstractmethod
    def is_valid(self, file_name:str) -> bool:
        pass
