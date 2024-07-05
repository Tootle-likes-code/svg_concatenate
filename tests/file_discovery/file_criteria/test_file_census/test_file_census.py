import unittest

from svg_concat.file_discovery.file_census import FileCensus
from tests.file_discovery.file_criteria.mocks.mock_criterion import MockCriterion


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
        self.assertSetEqual(set(), test_census.criteria)

    def test_file_criteria_is_value_sets_to_value(self):
        # Arrange
        expected_result = {MockCriterion(True), MockCriterion()}

        # Act
        test_census = FileCensus("test", criteria={MockCriterion(True), MockCriterion()})

        # Assert
        self.assertSetEqual(expected_result, test_census.criteria)


if __name__ == '__main__':
    unittest.main()
