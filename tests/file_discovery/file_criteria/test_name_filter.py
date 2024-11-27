import unittest

from svg_concat.file_discovery.file_filters.name_filter import NameFilter


class NameFilterTests(unittest.TestCase):
    def setUp(self):
        pass


class IsValidTests(NameFilterTests):
    def test_contained_name_is_passed_returns_true(self):
        # Arrange
        test_criterion = NameFilter(['test_name'])

        # Act
        result = test_criterion.is_valid('test_name')

        # Assert
        self.assertTrue(result)

    def test_not_contained_name_is_passed_returns_false(self):
        test_criterion = NameFilter(['test_name'])

        # Act
        result = test_criterion.is_valid('not_test_name')

        # Assert
        self.assertFalse(result)
