from typing import Protocol

from svg_concat.file_discovery import filter_factory
from svg_concat.file_discovery.file_filters import file_suffix_filter
from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.filter import Filter
from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.file_discovery.filter_types import FilterType
from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from svg_concat.ui.view_models import filter_view_model_factory
from svg_concat.ui.view_models.filter_view_model import FilterViewModel


class FiltersSubscriber(Protocol):
    def update_filters(self):
        ...


class FiltersModel:
    def __init__(self):
        self._filters: FilterCollection = FilterCollection()
        self.filters_observers: set[FiltersSubscriber] = set()
        self._models: dict[type(Filter), FilterViewModel] = {}

    @property
    def filters(self) -> dict[type(Filter), FilterViewModel]:
        return self._models

    @property
    def file_suffixes(self) -> str:
        found_filter: FileSuffixFilter | None = self._filters.get(FileSuffixFilter, None)

        if found_filter:
            return ", ".join(found_filter.allowed_suffixes)
        else:
            return ""

    @property
    def file_names(self) -> list[str]:
        found_filter: NameFilter | None = self._filters.get(NameFilter, None)

        if found_filter:
            return list(found_filter.names)
        else:
            return []

    def update_filters(self):
        self._models = filter_view_model_factory.convert_all(self._filters)

    def subscribe_to_changes(self, callback: FiltersSubscriber):
        self.filters_observers.add(callback)

    def publish_changes(self):
        self.update_filters()
        for callback in self.filters_observers:
            callback.update_filters()

    def create_filter(self, filter_type: FilterType, *args) -> None:
        new_filter = filter_factory.create(filter_type, *args)

        self._filters.upsert(new_filter)
        self.publish_changes()

    def create_inverted_filter(self, inverted_filter_type: FilterType, *args) -> None:
        new_filter = filter_factory.create_inverted_filter(inverted_filter_type, *args)

        self._filters.upsert(new_filter)
        self.publish_changes()

    def update_file_suffix_filter(self, filter_string: str) -> None:
        filter_: FileSuffixFilter | None = self.filters.get(FilterType.FILE_SUFFIX_FILTER, None)

        if filter_ is None:
            self._filters[FilterType.FILE_SUFFIX_FILTER] = file_suffix_filter.create_from_csv(filter_string)
        else:
            filter_.update(filter_string)

        self.publish_changes()
