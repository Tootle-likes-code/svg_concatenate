import unittest

from svg_concat.file_discovery.file_criteria.name_criterion import NameCriterion


class NameCriterionTests(unittest.TestCase):
    def setUp(self):
        pass


class IsValidTests(NameCriterionTests):
    def test_contained_name_is_passed_returns_true(self):
        # Arrange
        test_criterion = NameCriterion(['test_name'])

        # Act
        result = test_criterion.is_valid('test_name')

        # Assert
        self.assertTrue(result)

    def test_not_contained_name_is_passed_returns_false(self):
        test_criterion = NameCriterion(['test_name'])

        # Act
        result = test_criterion.is_valid('not_test_name')

        # Assert
        self.assertFalse(result)
