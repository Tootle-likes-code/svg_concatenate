import json
import stat
import unittest
from pathlib import Path

from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.job_tasks.job_result import JobResult
from svg_concat.job_tasks.verify_paths_task import VerifyPathsTask
from svg_concat.merge import merge_config
from tests.test_helpers import merge_config_builder


class VerifyPathTaskTests(unittest.TestCase):
    def setUp(self):
        empty_config = merge_config.create("test", "test",
                                           "test", "test", FilterCollection())
        self.empty_config = VerifyPathsTask(empty_config)


class PerformTaskTests(VerifyPathTaskTests):
    test_files = None
    folder = None

    @classmethod
    def setUpClass(cls):
        with open("test_config.json", "r") as test_config:
            config = json.load(test_config)
        cls.test_files = Path(config["test_folder"])
        cls.test_files.mkdir(exist_ok=True)
        cls.test_files.chmod(stat.S_IWUSR)
        print(f"Folder '{cls.test_files}' created.")

        cls.folder = Path(config["read_only_folder"])
        cls.folder.mkdir(exist_ok=True)
        cls.folder.chmod(stat.S_IREAD)
        print(f"Folder '{cls.folder}' created and set to read-only mode.")

    @classmethod
    def tearDownClass(cls):
        cls.folder.chmod(stat.S_IWUSR)
        cls.folder.rmdir()
        print(f"Folder '{cls.folder}' removed.")

        cls.test_files.rmdir()
        print(f"Folder '{cls.test_files}' removed.")

    def setUp(self):
        super().setUp()

        valid_svg_files = self.test_files.joinpath("svg.svg")
        valid_report_files = self.test_files.joinpath("report.txt")

        no_instance_config = (merge_config_builder.create()
                              .with_initial_directory("fake/not_exists/")
                              .with_svg_file(valid_svg_files)
                              .with_report_file(valid_report_files)
                              .build()
                              )

        no_svg_file_config = (merge_config_builder.create()
                              .with_initial_directory(self.test_files)
                              .with_svg_file("fake/not_exists/")
                              .with_report_file(valid_report_files)
                              .build()
                              )

        no_report_file_config = (merge_config_builder.create()
                                 .with_svg_file(valid_svg_files)
                                 .with_initial_directory(self.test_files)
                                 .with_report_file("fake/not_exists/")
                                 .build()
                                 )

        self.no_instance = VerifyPathsTask(no_instance_config)
        self.no_svg_file = VerifyPathsTask(no_svg_file_config)
        self.no_report_file = VerifyPathsTask(no_report_file_config)

    def test_no_merge_config_sets_fatal(self):
        # Arrange
        no_config = VerifyPathsTask(None)

        # Act
        result = no_config.perform_task(JobResult())

        # Assert
        self.assertTrue(result.is_fatal)

    def test_no_merge_config_returns_correct_message(self):
        # Arrange
        expected_result = (
            "Verifying Paths: No Config",
        )
        no_config = VerifyPathsTask(None)

        # Act
        result = no_config.perform_task(JobResult())

        # Assert
        self.assertEqual(expected_result, result.messages)

    def test_no_result_raises_value_error(self):
        # Arrange
        expected_message = "No JobResult given"

        # Assert
        with self.assertRaises(ValueError) as ex:
            # Act
            self.empty_config.perform_task(None)

        # Assert
        message = str(ex.exception)
        self.assertEqual(expected_message, message)

    def test_initial_directory_doesnt_exist_returns_fatal(self):
        # Act
        result = self.no_instance.perform_task(JobResult())

        # Assert
        self.assertTrue(result.is_fatal)

    def test_initial_directory_doesnt_exist_returns_correct_message(self):
        # Arrange
        expected_result = ("Verifying Paths: Initial Directory doesn't exist",)

        # Act
        result = self.no_instance.perform_task(JobResult())

        # Assert
        self.assertEqual(expected_result, result.messages)

    def test_svg_file_directory_doesnt_exist_returns_fatal(self):
        # Act
        result = self.no_svg_file.perform_task(JobResult())

        # Assert
        self.assertTrue(result.is_fatal)

    def test_svg_file_directory_doesnt_exist_returns_correct_message(self):
        # Arrange
        expected_result = ("Verifying Paths: Given svg output location doesn't exist",)

        # Act
        result = self.no_svg_file.perform_task(JobResult())

        # Assert
        self.assertEqual(expected_result, result.messages)

    def test_report_file_directory_doesnt_exist_returns_correct_message(self):
        # Arrange
        expected_result = ("Verifying Paths: Given report output location doesn't exist",)

        # Act
        result = self.no_report_file.perform_task(JobResult())

        # Assert
        self.assertEqual(expected_result, result.messages)

    def test_report_file_directory_doesnt_exist_returns_fatal(self):
        # Act
        result = self.no_report_file.perform_task(JobResult())

        # Assert
        self.assertTrue(result.is_fatal)

    def test_svg_file_directory_is_locked_returns_fatal(self):
        # Arrange
        config = (merge_config_builder.create()
                  .with_initial_directory(self.test_files)
                  .with_svg_file(self.folder.joinpath("svg.svg"))
                  .with_report_file(self.test_files.joinpath("report.txt"))
                  .build()
                  )
        test_task = VerifyPathsTask(config)

        # Act
        result = test_task.perform_task(JobResult())

        # Assert
        self.assertTrue(result.is_fatal)

    def test_svg_file_directory_is_locked_returns_correct_message(self):
        # Arrange
        expected_result = ("Verifying Paths: Given svg output location is not writable",)
        config = (merge_config_builder.create()
                  .with_initial_directory(self.test_files)
                  .with_svg_file(self.folder.joinpath("svg.svg"))
                  .with_report_file(self.test_files.joinpath("report.txt"))
                  .build()
                  )
        test_task = VerifyPathsTask(config)

        # Act
        result = test_task.perform_task(JobResult())

        # Assert
        self.assertEqual(expected_result, result.messages)

    def test_report_file_directory_is_locked_returns_fatal(self):
        # Arrange
        config = (merge_config_builder.create()
                  .with_initial_directory(self.test_files)
                  .with_svg_file(self.test_files.joinpath("svg.svg"))
                  .with_report_file(self.folder.joinpath("report.txt"))
                  .build()
                  )
        test_task = VerifyPathsTask(config)

        # Act
        result = test_task.perform_task(JobResult())

        # Assert
        self.assertTrue(result.is_fatal)

    def test_report_file_directory_is_locked_returns_correct_message(self):
        # Arrange
        expected_result = ("Verifying Paths: Given report output location is not writable",)
        config = (merge_config_builder.create()
                  .with_initial_directory(self.test_files)
                  .with_svg_file(self.test_files.joinpath("svg.svg"))
                  .with_report_file(self.folder.joinpath("report.txt"))
                  .build()
                  )
        test_task = VerifyPathsTask(config)

        # Act
        result = test_task.perform_task(JobResult())

        # Assert
        self.assertEqual(expected_result, result.messages)


if __name__ == '__main__':
    unittest.main()
