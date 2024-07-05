from svg_concat.file_discovery.file_criteria.criterion import Criterion


class MockCriterion(Criterion):
    def __init__(self, result: bool = True):
        self.result = result

    def __eq__(self, other):
        return self.result == other.result

    def __hash__(self):
        return hash(self.result)

    def is_valid(self, file_name: str) -> bool:
        return self.result
