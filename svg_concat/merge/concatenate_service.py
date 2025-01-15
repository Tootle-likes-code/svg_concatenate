from svg_concat.job_tasks import merge_job_factory
from svg_concat.job_tasks.job_result import JobResult
from svg_concat.merge.merge_config import MergeConfig
from svg_concat.merge import report_writer


class ConcatenateService:
    def __init__(self):
        self.success_callbacks = []
        self.failure_callbacks = []

    def concatenate(self, merge_config: MergeConfig):
        merge_job = merge_job_factory.create(merge_config)

        job_result = merge_job.start()

        if job_result.is_success:
            self._success(job_result)
        else:
            self._fail(job_result)

        report_writer.write_report(merge_config.report_path, job_result)

    def subscribe_to_failures(self, callback):
        self.failure_callbacks.append(callback)

    def subscribe_to_successes(self, callback):
        self.success_callbacks.append(callback)

    def _fail(self, result: JobResult):
        for callback in self.failure_callbacks:
            callback(result)

    def _success(self, result: JobResult):
        for callback in self.success_callbacks:
            callback(result)
