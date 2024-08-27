import tkinter as tk
from tkinter import filedialog

from svg_concat.ui.ui_vars import DEFAULT_PADDING, DEFAULT_PADDING_WITH_BUTTON


class InputFolderFrame(tk.Frame):
    def __init__(self, parent):
        super.__init__(parent)
        self.parent = parent
        self.selected_initial_folder = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.grid(sticky=tk.NW+tk.E)

        self._createWidgets()

    def _createWidgets(self):
        self.initial_folder_label = tk.Label(self, text="Initial Folder:")
        self.initial_folder_label.grid(row=0, column=0, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING_WITH_BUTTON,
                                       sticky=tk.NW)

        self.initial_folder_entry = tk.Entry(self, textvariable=self.selected_initial_folder)
        self.initial_folder_entry.grid(row=0, column=1, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING_WITH_BUTTON,
                                       columnspan=2, sticky=tk.NW)

        self.initial_folder_select_button = tk.Button(self, text="Select Folder",
                                                      command=self._select_initial_folder)
        self.initial_folder_select_button.grid(row=0, column=3, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING,
                                               sticky=tk.NW)


    def _select_initial_folder(self):
        self.selected_initial_folder.set(filedialog.askdirectory())