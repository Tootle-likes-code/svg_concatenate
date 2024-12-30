import tkinter as tk
from tkinter import ttk

from svg_concat.ui import shared


class FilterFrame(tk.Frame):
    def __init__(self, master, add_filter_action):
        super().__init__(master)
        self._master = master
        self._add_window_open = False
        self.filter_names = tk.StringVar()

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        label = ttk.Label(self, text="Search Filters: ")
        self.list_box = tk.Listbox(self, listvariable=self.filter_names)
        self.button = ttk.Button(self, text="Add/Update\nSearch Filter", padding=(5, 5), command=add_filter_action)

        label.grid(row=0, column=0, sticky=tk.EW, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.list_box.grid(row=1, column=0, columnspan=3, rowspan=4, sticky=tk.EW,
                           padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.button.grid(row=1, column=3, padx=(0, shared.X_PADDING), pady=shared.Y_PADDING)

    def update_filters(self, filters):
        self.filter_names.set(filters)
