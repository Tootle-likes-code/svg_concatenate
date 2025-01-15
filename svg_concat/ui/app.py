import tkinter as tk
import tkinter.ttk as ttk

from svg_concat.ui import shared
from svg_concat.ui.directory_select_frame import DirectorySelectFrame
from svg_concat.ui.filter_frame import FilterFrame
from svg_concat.ui.output_frame import OutputFrame
from svg_concat.ui.report_section_frame import ReportSectionFrame


class App(tk.Tk):
    def __init__(self, save_config_command, load_config_command, **kwargs):
        super().__init__()

        self.title('SVG Concatenate')
        self.columnconfigure(1, weight=1)
        self.columnconfigure(5, weight=1)
        self.rowconfigure(2, weight=1)

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save Config", command=save_config_command)
        file_menu.add_command(label="Load Config", command=load_config_command)

        menubar.add_cascade(label="File", menu=file_menu)

        self.directory_to_search_frame = (
            DirectorySelectFrame(self, "Directory to Search", kwargs["initial_directory_listener"]))
        self.filter_frame = FilterFrame(self, kwargs["new_filter"])
        self.directory_to_output = OutputFrame(
            self,
            kwargs["output_directory_listener"],
            kwargs["svg_output_listener"],
            kwargs["report_output_listener"]
        )
        self.run_button = ttk.Button(self, text="Concatenate", command=kwargs["run_button_action"],
                                     padding=shared.X_PADDING, state=tk.DISABLED)
        separator = ttk.Separator(self, orient=tk.VERTICAL)
        self.report_section = ReportSectionFrame(self)

        self.directory_to_search_frame.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW,
                                            padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.filter_frame.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW,
                               padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.directory_to_output.grid(row=2, column=0, columnspan=4, sticky=tk.NSEW,
                                      padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.run_button.grid(row=3, column=3, sticky=tk.E, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        separator.grid(row=0, column=4, rowspan=4, sticky=tk.NS, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.report_section.grid(row=0, column=5, columnspan=2, rowspan=4, sticky=tk.NSEW,
                                 padx=shared.X_PADDING, pady=shared.Y_PADDING)

        self.config(menu=menubar)
        self.directory_to_search_frame.bind()

    def update_filters(self, filters):
        self.filter_frame.update_filters(filters)

    def update_run_button_state(self, enabled: bool):
        if enabled:
            self.run_button.config(state=tk.NORMAL)
        else:
            self.run_button.config(state=tk.DISABLED)

    def update_ui(self, initial_directory, output_directory, svg_file, report_file):
        self.directory_to_search_frame.update_text(initial_directory)
        self.directory_to_output.update_ui(output_directory, svg_file, report_file)

    def update_report(self, is_success, is_fatal, messages):
        self.report_section.update_report(is_success, is_fatal, messages)
