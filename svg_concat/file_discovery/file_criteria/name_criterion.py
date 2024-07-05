from svg_concat.file_discovery.file_criteria.criterion import Criterion


def create_criterion(file_names):
    if file_names is None or len(file_names) == 0:
        return

    return NameCriterion(file_names)


class NameCriterion(Criterion):
    def __init__(self, names: list[str]):
        self.names = names

    def is_valid(self, file_name: str) -> bool:
        if file_name in self.names:
            return True

        return False
