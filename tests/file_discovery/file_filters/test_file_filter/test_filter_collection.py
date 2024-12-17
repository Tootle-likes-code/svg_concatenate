import unittest

from svg_concat.file_discovery.file_filters.filter import Filter
from svg_concat.file_discovery.file_filters.filter_collection import FilterCollection
from svg_concat.file_discovery.file_filters.filter_types import FilterType


class FilterCollectionTest(unittest.TestCase):
    def setUp(self):
        self.test_collection = FilterCollection()


class ItemTest(FilterCollectionTest):
    def test_non_filter_value_raises_type_error(self):
        # Assert
        with self.assertRaises(TypeError) as ex:
            # Act
            # Assert
            self.test_collection[FilterType.FILE_SUFFIX_FILTER] = "hello world"

    def test_adding_valid_filter(self):
        """Test adding a valid Filter subclass instance."""
        collection = FilterCollection()
        filter_instance = MockValidFilter()
        collection['valid_filter'] = filter_instance
        self.assertIn('valid_filter', collection)
        self.assertIs(collection['valid_filter'], filter_instance)

    def test_updating_with_valid_filters(self):
        """Test that update() works with valid filters."""
        collection = FilterCollection()
        valid_filters = {
            'filter1': MockValidFilter(),
            'filter2': MockValidFilter(),
        }
        collection.update(valid_filters)
        self.assertIn('filter1', collection)
        self.assertIn('filter2', collection)

    def test_updating_with_invalid_filter_raises_error(self):
        """Test that update() raises TypeError if a value is not a Filter subclass."""
        collection = FilterCollection()
        valid_filter = MockValidFilter()
        invalid_filters = {
            'filter1': valid_filter,
            'filter2': MockInvalidFilter(),
        }
        with self.assertRaises(TypeError):
            collection.update(invalid_filters)


# Mock Filter Subclasses
class MockValidFilter(Filter):
    def is_valid(self, file_name: str) -> bool:
        return file_name == "True"

    def merge(self, other_filter: Filter):
        pass


class MockInvalidFilter:
    pass


class ConstructorTests(FilterCollectionTest):
    def test_initialization_with_no_items(self):
        """Test that FilterCollection initializes empty."""
        collection = FilterCollection()
        self.assertEqual(len(collection), 0)


class SetItemTests(FilterCollectionTest):
    def test_setitem_type_checking(self):
        """Test that __setitem__ performs type checking."""
        collection = FilterCollection()
        valid_filter = MockValidFilter()
        collection['valid'] = valid_filter
        with self.assertRaises(TypeError):
            collection['invalid'] = MockInvalidFilter()

    def test_multiple_updates_with_valid_filters(self):
        """Test multiple updates with valid filters."""
        collection = FilterCollection()
        valid_filters_1 = {'filter1': MockValidFilter()}
        valid_filters_2 = {'filter2': MockValidFilter()}
        collection.update(valid_filters_1)
        self.assertIn('filter1', collection)
        collection.update(valid_filters_2)
        self.assertIn('filter2', collection)

    def test_valid_initial_values(self):
        """Test dictionary behavior after adding valid filters."""

        class GoodFilterCollection(FilterCollection):
            def __init__(self):
                super().__init__()
                self['valid1'] = MockValidFilter()
                self['valid2'] = MockValidFilter()

        collection = GoodFilterCollection()
        self.assertIn('valid1', collection)
        self.assertIn('valid2', collection)


class UpsertTests(FilterCollectionTest):
    def test_upsert_adds_new_filter(self):
        """Test upsert adds a new filter if the key does not already exist."""
        collection = FilterCollection()
        valid_filter = MockValidFilter()
        collection.upsert('new_filter', valid_filter)

        self.assertIn('new_filter', collection)
        self.assertIs(collection['new_filter'], valid_filter)

    def test_upsert_merges_existing_filter(self):
        """Test upsert merges with an existing filter."""
        collection = FilterCollection()

        class MergeableFilter(MockValidFilter):
            def __init__(self):
                self.merged = False

            def merge(self, other):
                self.merged = True

        existing_filter = MergeableFilter()
        collection['existing_filter'] = existing_filter
        new_filter = MockValidFilter()

        collection.upsert('existing_filter', new_filter)

        self.assertTrue(existing_filter.merged)  # Verify merge() was called

    def test_upsert_with_invalid_value_raises_error(self):
        """Test upsert raises a TypeError when an invalid filter is provided."""
        collection = FilterCollection()
        invalid_filter = MockInvalidFilter()

        with self.assertRaises(TypeError):
            collection.upsert('invalid_filter', invalid_filter)

    def test_upsert_does_not_replace_existing_key(self):
        """Test upsert does not replace existing key but merges."""
        collection = FilterCollection()

        class MergeableFilter(MockValidFilter):
            def __init__(self):
                self.merged = False
                self.count = 1

            def merge(self, other):
                self.count += 1

        existing_filter = MergeableFilter()
        collection['existing'] = existing_filter

        new_filter = MockValidFilter()
        collection.upsert('existing', new_filter)

        self.assertEqual(existing_filter.count, 2)  # Merged, so count increments
        self.assertIs(collection['existing'], existing_filter)  # No replacement occurred


if __name__ == '__main__':
    unittest.main()
