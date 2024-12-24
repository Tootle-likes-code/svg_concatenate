import tkinter as tk
import tkinter.ttk as ttk

from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from svg_concat.ui import shared
from svg_concat.ui.create_filter_frame import CreateFilterFrame
from svg_concat.ui.new_file_name_filter_frame import NewNameFilterFrame
from svg_concat.ui.new_file_suffix_filter_frame import NewFileSuffixFilterFrame
from svg_concat.ui.view_models import filter_view_model_factory


class NewInverseFilterFrame(CreateFilterFrame):
    def __init__(self, parent, create_filter_action, update_file_suffix_action):
        super().__init__(parent)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        filter_names = [name for name in filter_view_model_factory.inverse_names_to_types_mapping.keys()]
        self.selected_filter_type = tk.StringVar()
        self.selected_filter_type.set(filter_names[0])

        drop_down_label = ttk.Label(self, text="Select Inverted Filter:")
        filter_combo = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.selected_filter_type,
            values=filter_names
        )
        filter_combo.bind("<<ComboboxSelected>>", self._show_selected_frame)

        file_suffix_filter_frame = NewFileSuffixFilterFrame(
            self,
            create_filter_action,
            update_file_suffix_action,
            ""
        )
        name_filter_frame = NewNameFilterFrame(
            self,
            [],
            create_filter_action
        )

        self._frames = {
            FileSuffixFilter: file_suffix_filter_frame,
            NameFilter: name_filter_frame
        }

        drop_down_label.grid(row=0, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.EW)
        filter_combo.grid(row=0, column=1, columnspan=2, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.EW)
        file_suffix_filter_frame.grid(row=1, column=0, columnspan=3, padx=shared.INTERIOR_PADDING,
                                      pady=shared.INTERIOR_PADDING, sticky=tk.NSEW)
        name_filter_frame.grid(row=1, column=0, columnspan=3,
                               padx=shared.INTERIOR_PADDING, pady=shared.INTERIOR_PADDING, sticky=tk.NSEW)

        self._show_selected_frame(None)

    def _show_selected_frame(self, _):
        selected_frame = self._selected_frame()
        selected_frame.tkraise()

    def _selected_frame(self) -> CreateFilterFrame:
        selected_filter = self.selected_filter_type.get()
        filter_class = filter_view_model_factory.inverse_names_to_types_mapping[selected_filter]
        return self._frames[filter_class]

    def create_filter(self) -> None:
        self._selected_frame().create_filter()

    def paste(self) -> None:
        self._selected_frame().paste()
