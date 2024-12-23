from svg_concat.file_discovery.file_filters.filter import Filter


def create_filter(file_names):
    if file_names is None or len(file_names) == 0:
        return

    return NameFilter(file_names)


class NameFilter(Filter):
    def __init__(self, names: set[str]):
        self.names = names

    @classmethod
    def create_dummy_instance(cls):
        return NameFilter(set())

    def __eq__(self, other):
        if not isinstance(other, NameFilter):
            return False
        return self.names == other.names

    def __hash__(self):
        return hash(frozenset(self.names))

    def is_valid(self, file_name: str) -> bool:
        if file_name in self.names:
            return True

        return False

    def merge(self, other_filter: Filter) -> None:
        if not isinstance(other_filter, NameFilter):
            raise TypeError(f"{other_filter} is not a {NameFilter.__name__}")

        self.names = other_filter.names
