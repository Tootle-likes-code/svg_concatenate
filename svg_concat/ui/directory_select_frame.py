import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from svg_concat.ui import shared


class DirectorySelectFrame(ttk.Frame):
    def __init__(self, master, label_text: str):
        super().__init__(master)

        self.selected_file_path = tk.StringVar()
        self.selected_file_path.set("")

        label = ttk.Label(self, text=f"{label_text}:")
        entry = ttk.Entry(self, textvariable=self.selected_file_path)
        open_button = ttk.Button(self, text="Select File", command=self._select_file, padding=5)

        label.grid(row=0, column=0, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.W)
        entry.grid(row=0, column=1, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.EW)
        open_button.grid(row=0, column=2, padx=shared.X_PADDING, pady=shared.Y_PADDING, sticky=tk.EW)

    def _select_file(self):
        filepath = tk.filedialog.askdirectory()

        if filepath:
            self.selected_file_path.set(filepath)
