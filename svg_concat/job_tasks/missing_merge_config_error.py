class MissingMergeConfigError(Exception):
    def __init__(self):
        super().__init__("Missing Merge Config")
