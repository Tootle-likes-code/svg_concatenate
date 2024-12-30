from svg_concat.file_discovery.file_filters.filter import Filter


class InverseFilter(Filter):
    def __init__(self, base_filter: Filter):
        self.base_filter = base_filter

    @classmethod
    def create_dummy_instance(cls):
        return InverseFilter(None)

    def __eq__(self, other):
        if not isinstance(other, InverseFilter):
            return False

        return self.base_filter == other.base_filter

    def __hash__(self):
        return hash(self.base_filter)

    def is_valid(self, file_name: str) -> bool:
        return not self.base_filter.is_valid(file_name)

    def merge(self, other_filter: "Filter") -> None:
        raise NotImplementedError("Not Implemented")

    def to_json(self):
        return {
            "inverted_filter": self.base_filter.to_json()
        }
