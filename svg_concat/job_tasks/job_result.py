from svg_concat.file_discovery.census_result import CensusResult
from svg_concat.read_only_list import ReadOnlyList


class JobResult:
    def __init__(self):
        self._failed = False
        self._is_fatal = False
        self._messages: list[str] = []
        self.census_result: CensusResult | None = None

    @property
    def is_success(self):
        return not self._failed

    @property
    def is_fatal(self):
        return self._is_fatal

    @property
    def messages(self) -> tuple[str, ...]:
        return ReadOnlyList(self._messages).data

    def add_message(self, message: str):
        self._messages.append(message)

    def __str__(self):
        return (f"JobResult(failed: {self._failed}, is_fatal: {self._is_fatal}, "
                f"messages: [{[message for message in self._messages]}])")

    def fail(self, message: str):
        self._failed = True
        self._messages.append(message)

    def fatal_fail(self, message: str):
        self._is_fatal = True
        self._failed = True
        self._messages.append(message)
