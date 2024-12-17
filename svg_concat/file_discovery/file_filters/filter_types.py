from enum import Enum


class FilterType(Enum):
    FILE_SUFFIX_FILTER = 0,
    FILE_NAME_FILTER = 1,
    INVERSE_FILTER = 2