import unittest

from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from tests.file_discovery.file_filters.mocks.mock_filter import MockFilter


class FilterCollectionTest(unittest.TestCase):
    def setUp(self):
        self.test_collection = FilterCollection()


class UpsertTests(FilterCollectionTest):
    def test_add_file_suffix_sets_file_suffix(self):
        # Arrange
        expected_result = FileSuffixFilter(".svg")
        new_file_suffix = FileSuffixFilter(".svg")

        # Act
        self.test_collection.upsert(new_file_suffix)

        # Assert
        self.assertEqual(expected_result, self.test_collection.file_suffix_filter)

    def test_add_name_filter_sets_name_filter(self):
        # Arrange
        expected_result = NameFilter({"Hello", "World"})
        name_filter = NameFilter({"Hello", "World"})

        # Act
        self.test_collection.upsert(name_filter)

        # Assert
        self.assertEqual(expected_result, self.test_collection.names_filter)

    def test_add_other_filter_adds_filter(self):
        # Arrange
        mock_filter = MockFilter()
        expected_result = {mock_filter}

        # Act
        self.test_collection.upsert(mock_filter)

        # Assert
        self.assertSetEqual(expected_result, self.test_collection.other_filters)

    def test_add_three_other_filter_adds_filters(self):
        mock_filter1 = MockFilter("test 1")
        mock_filter2 = MockFilter("test 2")
        mock_filter3 = MockFilter("test 3")
        expected_result = {mock_filter1, mock_filter2, mock_filter3}

        # Act
        self.test_collection.upsert(mock_filter1)
        self.test_collection.upsert(mock_filter2)
        self.test_collection.upsert(mock_filter3)

        # Assert
        self.assertSetEqual(expected_result, self.test_collection.other_filters)
        self.assertEqual(3, len(self.test_collection.other_filters))

    def test_non_filter_raises_type_error(self):
        # Assert
        with self.assertRaises(TypeError) as ex:
            # Act
            self.test_collection.upsert(None)


class GetTests(FilterCollectionTest):
    def test_get_file_suffix_filter_returns_current_file_suffix_filter(self):
        # Arrange
        expected_result = FileSuffixFilter(".svg")
        self.test_collection.upsert(FileSuffixFilter(".svg"))

        # Act
        result = self.test_collection.get(FileSuffixFilter)

        # Assert
        self.assertEqual(expected_result, result)

    def test_get_name_filter_returns_current_name_filter(self):
        # Arrange
        expected_result = NameFilter({"Hello", "World"})
        name_filter = NameFilter({"Hello", "World"})
        self.test_collection.upsert(name_filter)

        # Act
        result = self.test_collection.get(NameFilter)

        # Assert
        self.assertEqual(expected_result, result)

    def test_get_multiple_other_filters_from_system(self):
        # Arrange
        expected_result = set()
        for i in range(0, 3):
            mock = MockFilter(f"Test {i}")
            expected_result.add(mock)
            self.test_collection.upsert(MockFilter(f"Test {i}"))

        # Act
        result = self.test_collection.get(MockFilter)

        # Assert
        self.assertSetEqual(expected_result, result)

    def test_no_matching_filter_no_default_returns_none(self):
        # Arrange

        # Act
        result = self.test_collection.get(FileSuffixFilter)

        # Assert
        self.assertIsNone(result)

    def test_no_matching_filter_with_default_returns_given_result(self):
        # Arrange
        expected_result = "Hello World"

        # Act
        result = self.test_collection.get(FileSuffixFilter, "Hello World")

        # Assert
        self.assertEqual(expected_result, result)


class LenTests(FilterCollectionTest):
    def test_file_suffix_returns_one(self):
        # Arrange
        expected_result = 1
        file_suffix = FileSuffixFilter(".svg")
        self.test_collection.upsert(file_suffix)

        # Act
        result = len(self.test_collection)

        # Assert
        self.assertEqual(expected_result, result)

    def test_name_filter_returns_one(self):
        # Arrange
        expected_result = 1
        name_filter = NameFilter({"Hello", "World"})
        self.test_collection.upsert(name_filter)

        # Act
        result = len(self.test_collection)

        # Assert
        self.assertEqual(expected_result, result)

    def test_other_filters_counted_appropriately(self):
        # Arrange
        expected_result = 3
        for i in range(0, 3):
            self.test_collection.upsert(MockFilter(f"Test {i}"))

        # Act
        result = len(self.test_collection)

        # Assert
        self.assertEqual(expected_result, result)


class ValuesTests(FilterCollectionTest):
    def test_returns_all_entries_from_object(self):
        # Arrange
        mock_filter1 = MockFilter("test 1")
        mock_filter2 = MockFilter("test 2")
        mock_filter3 = MockFilter("test 3")
        expected_result = [
            mock_filter1,
            mock_filter2,
            mock_filter3,
            FileSuffixFilter(".svg"),
            NameFilter({"Hello", "World"})
        ]
        self.test_collection.upsert(FileSuffixFilter(".svg"))
        self.test_collection.upsert(NameFilter({"Hello", "World"}))
        self.test_collection.upsert(mock_filter1)
        self.test_collection.upsert(mock_filter2)
        self.test_collection.upsert(mock_filter3)

        # Act
        result = self.test_collection.values()

        # Assert
        self.assertCountEqual(expected_result, result)

    def test_empty_object_returns_empty_list(self):
        # Assert
        self.assertListEqual(self.test_collection.values(), [])


if __name__ == '__main__':
    unittest.main()
