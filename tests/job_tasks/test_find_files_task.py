import unittest
from pathlib import Path

from svg_concat.job_tasks.find_files_task import FindFilesTask
from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.missing_merge_config_error import MissingMergeConfigError
from tests.job_tasks.mocks.mock_job_task import MockTask
from tests.test_helpers import merge_config_builder


class FindFilesTaskTests(unittest.TestCase):
    pass


class ConstructorTests(FindFilesTaskTests):
    def test_given_next_is_set(self):
        # Arrange
        mocked_task = MockTask()
        expected_result = mocked_task

        # Act
        test_task = FindFilesTask(None, mocked_task)

        # Assert
        self.assertEqual(expected_result, test_task.next)


class PerformTaskTests(FindFilesTaskTests):
    test_files = Path("test_files/")

    def setUp(self):
        super().__init__()
        config = (merge_config_builder.create()
                  .with_initial_directory(self.test_files)
                  .build()
                  )

        self.test_task = FindFilesTask(config, MockTask())

    def test_no_merge_config_raises_correct_error(self):
        # Arrange

        # Assert
        with self.assertRaises(MissingMergeConfigError):
            # Act
            FindFilesTask(None, None).perform_task(JobResult())


if __name__ == '__main__':
    unittest.main()
