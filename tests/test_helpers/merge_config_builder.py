from pathlib import Path

from svg_concat.file_discovery.file_filters.filter import Filter
from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.svg.merge_config import MergeConfig


def create() -> "MergeConfigBuilder":
    return MergeConfigBuilder()


class MergeConfigBuilder:
    def __init__(self):
        self._initial_directory = Path("")
        self._svg_file = Path("")
        self._report_file = Path("")
        self._filters = FilterCollection()

    def build(self) -> MergeConfig:
        return MergeConfig(
            self._initial_directory,
            self._svg_file,
            self._report_file,
            self._filters
        )

    def with_initial_directory(self, initial_directory: str | Path) -> "MergeConfigBuilder":
        if isinstance(initial_directory, str):
            initial_directory = Path(initial_directory)
        self._initial_directory = initial_directory
        return self

    def with_svg_file(self, svg_file: str | Path) -> "MergeConfigBuilder":
        if isinstance(svg_file, str):
            svg_file = Path(svg_file)
        self._svg_file = svg_file
        return self

    def with_report_file(self, report_file: str | Path) -> "MergeConfigBuilder":
        if isinstance(report_file, str):
            report_file = Path(report_file)
        self._report_file = report_file
        return self

    def with_filters(self, filters: FilterCollection) -> "MergeConfigBuilder":
        self._filters = filters
        return self

    def with_filter(self, filter_: Filter) -> "MergeConfigBuilder":
        self._filters.upsert(filter_)
        return self
