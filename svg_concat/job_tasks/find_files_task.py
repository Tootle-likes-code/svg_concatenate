from svg_concat.file_discovery.file_census import FileCensus
from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.job_task import JobTask
from svg_concat.job_tasks.missing_merge_config_error import MissingMergeConfigError
from svg_concat.svg.merge_config import MergeConfig


class FindFilesTask(JobTask):
    def __init__(self, merge_config: MergeConfig, next_task: JobTask):
        super().__init__(merge_config)
        self.merge_config = merge_config
        self.next = next_task

    def perform_task(self, job_result: JobResult) -> JobResult:
        if self.merge_config == None:
            raise MissingMergeConfigError()

        job_result.add_message("File Search: Searching for Files")
        census = FileCensus(str(self.merge_config.initial_directory),
                            self.merge_config.filters,
                            self.merge_config.names_to_find()
                            )

        result = census.search_directory()
        job_result.census_result = result

        if result.is_failure:
            pretty_missing_files = "\n".join(result.missing_files)
            job_result.fail(f"File Search: Failed to find all files.  Missing:\n{pretty_missing_files}")
            return job_result

        job_result.add_message("File Search: Search complete.  Found all files.")
        return self.next.perform_task(job_result)
