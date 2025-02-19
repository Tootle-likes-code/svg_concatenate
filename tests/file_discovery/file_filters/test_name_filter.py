import unittest
from pathlib import Path

from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from tests.file_discovery.file_filters.mocks.mock_filter import MockFilter


class NameFilterTests(unittest.TestCase):
    def setUp(self):
        pass


class NamesWithCountTests(NameFilterTests):
    def test_duplicate_names_give_incresed_count(self):
        # Arrange
        expected_result = {"Joe": 2, "Anya": 1}
        test_filter = NameFilter(["Joe", "Joe", "Anya"])
        
        # Act
        result = test_filter.names_with_count
        
        # Assert
        self.assertDictEqual(expected_result, result)


class IsValidTests(NameFilterTests):
    def test_contained_name_is_passed_returns_true(self):
        # Arrange
        test_filter = NameFilter(['test_name'])

        # Act
        result = test_filter.is_valid(Path('test_name'))

        # Assert
        self.assertTrue(result)

    def test_not_contained_name_is_passed_returns_false(self):
        test_filter = NameFilter(['test_name'])

        # Act
        result = test_filter.is_valid(Path('not_test_name'))

        # Assert
        self.assertFalse(result)


class MergeTests(NameFilterTests):
    def test_first_names_replaced_by_other(self):
        # Arrange
        expected_result = {"Test 3", "Test 4"}
        filter_1 = NameFilter({"Test", "Test 2"})
        filter_2 = NameFilter({"Test 3", "Test 4"})

        # Act
        filter_1.merge(filter_2)

        # Assert
        self.assertSetEqual(expected_result, filter_1.names)

    def test_raises_type_error_when_not_correct_type(self):
        # Arrange
        filter_1 = NameFilter({"Test", "Test 2"})
        filter_2 = MockFilter()

        # Assert
        with self.assertRaises(TypeError) as ex:
            # Act
            filter_1.merge(filter_2)
