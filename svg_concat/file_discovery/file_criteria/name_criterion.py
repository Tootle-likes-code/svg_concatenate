from criterion import Criterion


class NameCriterion(Criterion):
    def __init__(self, names: list[str]):
        self.names = names

    def is_valid(self, file_name: str) -> bool:
        if file_name in self.names:
            return True

        return False
