class ReadOnlyList:
    def __init__(self, data: list[str]):
        self._data = tuple(data)

    @property
    def data(self):
        return self._data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __eq__(self, other: tuple):
        if not isinstance(other, tuple):
            return False
        return self._data == other

    def __str__(self):
        text = "\n".join(self._data)
        return text
