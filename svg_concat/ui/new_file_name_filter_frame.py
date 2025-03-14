import tkinter as tk
from tkinter import ttk
from typing import Callable

from svg_concat.file_discovery.filter_types import FilterType
from svg_concat.ui import shared
from svg_concat.ui.create_filter_frame import CreateFilterFrame


class NewNameFilterFrame(CreateFilterFrame):
    def __init__(self, parent, file_names, create_filter_action):
        super().__init__(parent)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.create_filter_action: Callable = create_filter_action

        self.new_file_name = tk.StringVar()

        label = (ttk.Label(self, text="Files to Find:"))
        self.files_listbox = tk.Listbox(self)
        self._generate_listbox(file_names)
        new_name_label = ttk.Label(self, text="New Name:")
        self.new_name_text_field = ttk.Entry(self, textvariable=self.new_file_name)
        add_button = ttk.Button(self, text="Add", command=self._add_button_clicked)
        remove_button = ttk.Button(self, text="Remove", command=self._remove_button_clicked)

        self.files_listbox.bind("<Delete>", self._remove_button_clicked)
        self.files_listbox.bind("<BackSpace>", self._remove_button_clicked)
        self.new_name_text_field.bind("<Control-v>", self._paste_into_text_field)
        self.new_name_text_field.bind("<Return>", self._new_name_text_field_enter_clicked)

        label.grid(row=0, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.NE)
        self.files_listbox.grid(row=1, column=0, columnspan=4, rowspan=5, padx=shared.X_PADDING,
                                pady=shared.Y_PADDING, sticky="NEW")
        new_name_label.grid(row=5, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky="NEW")
        self.new_name_text_field.grid(row=5, column=1, columnspan=3, padx=shared.X_PADDING,
                                      pady=shared.Y_PADDING, sticky="NEW")
        add_button.grid(row=6, column=2, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.NW)
        remove_button.grid(row=6, column=3, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.NW)

    def _generate_listbox(self, list):
        for item in list:
            self.files_listbox.insert(tk.END, item)

    def create_filter(self):
        files = self.files_listbox.get(0, tk.END)
        if isinstance(files, tuple):
            files = list(files)
        self.create_filter_action(FilterType.FILE_NAME_FILTER, files)

    def _add_button_clicked(self):
        self.files_listbox.insert(tk.END, self.new_file_name.get())
        self.new_file_name.set("")

    def _remove_button_clicked(self, _=None):
        for i in self.files_listbox.curselection():
            self.files_listbox.delete(i)

    def paste(self):
        clipboard = self.clipboard_get().split("\n")
        for item in clipboard:
            self.files_listbox.insert(tk.END, item)

    def _paste_into_text_field(self, _):
        clipboard = self.clipboard_get()
        self.new_file_name.set(clipboard)
        return "break"

    def _new_name_text_field_enter_clicked(self, _):
        self._add_button_clicked()
        return "break"
