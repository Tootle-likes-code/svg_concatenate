from svg_concat.file_discovery.filter_types import FilterType
from svg_concat.ui.app import App
from svg_concat.ui.models.filters_model import FiltersModel
from svg_concat.ui.new_filter_window import NewFilterWindow


class AppController:
    def __init__(self, filter_model: FiltersModel):
        self.filter_model = filter_model
        self.app: App | None = None

        self.new_filter_window: NewFilterWindow | None = None
        self._setup_listeners()

        self.initial_directory: str = ""
        self.output_directory: str = ""

    def _setup_listeners(self):
        self.filter_model.subscribe_to_changes(self)

    @property
    def filters(self):
        return self.filter_model.filters

    @property
    def file_suffixes(self):
        return self.filter_model.file_suffixes

    def create_app(self):
        self.app = App(
            new_filter=self.new_filter_start,
            initial_directory_listener=self.update_initial_directory,
            output_directory_listener=self.update_output_directory,
            run_button_action=self.concatenate
        )

    def update_file_suffix_filter(self, file_suffix_filter: str):
        self.filter_model.update_file_suffix_filter(file_suffix_filter)

    def update_filters(self):
        self.app.update_filters(self.filters)

    def new_filter_start(self):
        self.new_filter_window = (
            NewFilterWindow(self.app,
                            create_filter=self.create_filter,
                            create_inverse_filter=self.create_inverse_filter,
                            update_file_suffix_action=self.update_file_suffix_filter,
                            file_suffixes=self.filter_model.file_suffixes,
                            file_names=self.filter_model.file_names
                            )
        )

    def create_filter(self, filter_type: FilterType, *args):
        self.filter_model.create_filter(filter_type, *args)

    def create_inverse_filter(self, inverted_filter_type: FilterType, *args):
        self.filter_model.create_inverted_filter(inverted_filter_type, *args)

    def update_file_suffix_action(self, file_suffix_filter: str):
        self.filter_model.update_file_suffix_filter(file_suffix_filter)

    def update_run_button_state(self) -> None:
        initial_directory_is_valid = self.initial_directory is not None and self.initial_directory != ""
        output_directory_is_valid = self.output_directory is not None and self.output_directory != ""

        enabled = initial_directory_is_valid and output_directory_is_valid
        self.app.update_run_button_state(enabled)

    def update_initial_directory(self, path: str) -> None:
        self.initial_directory = path

        self.update_run_button_state()


    def update_output_directory(self, path: str) -> None:
        self.output_directory = path

        self.update_run_button_state()

    def concatenate(self):
        print("Concatenate!!")
        pass
