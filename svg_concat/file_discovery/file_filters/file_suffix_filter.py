from svg_concat.file_discovery.file_filters.filter import Filter


def _clean_suffixes(suffixes: str | list[str]) -> set[str]:
    if suffixes is str:
        return {suffixes}

    clean_suffixes: set[str] = set()
    for suffix in suffixes:
        stripped_suffix = suffix.strip()
        if stripped_suffix[0] == '.':
            stripped_suffix = stripped_suffix[1:]

        clean_suffixes.add(stripped_suffix)

        return clean_suffixes


class FileSuffixFilter(Filter):
    def __init__(self, suffix_list: str | list[str]):
        self.allowed_suffixes = _clean_suffixes(suffix_list)

    def is_valid(self, file_name: str) -> bool:
        for suffix in self.allowed_suffixes:
            if file_name.endswith(suffix):
                return True

        return False
