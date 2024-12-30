from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.job_task import JobTask
from svg_concat.svg.merge_config import MergeConfig
from svg_concat.svg.merge_svgs import merge_svgs


class MergeSvgsTask(JobTask):
    def __init__(self, merge_config: MergeConfig):
        super().__init__(merge_config)

    def perform_task(self, job_result: JobResult) -> JobResult:
        output_file = self.merge_config.svg_file
        job_result.add_message("Merge SVGs: Beginning Merge")
        merged_svgs = merge_svgs(output_file, *job_result.census_result.found_files)
        [job_result.add_message(merged_svg) for merged_svg in merged_svgs.values()]
        job_result.add_message("Merge SVGs: Completed")
        return job_result
