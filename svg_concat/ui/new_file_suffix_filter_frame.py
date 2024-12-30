import tkinter as tk
from tkinter import ttk
from typing import Callable

from svg_concat.file_discovery.filter_types import FilterType
from svg_concat.ui import shared
from svg_concat.ui.create_filter_frame import CreateFilterFrame


class NewFileSuffixFilterFrame(CreateFilterFrame):
    def __init__(self, master, create_filter_action, update_file_suffix_action, existing_file_suffix=""):
        super().__init__(master)
        self.create_filter_action: Callable = create_filter_action
        self.update_file_suffix_action = update_file_suffix_action

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.name_text = tk.StringVar()
        self.name_text.set(existing_file_suffix)

        label = ttk.Label(self, text="File Suffix:")
        entry = ttk.Entry(self, textvariable=self.name_text)

        label.grid(row=0, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky="NEW")
        entry.grid(row=0, column=1, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky="NEW")

    def create_filter(self):
        self.create_filter_action(FilterType.FILE_SUFFIX_FILTER, self.name_text.get())

    def update_file_suffix_text(self):
        self.update_file_suffix_action(self.name_text.get())

    def paste(self):
        clipboard = self.clipboard_get().split("\n")
        clipboard = ", ".join(clipboard)

        existing_text = self.name_text.get()
        if existing_text and existing_text != "":
            new_text = existing_text + ", " + clipboard
        else:
            new_text = clipboard

        self.name_text.set(new_text)
