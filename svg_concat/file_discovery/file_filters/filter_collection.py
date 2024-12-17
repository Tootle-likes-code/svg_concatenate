from svg_concat.file_discovery.file_filters.filter import Filter


class FilterCollection(dict):
    def __init__(self):
        super().__init__()
        for value in self.values():
            self._check_value(value)

    def _check_value(self, value):
        if not isinstance(value, Filter) or not issubclass(type(value), Filter):
            raise TypeError(f'{value} is not a subclass of {Filter.__name__}')

    def __setitem__(self, key, value):
        self._check_value(value)
        super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            self._check_value(value)
        super().update(*args, **kwargs)

    def upsert(self, key, value):
        if key not in self:
            self[key] = value
        else:
            self[key].merge(value)
