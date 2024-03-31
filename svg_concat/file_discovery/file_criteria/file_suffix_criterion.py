from svg_concat.file_discovery.file_criteria.criterion import Criterion


def _clean_suffixes(suffix_list) -> set[str]:
    clean_suffixes: set[str] = set()

    for suffix in suffix_list:
        stripped_suffix = suffix.strip()
        if stripped_suffix[0] == '.':
            stripped_suffix = stripped_suffix[1:]

        clean_suffixes.add(stripped_suffix)

        return clean_suffixes


class FileSuffixCriterion(Criterion):
    def __init__(self, suffix_list: list[str]):
        self.allowed_suffixes = _clean_suffixes(suffix_list)

    def is_valid(self, file_name: str) -> bool:
        for suffix in self.allowed_suffixes:
            if file_name.endswith(suffix):
                return True

        return False
