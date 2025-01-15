from pathlib import Path

from svg_concat.file_discovery.file_filters.filter import Filter


def create_filter(file_names):
    if file_names is None or len(file_names) == 0:
        return

    return NameFilter(file_names)


class NameFilter(Filter):
    def __init__(self, names: list[str]):
        self.names = names

    @classmethod
    def create_dummy_instance(cls):
        return NameFilter([])

    @property
    def names_with_count(self) -> dict[str, int]:
        counted_names = {}
        for name in self.names:
            if name in counted_names:
                counted_names[name] += 1
            else:
                counted_names[name] = 1

        return counted_names

    def __eq__(self, other):
        if not isinstance(other, NameFilter):
            return False
        return self.names == other.names

    def __hash__(self):
        return hash(frozenset(self.names))

    def is_valid(self, file_name: Path) -> bool:
        if file_name.name in self.names or file_name.stem in self.names:
            return True

        return False

    def merge(self, other_filter: Filter) -> None:
        if not isinstance(other_filter, NameFilter):
            raise TypeError(f"{other_filter} is not a {NameFilter.__name__}")

        self.names = other_filter.names

    def to_json(self) -> dict:
        return {
            "names": list(self.names),
        }
