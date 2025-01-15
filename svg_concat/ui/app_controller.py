from svg_concat.file_discovery.filter_types import FilterType
from svg_concat.job_tasks.job_result import JobResult
from svg_concat.merge import merge_config
from svg_concat.ui.app import App
from svg_concat.merge.concatenate_service import ConcatenateService
from svg_concat.ui.models.config_service import ConfigService
from svg_concat.ui.models.filters_model import FiltersModel
from svg_concat.ui.new_filter_window import NewFilterWindow


class AppController:
    def __init__(self, filter_model: FiltersModel, concatenate_service: ConcatenateService,
                 config_service: ConfigService):
        self.filter_model = filter_model
        self.concatenate_service = concatenate_service
        self.concatenate_service.subscribe_to_failures(self._handle_result)
        self.concatenate_service.subscribe_to_successes(self._handle_result)

        self.config_service = config_service

        self.app: App | None = None

        self.new_filter_window: NewFilterWindow | None = None
        self._setup_listeners()

        self.initial_directory: str = ""
        self.output_directory: str = ""
        self.svg_file: str = ""
        self.report_file: str = ""

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
            self.save_config,
            self.load_config,
            new_filter=self.new_filter_start,
            initial_directory_listener=self.update_initial_directory,
            output_directory_listener=self.update_output_directory,
            run_button_action=self.concatenate,
            svg_output_listener=self.update_svg_output,
            report_output_listener=self.update_report_output
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
        svg_file_is_valid = self.svg_file is not None and self.svg_file != ""
        report_file_is_valid = self.report_file is not None and self.report_file != ""

        enabled = (
                initial_directory_is_valid
                and output_directory_is_valid
                and svg_file_is_valid
                and report_file_is_valid
        )
        self.app.update_run_button_state(enabled)

    def update_initial_directory(self, path: str) -> None:
        self.initial_directory = path

        self.update_run_button_state()

    def update_output_directory(self, path: str) -> None:
        self.output_directory = path

        self.update_run_button_state()

    def update_svg_output(self, path: str) -> None:
        self.svg_file = path

        self.update_run_button_state()

    def update_report_output(self, path: str) -> None:
        self.report_file = path

        self.update_run_button_state()

    def concatenate(self) -> None:
        self.concatenate_service.concatenate(self._create_merge_config())

    def _create_merge_config(self):
        return merge_config.create(self.initial_directory, self.output_directory,
                                   self.svg_file, self.report_file, self.filter_model.get())

    def _handle_result(self, result: JobResult):
        self.app.update_report(result.is_success, result.is_fatal, result.messages)

    def save_config(self):
        self.config_service.save_config(self._create_merge_config())

    def load_config(self):
        config = self.config_service.load_config()
        self.initial_directory = config.initial_directory
        self.output_directory = config.output_directory
        self.svg_file = config.svg_file
        self.report_file = config.report_path
        self.filter_model.set(config.filters)

        self._update_app()

    def _update_app(self):
        self.app.update_ui(
            self.initial_directory,
            self.output_directory,
            self.svg_file,
            self.report_file
        )
