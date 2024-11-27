from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def is_valid(self, file_name:str) -> bool:
        pass
