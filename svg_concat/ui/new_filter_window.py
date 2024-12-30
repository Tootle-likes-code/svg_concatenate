import tkinter as tk
from tkinter import ttk

from svg_concat.file_discovery.file_filters.file_suffix_filter import FileSuffixFilter
from svg_concat.file_discovery.file_filters.inverse_filter import InverseFilter
from svg_concat.file_discovery.file_filters.name_filter import NameFilter
from svg_concat.ui import shared
from svg_concat.ui.create_filter_frame import CreateFilterFrame
from svg_concat.ui.new_file_name_filter_frame import NewNameFilterFrame
from svg_concat.ui.new_file_suffix_filter_frame import NewFileSuffixFilterFrame
from svg_concat.ui.new_inverse_filter_frame import NewInverseFilterFrame
from svg_concat.ui.view_models import filter_view_model_factory


class NewFilterWindow(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args)
        self._parent = parent
        self.title("New Filter")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.selected_filter_type = tk.StringVar()

        file_suffix_filter = NewFileSuffixFilterFrame(
            self,
            kwargs["create_filter"],
            kwargs["update_file_suffix_action"],
            kwargs["file_suffixes"]
        )

        file_name_filter = NewNameFilterFrame(
            self,
            kwargs["file_names"],
            kwargs["create_filter"]
        )

        inverse_filter_frame = NewInverseFilterFrame(
            self,
            kwargs["create_inverse_filter"],
            kwargs["update_file_suffix_action"]
        )

        self._frames = {
            FileSuffixFilter: file_suffix_filter,
            NameFilter: file_name_filter,
            InverseFilter: inverse_filter_frame
        }

        label = ttk.Label(self, text="Select Filter Type:")
        filter_names = [name for name in filter_view_model_factory.filter_names_to_types_mapping.keys()]
        filter_combo = ttk.Combobox(
            self,
            values=filter_names,
            textvariable=self.selected_filter_type,
            state='readonly'
        )
        filter_combo.bind("<<ComboboxSelected>>", self._show_selected_frame)
        self.selected_filter_type.set(filter_names[0])

        separator = ttk.Separator(self, orient=tk.HORIZONTAL)

        create_button = ttk.Button(self, text="Create", command=self.create_button_clicked)
        cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)

        label.grid(row=0, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        filter_combo.grid(row=0, column=1, columnspan=2, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.E)

        separator.grid(row=1, column=0, columnspan=3,
                       padx=shared.SEPARATOR_PADDING, pady=shared.SEPARATOR_PADDING, sticky=tk.EW)

        create_button.grid(row=3, column=1, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.E)
        cancel_button.grid(row=3, column=2, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.E)

        file_suffix_filter.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW,
                                padx=shared.INTERIOR_PADDING, pady=shared.INTERIOR_PADDING)
        file_name_filter.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW,
                              padx=shared.INTERIOR_PADDING, pady=shared.INTERIOR_PADDING)
        inverse_filter_frame.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW,
                                  padx=shared.INTERIOR_PADDING, pady=shared.INTERIOR_PADDING)

        self._show_selected_frame()
        self.focus()
        self.grab_set()
        self.bind("<Return>", self.create_button_clicked)
        self.bind("<KP_Enter>", self.create_button_clicked)
        self.bind("<Control-v>", self._paste)

    def _show_selected_frame(self, *_):
        selected_frame = self._selected_frame()
        selected_frame.tkraise()

    def create_button_clicked(self, *_):
        self._selected_frame().create_filter()
        self.destroy()

    def _selected_frame(self) -> CreateFilterFrame:
        selected_filter = self.selected_filter_type.get()
        filter_class = filter_view_model_factory.filter_names_to_types_mapping[selected_filter]
        return self._frames[filter_class]

    def _paste(self, _):
        selected_frame = self._selected_frame()
        selected_frame.paste()
