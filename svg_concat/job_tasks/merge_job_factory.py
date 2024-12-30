from svg_concat.job_tasks.find_files_task import FindFilesTask
from svg_concat.job_tasks.merge_svgs_task import MergeSvgsTask
from svg_concat.job_tasks.verify_paths_task import VerifyPathsTask
from svg_concat.svg.merge_config import MergeConfig
from svg_concat.svg.merge_job import MergeJob


def create(merge_config: MergeConfig) -> MergeJob:
    merge_svgs_job = MergeSvgsTask(merge_config)
    find_files_task = FindFilesTask(merge_config, merge_svgs_job)
    verify_paths_task = VerifyPathsTask(merge_config, find_files_task)

    merge_job = MergeJob()
    merge_job.add_job(verify_paths_task)

    return merge_job
