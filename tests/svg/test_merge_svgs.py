import unittest

from svg_concat.svg.merge_svgs import merge_svgs
from tests.svg import expected_results
from tests.test_helpers import clear_test_folder


def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()


class MergeSvgsTests(unittest.TestCase):
    def setUp(self):
        clear_test_folder.delete_all_files_for_test(MergeSvgsTests.__name__)

    def test_loaded_file_is_merged_correctly(self):
        # Arrange
        files_to_merge = ["test_files\\Sub folder\\Aadhira.svg", "test_files\\Sub folder\\Sub Sub Folder\\Best Man.svg"]
        output_location = "wip\\test_output\\merge_svgs\\test_loaded_file_is_merged_correctly.svg"
        expected_result = expected_results.test_merge_svgs_results[self.test_loaded_file_is_merged_correctly.__name__]

        # Act
        merge_svgs(output_location, True, *files_to_merge)
        result = load_file(output_location)

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
