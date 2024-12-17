import unittest

from svg_concat.file_discovery.file_filters.inverse_filter import InverseFilter
from tests.file_discovery.file_filters.mocks.mock_filter import MockFilter


class InverseCriterionTest(unittest.TestCase):
    pass


class IsValidTests(unittest.TestCase):
    def test_contained_criteria_returns_true_is_valid_returns_false(self):
        # Arrange
        mock_criteria = MockFilter()
        test_criterion = InverseFilter(mock_criteria)

        # Act
        result = test_criterion.is_valid("Test")

        # Assert
        self.assertFalse(result)

    def test_contained_criteria_returns_false_is_valid_returns_true(self):
        # Arrange
        mock_criteria = MockFilter(False)
        test_criterion = InverseFilter(mock_criteria)

        # Act
        result = test_criterion.is_valid("Test")

        # Assert
        self.assertTrue(result)
