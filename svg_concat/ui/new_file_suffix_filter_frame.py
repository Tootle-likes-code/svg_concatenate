import tkinter as tk
from tkinter import ttk
from typing import Callable

from svg_concat.file_discovery.file_filters.filter_types import FilterType
from svg_concat.ui.create_filter_frame import CreateFilterFrame


class NewFileSuffixFilterFrame(CreateFilterFrame):
    def __init__(self, master, create_filter_action, update_file_suffix_action):
        super().__init__(master)
        self.create_filter_action: Callable = create_filter_action
        self.update_file_suffix_action = update_file_suffix_action

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.name_text = tk.StringVar()

        label = ttk.Label(self, text="File Suffix:")
        entry = ttk.Entry(self, textvariable=self.name_text)

        label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.EW)
        entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

    def create_filter(self):
        self.create_filter_action(FilterType.FILE_SUFFIX_FILTER, self.name_text.get())

    def update_file_suffix_text(self):
        self.update_file_suffix_action(self.name_text.get())
