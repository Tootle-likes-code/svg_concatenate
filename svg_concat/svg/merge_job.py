from datetime import datetime, timezone

from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.job_task import JobTask
from svg_concat.svg.merge_config import MergeConfig


class MergeJob:
    def __init__(self) -> None:
        self._job_steps: list[JobTask] = []
        self._last_job: JobTask | None = None

    @property
    def _first_step(self) -> JobTask | None:
        return self._job_steps[0] if self._job_steps else None

    def add_job(self, job_task: JobTask) -> None:
        if self._last_job is not None:
            self._last_job.next = job_task

        self._job_steps.append(job_task)
        self._last_job = job_task

    def start(self) -> JobResult:
        job_result: JobResult = JobResult()
        job_result.add_message(f"Started {datetime.now(timezone.utc).isoformat()}.")
        if self._first_step:
            return self._first_step.perform_task(job_result)
        else:
            raise ValueError("No Job's assigned")
