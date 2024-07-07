import unittest

from svg_concat.file_discovery.file_criteria.inverse_criterion import InverseCriterion
from tests.file_discovery.file_criteria.mocks.mock_criterion import MockCriterion


class InverseCriterionTest(unittest.TestCase):
    pass


class IsValidTests(unittest.TestCase):
    def test_contained_criteria_returns_true_is_valid_returns_false(self):
        # Arrange
        mock_criteria = MockCriterion()
        test_criterion = InverseCriterion(mock_criteria)

        # Act
        result = test_criterion.is_valid("Test")

        # Assert
        self.assertFalse(result)

    def test_contained_criteria_returns_false_is_valid_returns_true(self):
        # Arrange
        mock_criteria = MockCriterion(False)
        test_criterion = InverseCriterion(mock_criteria)

        # Act
        result = test_criterion.is_valid("Test")

        # Assert
        self.assertTrue(result)
