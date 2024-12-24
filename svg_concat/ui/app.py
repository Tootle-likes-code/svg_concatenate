import tkinter as tk
import tkinter.ttk as ttk

from svg_concat.ui import shared
from svg_concat.ui.directory_select_frame import DirectorySelectFrame
from svg_concat.ui.filter_frame import FilterFrame


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__()

        self.title('SVG Concatenate')

        self.directory_to_search_frame = (
            DirectorySelectFrame(self, "Directory to Search", kwargs["initial_directory_listener"]))
        self.filter_frame = FilterFrame(self, kwargs["new_filter"])
        self.directory_to_output = (
            DirectorySelectFrame(self, "Directory to Save", kwargs["output_directory_listener"]))
        self.run_button = ttk.Button(self, text="Concatenate", command=kwargs["run_button_action"], padding=shared.X_PADDING,
                                state=tk.DISABLED)
        separator = ttk.Separator(self)

        self.directory_to_search_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.E)
        self.filter_frame.pack(side=tk.TOP, fill=tk.X, anchor=tk.E)
        self.directory_to_output.pack(side=tk.TOP, fill=tk.X)
        self.run_button.pack(side=tk.TOP, anchor=tk.E, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        separator.pack(side=tk.TOP, fill=tk.X, anchor=tk.E,
                       padx=shared.SEPARATOR_PADDING, pady=shared.SEPARATOR_PADDING)

        self.directory_to_search_frame.bind()

    def update_filters(self, filters):
        self.filter_frame.update_filters(filters)

    def update_run_button_state(self, enabled: bool):
        if enabled:
            self.run_button.config(state=tk.NORMAL)
        else:
            self.run_button.config(state=tk.DISABLED)
