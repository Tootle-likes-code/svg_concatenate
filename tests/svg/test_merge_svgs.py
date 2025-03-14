import unittest
from pathlib import Path

from svg_concat.file_discovery.censused_file import CensusedFile
from svg_concat.svg.merge_svgs import merge_svgs, line_merge_svgs
from tests.svg import expected_results
from tests.test_helpers import file_helper


class MergeSvgsTests(unittest.TestCase):
    def setUp(self):
        self.test_loaded_file_is_merged_correctly_output = (
            Path(f"{MergeSvgsTests.test_loaded_file_is_merged_correctly.__name__}.svg"))
        self.test_line_merge_svgs_output = Path(f"{MergeSvgsTests.test_line_merge_svgs.__name__}.svg")

    def tearDown(self):
        if self.test_loaded_file_is_merged_correctly_output.exists():
            self.test_loaded_file_is_merged_correctly_output.unlink()

        if self.test_line_merge_svgs_output.exists():
            self.test_line_merge_svgs_output.unlink()

    def test_loaded_file_is_merged_correctly(self):
        # Arrange
        files_to_merge = [
            (CensusedFile("Aadhira", file_helper.get_path("test_files/Sub folder/Aadhira.svg")), 1),
            (CensusedFile("Best Man", file_helper.get_path("test_files/Sub folder/Sub Sub Folder/Best Man.svg")), 1),
            (CensusedFile("Aaleah", file_helper.get_path("test_files/Aaleah.svg")), 1),
            (CensusedFile("Aaliyah", file_helper.get_path("test_files/Other Sub Folder/Aaliyah.svg")), 1)
        ]
        output_location = self.test_loaded_file_is_merged_correctly_output
        expected_result = expected_results.test_merge_svgs_results[self.test_loaded_file_is_merged_correctly.__name__]

        # Act
        merge_svgs(output_location, files_to_merge)

        # Assert
        self.assertTrue(self.test_loaded_file_is_merged_correctly_output.exists())

        with self.test_loaded_file_is_merged_correctly_output.open('r') as f:
            result = f.read()

        self.assertEqual(expected_result, result)

    def test_line_merge_svgs(self):
        # Arrange
        files_to_merge = [
            file_helper.get_path("test_files/Sub folder/Aadhira.svg"),
            file_helper.get_path("test_files/Sub folder/Sub Sub Folder/Best Man.svg")
        ]
        output_location = self.test_line_merge_svgs_output
        expected_result = expected_results.test_merge_svgs_results[self.test_line_merge_svgs.__name__]

        # Act
        line_merge_svgs(output_location, True, *files_to_merge)

        # Assert
        self.assertTrue(self.test_line_merge_svgs_output.exists())

        with self.test_line_merge_svgs_output.open('r') as f:
            result = f.read()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
