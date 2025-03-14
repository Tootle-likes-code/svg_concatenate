import unittest

from svg_concat.file_discovery import census_result_builder
from svg_concat.file_discovery.census_result_builder import CensusResultBuilder
from svg_concat.file_discovery.file_census import FileCensus
from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from tests.file_discovery.file_filters.test_file_filter.test_file_census import FileCensusTests
from tests.test_helpers import file_helper


@staticmethod
def create_result_with_all_files_found(builder: CensusResultBuilder = None):
    if builder is None:
        builder = census_result_builder.create_census_result()

    return (builder.with_found_file(file_helper.get_path("test_files/Sub folder/Aaden.svg"))
            .with_found_file(file_helper.get_path("test_files/Sub folder/Aadhira.svg"))
            .with_found_file(file_helper.get_path("test_files/Sub folder/Rūta.svg"))
            .with_found_file(file_helper.get_path("test_files/Sub folder/Sub Sub Folder/Best Man.svg"))
            .with_found_file(file_helper.get_path("test_files/Sub folder/Sub Sub Folder/Maid of Honour.svg"))
            .with_found_file(file_helper.get_path("test_files/Other Sub Folder/Aaliyah.svg"))
            .with_found_file(file_helper.get_path("test_files/Aakash.svg"))
            .with_found_file(file_helper.get_path("test_files/test1.txt"))
            .with_found_file(file_helper.get_path("test_files/Aaleah.svg"))
            .build())


class SearchTests(FileCensusTests):
    pass


class FindAllFilesTests(SearchTests):
    def test_no_filter_census_result_for_every_file(self):
        # Arrange
        expected_result = create_result_with_all_files_found()
        file_path = file_helper.get_path("test_files/")
        test_census = FileCensus(str(file_path))

        # Act
        results = test_census.search_directory()

        # Assert
        self.assertSetEqual(expected_result.found_files, results.found_files)

    def test_no_filter_census_no_missing_files(self):
        # Arrange
        test_census = FileCensus("test_files")

        # Act
        result = test_census.search_directory()

        # Assert
        self.assertSetEqual(set(), result.missing_files)

    def test_file_filter_census_all_found_files(self):
        # Assert
        expected_result = (census_result_builder.create_census_result()
                           .with_found_file(file_helper.get_path("test_files/Sub folder/Aaden.svg"))
                           .with_found_file(file_helper.get_path("test_files/Sub folder/Rūta.svg"))
                           .with_found_file(file_helper.get_path("test_files/Other Sub Folder/Aaliyah.svg"))
                           .with_found_file(file_helper.get_path("test_files/test1.txt"))
                           .with_found_file(file_helper.get_path("test_files/Aaleah.svg"))
                           .build())
        names = {"Aaden.svg", "Rūta.svg", "Aaleah.svg", "Aaliyah.svg", "test1.txt"}
        test_filter = NameFilter(names)
        test_census = FileCensus(str(file_helper.get_path("test_files/")), {test_filter})

        # Actfile_helper.get_path(
        result = test_census.search_directory()

        # Assert
        self.assertSetEqual(expected_result.found_files, result.found_files)

    def test_file_filter_census_some_missing_files(self):
        # Arrange
        expected_result = (census_result_builder.create_census_result()
                           .with_missing_file("new.txt")
                           .build())
        test_census = FileCensus("test_files", files_to_find={"new.txt"})

        # Act
        result = test_census.search_directory()

        # Assert
        self.assertSetEqual(expected_result.missing_files, result.missing_files)


if __name__ == '__main__':
    unittest.main()
