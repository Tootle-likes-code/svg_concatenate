from svg_concat.file_discovery.file_filters.filter import Filter


class FilterViewModel:
    def __init__(self, criterion: Filter, name: str, tooltip_text: str):
        self.criterion = criterion
        self.name = name
        self.tooltip_text = tooltip_text

    def __str__(self):
        return self.name
