import os
import stat

from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.job_task import JobTask
from svg_concat.svg.merge_config import MergeConfig


class VerifyPathsTask(JobTask):
    def __init__(self, merge_config: MergeConfig, next: JobTask | None = None):
        super().__init__(merge_config)
        if next is not None:
            self.next = next

    def perform_task(self, job_result: JobResult) -> JobResult:
        if not job_result:
            raise ValueError("No JobResult given")

        self._check_merge_config_is_valid(job_result)

        if not job_result.is_success:
            return job_result

        self._check_initial_directory_exists(job_result)
        self._check_svg_parent_directory_exists(job_result)
        self._check_report_file_directory_exists(job_result)

        if not job_result.is_success:
            return job_result

        self._check_svg_parent_directory_is_writeable(job_result)
        self._check_report_parent_directory_is_writeable(job_result)

        return self.next.perform_task(job_result)

    def _check_merge_config_is_valid(self, job_result: JobResult):
        if self.merge_config is None:
            job_result.fatal_fail("Verifying Paths: No Config")

    def _check_initial_directory_exists(self, job_result: JobResult):
        if not self.merge_config.initial_directory.exists():
            job_result.fatal_fail("Verifying Paths: Initial Directory doesn't exist")

    def _check_svg_parent_directory_exists(self, job_result: JobResult):
        if not self.merge_config.svg_file.parent.exists():
            job_result.fatal_fail("Verifying Paths: Given svg output location doesn't exist")

    def _check_report_file_directory_exists(self, job_result: JobResult):
        if not self.merge_config.report_path.parent.exists():
            job_result.fatal_fail("Verifying Paths: Given report output location doesn't exist")

    def _check_svg_parent_directory_is_writeable(self, job_result: JobResult):
        permissions = self.merge_config.svg_file.parent.stat().st_mode
        if not permissions & stat.S_IWUSR:
            job_result.fatal_fail("Verifying Paths: Given svg output location is not writable")

    def _check_report_parent_directory_is_writeable(self, job_result: JobResult):
        permissions = self.merge_config.report_path.parent.stat().st_mode
        if not permissions & stat.S_IWUSR:
            job_result.fatal_fail("Verifying Paths: Given report output location is not writable")
