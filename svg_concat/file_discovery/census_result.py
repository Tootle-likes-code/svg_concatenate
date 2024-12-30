from dataclasses import dataclass, field

from svg_concat.file_discovery.censused_file import CensusedFile


@dataclass
class CensusResult:
    found_files: set[CensusedFile] = field(default_factory=set)
    missing_files: set[str] = field(default_factory=set)

    def __eq__(self, other):
        if not isinstance(other, CensusResult):
            return False

        if self.found_files != other.found_files:
            return False

        if self.missing_files != other.missing_files:
            return False

        return True

    @property
    def is_success(self) -> bool:
        return len(self.found_files) > 0 and not self.has_missing_files
    @property
    def is_failure(self):
        return not self.is_success

    @property
    def has_missing_files(self):
        return len(self.missing_files) > 0
