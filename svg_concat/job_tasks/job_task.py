from abc import ABC, abstractmethod

from svg_concat.job_tasks.job_result import JobResult
from svg_concat.merge.merge_config import MergeConfig


class JobTask(ABC):
    def __init__(self, merge_config: MergeConfig):
        self.merge_config = merge_config
        self.next: JobTask | None = None

    @abstractmethod
    def perform_task(self, job_result: JobResult) -> JobResult:
        pass
