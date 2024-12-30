from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.job_task import JobTask
from svg_concat.svg.merge_config import MergeConfig


class MockTask(JobTask):
    def __init__(self, merge_config: MergeConfig | None = None):
        super().__init__(merge_config)

    def perform_task(self, job_result: JobResult) -> JobResult:
        return job_result
