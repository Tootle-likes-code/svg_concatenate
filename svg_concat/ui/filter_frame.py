import tkinter as tk
from tkinter import ttk


class FilterFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self._add_window_open = False
        self.filter_names = tk.StringVar()

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        label = ttk.Label(self, text="Search Filters: ")
        self.list_box = tk.Listbox(self, listvariable=self.filter_names)
        self.button = ttk.Button(self, text="Add Search Filter", padding=(5, 5))

        label.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)
        self.list_box.grid(row=1, column=0, columnspan=3, rowspan=4, sticky=tk.EW, padx=10, pady=10)
        self.button.grid(row=1, column=3, padx=(0, 10), pady=10)

    def update_filters(self, filters):
        self.filter_names.set(filters)

    def add_filter_button(self, action_callback):
        self.button["command"] = action_callback
