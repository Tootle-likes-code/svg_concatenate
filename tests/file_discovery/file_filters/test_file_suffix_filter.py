import unittest

from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter


class FileSuffixFilterTests(unittest.TestCase):
    def setUp(self):
        self.test_criterion = FileSuffixFilter([".svg", ".txt"])


class ConstructorTest(FileSuffixFilterTests):
    def setUp(self):
        self.file_suffixes = [".svg", " svg"]

    def test_leading_spaces_are_trimmed(self):
        # Arrange
        expected_result = "svg"

        # Act
        result = FileSuffixFilter([" svg"])

        # Assert
        self.assertTrue(expected_result in result.allowed_suffixes, f"Spaces were not trimmed. {result.allowed_suffixes}")

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
        result = self.test_criterion.is_valid("test.svg")

        # Assert
        self.assertTrue(result)

    def test_returns_false_if_file_does_not_use_suffix(self):
        # Assert
        self.assertFalse(self.test_criterion.is_valid("test.png"))

    def test_does_not_return_none_if_file_does_not_use_suffix(self):
        # Assert
        self.assertIsNotNone(self.test_criterion.is_valid("test.png"))

    def test_returns_true_if_file_is_in_allowed_but_not_the_first(self):
        # Assert
        self.assertTrue(self.test_criterion.is_valid("test.txt"))


if __name__ == '__main__':
    unittest.main()
