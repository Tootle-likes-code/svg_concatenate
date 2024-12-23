from typing import Callable, Type

from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.filter import Filter
from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.file_discovery.file_filters.inverse_filter import Filter
from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from svg_concat.ui.view_models.filter_view_model import FilterViewModel


def convert_all(filters: list[Filter] | set[Filter] | FilterCollection) \
        -> dict[Type[Filter], FilterViewModel]:
    if isinstance(filters, FilterCollection):
        return convert_all(filters.values())
    return {type(filter_): convert(filter_) for filter_ in filters}


def convert(filter_to_convert: Filter) -> FilterViewModel:
    func = _conversion_methods[type(filter_to_convert)]
    return func(filter_to_convert)


def _convert_file_suffix_filter(file_suffix_filter: FileSuffixFilter) -> FilterViewModel:
    suffixes = ", ".join(file_suffix_filter.allowed_suffixes)
    name = f"allow files using: {suffixes}"
    tooltip_text = name

    return FilterViewModel(file_suffix_filter, name, tooltip_text)


def _convert_name_filter(name_filter: NameFilter) -> FilterViewModel:
    files = ", ".join(name_filter.names)
    name = f"allow filenames: {files}"
    tooltip_text = name

    return FilterViewModel(name_filter, name, tooltip_text)


def _convert_inverse_filter(criterion: Filter) -> FilterViewModel:
    child_view_model = convert(criterion.base_criterion)
    description = f"dis{child_view_model.name}"
    tooltip_text = f"dis{child_view_model.tooltip_text}"

    return FilterViewModel(criterion, description, tooltip_text)


_conversion_methods: dict[str, Callable[[Filter], FilterViewModel]] = {
    FileSuffixFilter: _convert_file_suffix_filter,
    NameFilter: _convert_name_filter,
    Filter: _convert_inverse_filter
}

filter_names_to_types_mapping = {
    "File Type Filter": FileSuffixFilter,
    "Names Filter": NameFilter,
    "Inverse Filter": Filter
}

filter_types_to_names_mapping = {value: key for key, value in filter_names_to_types_mapping.items()}


def create(file_suffix: str | None = None) -> FilterViewModel:
    if file_suffix is not None:
        return _create_file_suffix_filter(file_suffix)


def _create_file_suffix_filter(file_suffix: str) -> FilterViewModel:
    filter_ = FileSuffixFilter(file_suffix)
    return _convert_file_suffix_filter(filter_)
