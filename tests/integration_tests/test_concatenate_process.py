import json
import unittest
from pathlib import Path

from svg_concat.merge.concatenate_service import ConcatenateService
from tests.integration_tests import expected_results
from tests.test_helpers import merge_config_builder

DEFAULT_TEST_FOLDER = Path("test_files")


class ConcatenateProcessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            with open("test_config.json") as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            print("Test config not found, cannot run tests")
            exit(1)

        cls.test_output_directories = {
            "test_duplicate_names_are_represented_appropriately": Path(config["test_output_directory"]).joinpath(
                "test_duplicate_names_are_represented_appropriately.svg"),
        }

    @classmethod
    def tearDownClass(cls):
        for test_file in cls.test_output_directories.values():
            #test_file.unlink()
            pass

    def setUp(self):
        self.test_concatenate_service = ConcatenateService()


class ValidConcatenateTests(ConcatenateProcessTests):
    def test_duplicate_names_are_represented_appropriately(self):
        # Arrange
        expected_result = expected_results.duplicate_entries_expected_result
        test_config = (merge_config_builder.create()
                       .with_initial_directory(DEFAULT_TEST_FOLDER)
                       .with_name_filter("Aaden", "Aaden", "Aaden")
                       .with_file_suffix_filter(".svg")
                       .with_svg_file(
            self.test_output_directories[self.test_duplicate_names_are_represented_appropriately.__name__])
                       .build())

        # Act
        self.test_concatenate_service.concatenate(test_config)
        result = None
        with open(self.test_output_directories[self.test_duplicate_names_are_represented_appropriately.__name__]) as f:
            result = f.read()

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
