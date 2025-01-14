import unittest
from pathlib import Path

from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from tests.file_discovery.file_filters.mocks.mock_filter import MockFilter


class FileSuffixFilterTests(unittest.TestCase):
    def setUp(self):
        self.test_filter = FileSuffixFilter([".svg", ".txt"])


class ConstructorTest(FileSuffixFilterTests):
    def setUp(self):
        self.file_suffixes = [".svg", " svg"]

    def test_leading_spaces_are_trimmed(self):
        # Arrange
        expected_result = "svg"

        # Act
        result = FileSuffixFilter([" svg"])

        # Assert
        self.assertTrue(expected_result in result.allowed_suffixes,
                        f"Spaces were not trimmed. {result.allowed_suffixes}")

    def test_dots_are_trimmed(self):
        # Arrange
        expected_result = "svg"

        # Act
        result = FileSuffixFilter([".svg"])

        # Assert
        self.assertTrue(expected_result in result.allowed_suffixes, f"Dots are not trimmed. {result.allowed_suffixes}")

    def test_no_duplicates_returned(self):
        # Arrange
        expected_result = {"svg"}

        # Act
        result = FileSuffixFilter(self.file_suffixes)

        # Assert
        self.assertSetEqual(result.allowed_suffixes, expected_result)


class IsValidTests(FileSuffixFilterTests):
    def test_returns_true_if_file_ends_with_valid_suffix(self):
        # Act
        result = self.test_filter.is_valid(Path("test.svg"))

        # Assert
        self.assertTrue(result)

    def test_returns_false_if_file_does_not_use_suffix(self):
        # Assert
        self.assertFalse(self.test_filter.is_valid(Path("test.png")))

    def test_does_not_return_none_if_file_does_not_use_suffix(self):
        # Assert
        self.assertIsNotNone(self.test_filter.is_valid(Path("test.png")))

    def test_returns_true_if_file_is_in_allowed_but_not_the_first(self):
        # Assert
        self.assertTrue(self.test_filter.is_valid(Path("test.txt")))


class MergeTests(FileSuffixFilterTests):
    def test_replaces_previous_set(self):
        # Arrange
        expected_result = {"svg2", "txt2"}
        filter_1 = FileSuffixFilter([".svg", ".txt"])
        filter_2 = FileSuffixFilter([".svg2", ".txt2"])

        # Act
        filter_1.merge(filter_2)

        # Assert
        self.assertSetEqual(expected_result, filter_1.allowed_suffixes)

    def test_raises_type_error_when_not_correct_type(self):
        # Arrange
        filter_1 = FileSuffixFilter([".svg", ".txt"])
        filter_2 = MockFilter()

        # Assert
        with self.assertRaises(TypeError) as ex:
            # Act
            filter_1.merge(filter_2)


if __name__ == '__main__':
    unittest.main()
