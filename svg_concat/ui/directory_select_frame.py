import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from typing import Callable

from svg_concat.ui import shared


class DirectorySelectFrame(ttk.Frame):
    def __init__(self, master, label_text: str, update_callback: Callable):
        super().__init__(master)
        self.update_callback: Callable = update_callback

        self.columnconfigure(1, weight=1)

        self.selected_file_path = tk.StringVar()
        self.selected_file_path.set("")
        self.selected_file_path.trace_add("write", self.path_updated)

        label = ttk.Label(self, text=f"{label_text}:")
        self.selected_file_path_entry = ttk.Entry(self, textvariable=self.selected_file_path)
        open_button = ttk.Button(self, text="Select File", command=self._select_file, padding=5)

        label.grid(row=0, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.W)
        self.selected_file_path_entry.grid(row=0, column=1, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.EW)
        open_button.grid(row=0, column=2, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.EW)

    def _select_file(self):
        filepath = tk.filedialog.askdirectory()

        if filepath:
            self.selected_file_path.set(filepath)

        self.selected_file_path_entry.icursor(tk.END)
        self.selected_file_path_entry.xview_moveto(1)

    def path_updated(self, *_):
        self.update_callback(self.selected_file_path.get())
