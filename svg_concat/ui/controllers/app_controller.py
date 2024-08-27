from svg_concat.file_discovery.file_census import FileCensus
from svg_concat.file_discovery.file_criteria.criterion import Criterion


class AppController:
    def __init__(self):
        self.criteria: list[Criterion] = []
        self.starting_directory: str = ""
        self.files_to_find: set[str] = set()

    def concatenate_files(self):
        census = FileCensus(self.starting_directory, self.criteria, self.files_to_find)
        census_result = census.search_directory()

        if census_result.has_missing_files:
            self.confirm_missing_files()
            return



    def confirm_missing_files(self):
        pass

