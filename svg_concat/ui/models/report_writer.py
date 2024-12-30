from pathlib import Path

from svg_concat.job_tasks.job_result import JobResult


def write_report(report_path: Path, result: JobResult):
    with report_path.open('w', encoding="UTF-8") as report_file:
        if result.is_success:
            report_file.write("Status: Success")
        elif result.is_fatal:
            report_file.write("Status: Fatal Error")
        else:
            report_file.write("Status: Error")

        report_file.write("\n#####################################################")
        reported_messages = "\n".join(result.messages)
        report_file.write(reported_messages)

