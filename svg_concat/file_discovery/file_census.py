import os

from svg_concat.file_discovery import census_result_builder
from svg_concat.file_discovery.census_result import CensusResult
from svg_concat.file_discovery.census_result_builder import CensusResultBuilder
from svg_concat.file_discovery.file_criteria import name_criterion
from svg_concat.file_discovery.file_criteria.criterion import Criterion
from svg_concat.file_discovery.file_criteria.name_criterion import NameCriterion


class FileCensus:
    def __init__(self, starting_directory: str, criteria: set[Criterion] | None = None,
                 files_to_find: list[str] = None):
        self.starting_directory = starting_directory

        if criteria is None:
            self.criteria = set()
        else:
            self.criteria = criteria

        if files_to_find is not None or files_to_find != []:
            self.files_to_find: NameCriterion = name_criterion.create_criterion(files_to_find)
            if self.files_to_find is not None:
                self.criteria.add(self.files_to_find)

    def search_directory(self) -> CensusResult:
        search_result_builder = census_result_builder.create_census_result()

        for path, directories, files in os.walk(self.starting_directory):
            self._add_files(path, files, search_result_builder)

        self._check_missing_files(search_result_builder)

        return search_result_builder.build()

    def _add_files(self, path, files, search_result_builder: CensusResultBuilder):
        for file_name in files:
            if not self._check_file_is_valid(file_name):
                continue
            full_path = os.path.join(path, file_name)
            search_result_builder.with_found_file(full_path, file_name)

    def _check_file_is_valid(self, file: str) -> bool:
        for criteria in self.criteria:
            if not criteria.is_valid(file):
                return False

        return True

    def _check_missing_files(self, builder: CensusResultBuilder):
        if self.files_to_find is None:
            return

        for file in self.files_to_find.names:
            if not builder.has_found_file(file):
                builder.with_missing_file(file)
