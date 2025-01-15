from svg_concat.file_discovery.censused_file import CensusedFile
from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.job_task import JobTask
from svg_concat.merge.merge_config import MergeConfig
from svg_concat.svg.merge_svgs import merge_svgs


class MergeSvgsTask(JobTask):
    def __init__(self, merge_config: MergeConfig):
        super().__init__(merge_config)

    def perform_task(self, job_result: JobResult) -> JobResult:
        output_file = self.merge_config.svg_file
        job_result.add_message("Merge SVGs: Beginning Merge")
        files_to_merge_with_count = self._get_number_of_times_file_needs_to_be_added(
            job_result.census_result.found_files)
        merged_svgs = merge_svgs(output_file, files_to_merge_with_count)
        [job_result.add_message(merged_svg) for merged_svg in merged_svgs.values()]
        job_result.add_message("Merge SVGs: Completed")
        return job_result

    def _get_number_of_times_file_needs_to_be_added(self, found_files) -> list[tuple[CensusedFile, int]]:
        found_files_with_times_to_merge = []
        names_to_find = self.merge_config.names_to_find()
        for found_file in found_files:
            times_to_merge = names_to_find[found_file.name]
            file_and_count = (found_file, times_to_merge)
            found_files_with_times_to_merge.append(file_and_count)

        return found_files_with_times_to_merge
