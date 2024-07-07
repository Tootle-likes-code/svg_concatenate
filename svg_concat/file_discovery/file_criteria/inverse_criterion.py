from svg_concat.file_discovery.file_criteria.criterion import Criterion


class InverseCriterion(Criterion):
    def __init__(self, base_criterion: Criterion):
        self.base_criterion = base_criterion

    def is_valid(self, file_name: str) -> bool:
        return not self.base_criterion.is_valid(file_name)
