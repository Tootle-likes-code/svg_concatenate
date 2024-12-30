from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.inverse_filter import Filter, InverseFilter
from svg_concat.file_discovery.file_filters.name_filter import NameFilter


def create_from_json(data: list[dict]) -> "FilterCollection":
    filter_collection = FilterCollection()
    for filter_dict in data:
        filter_collection.upsert(_create_filter_from_json(filter_dict))

    return filter_collection


def _create_filter_from_json(filter_dict: dict) -> Filter:
    if "names" in filter_dict:
        return NameFilter(filter_dict["names"])

    if "inverted_filter" in filter_dict:
        internal_filter = _create_filter_from_json(filter_dict["inverted_filter"])
        return InverseFilter(internal_filter)

    if "allowed_suffixes" in filter_dict:
        return FileSuffixFilter(filter_dict["allowed_suffixes"])


class FilterCollection:
    def __init__(self):
        self.file_suffix_filter: FileSuffixFilter | None = None
        self.names_filter: NameFilter | None = None
        self.other_filters: set[Filter] = set()

    def _check_value(self, value) -> None:
        if not isinstance(value, Filter) or not issubclass(type(value), Filter):
            raise TypeError(f'{value} is not a subclass of {Filter.__name__}')

    def __len__(self) -> int:
        count = len(self.other_filters)
        if self.file_suffix_filter is not None:
            count += 1
        if self.names_filter is not None:
            count += 1

        return count

    def __str__(self) -> str:
        output = f"{FilterCollection.__name__}("

    def get(self, filter_to_find, default=None) -> Filter | set[Filter]:
        instance = filter_to_find.create_dummy_instance()
        self._check_value(instance)

        if isinstance(instance, FileSuffixFilter):
            if self.file_suffix_filter is not None:
                return self.file_suffix_filter
            else:
                return default

        if isinstance(instance, NameFilter) and self.names_filter is not None:
            if self.names_filter is not None:
                return self.names_filter
            else:
                return default

        results = set()
        for filter_ in self.other_filters:
            if isinstance(filter_, filter_to_find):
                results.add(filter_)

        if len(results) == 0:
            return default
        else:
            return results

    def upsert(self, value) -> None:
        if not issubclass(type(value), Filter):
            raise TypeError(f'{value} is not a subclass of {Filter.__name__}')

        if isinstance(value, FileSuffixFilter):
            if self.file_suffix_filter is not None:
                self.file_suffix_filter.merge(value)
            else:
                self.file_suffix_filter = value

        elif isinstance(value, NameFilter):
            if self.names_filter is not None:
                self.names_filter.merge(value)
            else:
                self.names_filter = value
        else:
            self.other_filters.add(value)

    def values(self) -> list[Filter]:
        values = list(self.other_filters)

        if self.file_suffix_filter is not None:
            values.append(self.file_suffix_filter)

        if self.names_filter is not None:
            values.append(self.names_filter)

        return values
