from svg_concat.file_discovery.file_filters.filter import Filter


def create_from_csv(text: str) -> "FileSuffixFilter":
    values = text.split(",")
    return FileSuffixFilter(values)


def _clean_suffixes(suffixes: str | list[str]) -> set[str]:
    if isinstance(suffixes, str):
        return {suffixes}

    clean_suffixes: set[str] = set()
    for suffix in suffixes:
        stripped_suffix = suffix.strip()
        if stripped_suffix == "":
            continue
        if stripped_suffix[0] == '.':
            stripped_suffix = stripped_suffix[1:]

        clean_suffixes.add(stripped_suffix)

    return clean_suffixes


class FileSuffixFilter(Filter):
    def __init__(self, suffix_list: str | list[str]):
        self.allowed_suffixes = _clean_suffixes(suffix_list)

    @classmethod
    def create_dummy_instance(cls) -> "FileSuffixFilter":
        return FileSuffixFilter(".svg")

    def __eq__(self, other):
        if not isinstance(other, FileSuffixFilter):
            return False

        return self.allowed_suffixes == other.allowed_suffixes

    def __hash__(self):
        return hash(frozenset(self.allowed_suffixes))

    def is_valid(self, file_name: str) -> bool:
        for suffix in self.allowed_suffixes:
            if file_name.endswith(suffix):
                return True
        return False

    def update(self, file_suffixes: str) -> None:
        suffixes = _clean_suffixes(file_suffixes.split(","))

        for suffix in suffixes:
            self.allowed_suffixes.add(suffix)

    def merge(self, other_filter: Filter):
        if not isinstance(other_filter, FileSuffixFilter):
            raise TypeError(f"{other_filter} is not a {FileSuffixFilter.__name__}")

        self.allowed_suffixes = other_filter.allowed_suffixes

    def __repr__(self):
        return f"FileSuffixFilter(allowed_suffixes={self.allowed_suffixes})"

