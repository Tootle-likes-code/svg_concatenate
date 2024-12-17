import tkinter as tk

from svg_concat.ui.directory_select_frame import DirectorySelectFrame
from svg_concat.ui.filter_frame import FilterFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('SVG Concatenate')

        self.directory_to_search_frame = DirectorySelectFrame(self, "Directory to Search")
        self.filter_frame = FilterFrame(self)

        self.directory_to_search_frame.pack(side=tk.TOP, fill=tk.X)
        self.filter_frame.pack(side=tk.TOP, fill=tk.X, anchor="e")

    def update_filters(self, filters):
        self.filter_frame.update_filters(filters)

    def add_filter_button(self, action_callback):
        self.filter_frame.add_filter_button(action_callback)
