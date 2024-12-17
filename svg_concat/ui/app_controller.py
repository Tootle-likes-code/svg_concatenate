from svg_concat.file_discovery.file_filters.filter_types import FilterType
from svg_concat.ui.app import App
from svg_concat.ui.models.filters_model import FiltersModel
from svg_concat.ui.new_filter_window import NewFilterWindow


class AppController:
    def __init__(self, filter_model: FiltersModel, app: App):
        self.filter_model = filter_model
        self.app = app
        self.app.add_filter_button(self.new_filter_start)
        self.new_filter_window: NewFilterWindow
        self._setup_listeners()

    def _setup_listeners(self):
        self.filter_model.subscribe_to_changes(self)

    @property
    def filters(self):
        return list(self.filter_model.filters.values())

    def update_file_suffix_filter(self, file_suffix_filter: str):
        self.filter_model.update_file_suffix_filter(file_suffix_filter)

    def update_filters(self):
        self.app.update_filters(self.filters)

    def new_filter_start(self):
        self.new_filter_window = (
            NewFilterWindow(self.app,
                            create_filter=self.create_filter,
                            update_file_suffix_action=self.update_file_suffix_filter)
        )

    def create_filter(self, filter_type: FilterType, *args):
        self.filter_model.create_filter(filter_type, *args)

    def update_file_suffix_action(self, file_suffix_filter: str):
        self.filter_model.update_file_suffix_filter(file_suffix_filter)
