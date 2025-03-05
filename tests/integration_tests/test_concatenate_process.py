import unittest
from pathlib import Path

from svg_concat.merge.concatenate_service import ConcatenateService
from tests.integration_tests import expected_results
from tests.test_helpers import merge_config_builder

DEFAULT_TEST_FOLDER = Path("test_files")


class ConcatenateProcessTests(unittest.TestCase):
    def setUp(self):
        self.test_concatenate_service = ConcatenateService()


class ValidConcatenateTests(ConcatenateProcessTests):
    def setUp(self):
        super().setUp()
        self.test_file_path = Path(ValidConcatenateTests.__name__ + ".svg")

        self._clear_files()

    def _clear_files(self):
        if self.test_file_path.exists():
            self.test_file_path.unlink()

    def tearDown(self):
        self._clear_files()

    def test_duplicate_names_are_in_file(self):
        # Arrange
        expected_result = expected_results.duplicate_entries_expected_result
        test_config = (merge_config_builder.create()
                       .with_initial_directory(DEFAULT_TEST_FOLDER)
                       .with_name_filter("Aaden", "Aaden", "Aaden")
                       .with_file_suffix_filter(".svg")
                       .with_svg_file(self.test_file_path)
                       .build())

        # Act
        self.test_concatenate_service.concatenate(test_config)

        # Assert
        self.assertTrue(self.test_file_path.exists())
        result = None
        with open(self.test_file_path) as f:
            result = f.read()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
