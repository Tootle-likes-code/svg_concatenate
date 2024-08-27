import tkinter as tk

from svg_concat.ui.criteria_selction_frame import CriteriaSelectionFrame
from svg_concat.ui.input_folder_frame import InputFolderFrame


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        top = self.winfo_toplevel()
        top.columnconfigure(0, weight=1, minsize=400)
        top.rowconfigure(0, weight=1, minsize=400)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid(sticky=tk.NW)

        self._createWidgets()

    def _createWidgets(self):
        self.input_folder_frame = InputFolderFrame(self)
        self.input_folder_frame.grid(row=0, column=0, sticky=tk.E+tk.W)

        self.criteria_selection_frame = CriteriaSelectionFrame(self)
        self.criteria_selection_frame.grid(row=1, column=0, sticky=tk.E+tk.W)

