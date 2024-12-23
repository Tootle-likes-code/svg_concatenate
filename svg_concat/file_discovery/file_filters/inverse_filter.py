from svg_concat.file_discovery.file_filters.filter import Filter


class InverseFilter(Filter):
    def __init__(self, base_criterion: Filter):
        self.base_criterion = base_criterion

    @classmethod
    def create_dummy_instance(cls):
        return InverseFilter(None)

    def __eq__(self, other):
        if not isinstance(other, InverseFilter):
            return False

        return self.base_criterion == other.base_criterion

    def is_valid(self, file_name: str) -> bool:
        return not self.base_criterion.is_valid(file_name)

    def merge(self, other_filter: "Filter") -> None:
        raise NotImplementedError("Not Implemented")
