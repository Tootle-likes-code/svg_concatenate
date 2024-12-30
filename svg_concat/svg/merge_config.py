from dataclasses import dataclass
from pathlib import Path

from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection


def create(
        initial_directory: str,
        output_directory: str,
        svg_file: str,
        report_file: str,
        filters: FilterCollection
) -> "MergeConfig":
    output_directory_path = Path(output_directory)
    svg_path: Path = output_directory_path.joinpath(svg_file)
    report_path: Path = output_directory_path.joinpath(report_file)

    return MergeConfig(Path(initial_directory), output_directory_path, svg_path, report_path, filters)


@dataclass
class MergeConfig:
    initial_directory: Path
    output_directory: Path
    svg_file: Path
    report_path: Path
    filters: FilterCollection

    def names_to_find(self) -> set[str]:
        if self.filters.names_filter is not None:
            return self.filters.names_filter.names
        return set()
