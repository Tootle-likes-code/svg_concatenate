from svg_concat.file_discovery.file_filters.filter import Filter


class MockFilter(Filter):
    def __init__(self, name: str = "", result: bool = True):
        self.result = result
        self.name = name

    @classmethod
    def create_dummy_instance(cls):
        return MockFilter()

    def __str__(self):
        return f"MockFilter(Name: {self.name}, Result: {self.result}4)"

    def __eq__(self, other):
        return self.result == other.result and self.name == other.name

    def __hash__(self):
        return hash(hash(self.name) + hash(self.result))

    def is_valid(self, file_name: str) -> bool:
        return self.result

    def merge(self, other: 'MockFilter'):
        pass

    def to_json(self) -> str:
        pass
