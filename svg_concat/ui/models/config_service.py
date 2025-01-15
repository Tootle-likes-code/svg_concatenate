import json

from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.merge.merge_config import MergeConfig, create as create_merge_config
from svg_concat.file_discovery.file_filters import filter_collection


class ConfigService:
    def save_config(self, merge_config: MergeConfig) -> None:
        converted_data = self._convert_config_to_json(merge_config)
        with open('config.json', 'w') as f:
            json.dump(converted_data, f, indent=4)

    def _convert_config_to_json(self, merge_config: MergeConfig):
        filters = self._convert_filters_to_json(merge_config.filters)
        json_config = {
            "initial_directory": str(merge_config.initial_directory),
            "output_directory": str(merge_config.output_directory),
            "svg_file": str(merge_config.svg_file.name),
            "report_file": str(merge_config.report_path.name),
            "filters": filters
        }

        return json_config

    def _convert_filters_to_json(self, filters: FilterCollection):
        converted_filters = [filter_.to_json() for filter_ in filters.values()]

        return converted_filters

    def load_config(self) -> MergeConfig:
        with open('config.json', 'r') as f:
            base_config = json.load(f)

        filters = filter_collection.create_from_json(base_config["filters"])

        merge_config = create_merge_config(
            base_config["initial_directory"],
            base_config["output_directory"],
            base_config["svg_file"],
            base_config["report_file"],
            filters
        )

        return merge_config
