import unittest

from svg_concat.file_discovery.file_census import FileCensus
from tests.file_discovery.file_filters.mocks.mock_filter import MockFilter


class FileCensusTests(unittest.TestCase):
    def setUp(self):
        self.test_census = FileCensus("Starting Directory", )


class ConstructorTests(FileCensusTests):
    def test_sets_starting_directory(self):
        # Arrange
        expected_result = "expected result"

        # Act
        test_census = FileCensus("expected result")

        # Assert
        self.assertEqual(expected_result, test_census.starting_directory)

    def test_file_criteria_is_none_sets_to_empty_set(self):
        # Act
        test_census = FileCensus("test")

        # Assert
        self.assertListEqual([], test_census.filters)

    def test_file_criteria_is_value_sets_to_value(self):
        # Arrange
        expected_result = [MockFilter(result=True), MockFilter()]

        # Act
        test_census = FileCensus("test", filters=[MockFilter(result=True), MockFilter()])

        # Assert
        self.assertListEqual(expected_result, test_census.filters)


if __name__ == '__main__':
    unittest.main()
