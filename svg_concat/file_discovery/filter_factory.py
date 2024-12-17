from typing import Type, Callable

from svg_concat.file_discovery.file_filters import file_suffix_filter
from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.filter import Filter
from svg_concat.file_discovery.file_filters.filter_types import FilterType


def _create_file_suffix_filter(*args) -> FileSuffixFilter:
    file_name_suffixes = args[0]
    return file_suffix_filter.create_from_csv(file_name_suffixes)


_FILTER_CREATE: dict[FilterType, Callable] = {
    FilterType.FILE_SUFFIX_FILTER: _create_file_suffix_filter
}


def create(filter_type: FilterType, *args) -> Filter:
    created_filter = _FILTER_CREATE[filter_type](*args)
    return created_filter
