from pathlib import Path

from svg_concat.file_discovery.census_result import CensusResult
from svg_concat.file_discovery.censused_file import CensusedFile


def create_census_result() -> "CensusResultBuilder":
    return CensusResultBuilder()


class CensusResultBuilder:
    def __init__(self):
        self.found_files: set[CensusedFile] = set()
        self.missing_files: set[str] = set()

    def build(self) -> CensusResult:
        return CensusResult(found_files=self.found_files, missing_files=self.missing_files)

    def with_found_file(self, file_path: str, file_name: str) -> "CensusResultBuilder":
        path = Path(file_path)
        self.found_files.add(CensusedFile(name=file_name, path=path))
        return self

    def with_censused_file(self, censused_file: CensusedFile) -> "CensusResultBuilder":
        self.found_files.add(censused_file)
        return self

    def with_missing_file(self, file_path: str) -> "CensusResultBuilder":
        self.missing_files.add(file_path)
        return self

    def has_found_file(self, file_name: str) -> bool:
        return file_name in self.found_files
