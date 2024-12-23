from typing import Callable

from svg_concat.file_discovery.file_filters import file_suffix_filter, name_filter
from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.filter import Filter
from svg_concat.file_discovery.filter_types import FilterType
from svg_concat.file_discovery.file_filters.name_filter import NameFilter


def _create_file_suffix_filter(*args) -> FileSuffixFilter:
    file_name_suffixes = args[0]
    return file_suffix_filter.create_from_csv(file_name_suffixes)


def _create_name_filter(*args) -> NameFilter:
    file_names = set(args[0])
    return name_filter.create_filter(file_names)


_FILTER_CREATE: dict[FilterType, Callable] = {
    FilterType.FILE_SUFFIX_FILTER: _create_file_suffix_filter,
    FilterType.FILE_NAME_FILTER: _create_name_filter
}


def create(filter_type: FilterType, *args) -> Filter:
    created_filter = _FILTER_CREATE[filter_type](*args)
    return created_filter
