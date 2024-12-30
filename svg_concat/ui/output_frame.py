import tkinter as tk
import tkinter.ttk as ttk
from typing import Callable

from svg_concat.ui import shared
from svg_concat.ui.directory_select_frame import DirectorySelectFrame


class OutputFrame(ttk.Frame):
    def __init__(self, master, output_directory_listener: Callable[[str], None],
                 svg_output_listener: Callable[[str], None], report_output_listener: Callable[[str], None]):
        super().__init__(master)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.svg_output_listener = svg_output_listener
        self.report_output_listener = report_output_listener

        self.svg_output = tk.StringVar()
        self.svg_output.trace_add("write", self._svg_output_updated)
        self.report_output = tk.StringVar()
        self.report_output.trace_add("write", self._report_output_updated)

        self.directory_frame = DirectorySelectFrame(self, "Directory to Save", output_directory_listener)
        svg_output_label = ttk.Label(self, text="SVG File Name:")
        svg_output_entry = ttk.Entry(self, textvariable=self.svg_output)
        report_output_label = ttk.Label(self, text="Report File Name:")
        report_output_entry = ttk.Entry(self, textvariable=self.report_output)

        self.directory_frame.grid(row=0, column=0, columnspan=3, sticky="NEW")
        svg_output_label.grid(row=1, column=0, sticky=tk.NW,
                              padx=shared.X_PADDING, pady=shared.Y_PADDING)
        svg_output_entry.grid(row=1, column=1, sticky="NEW", columnspan=2,
                              padx=shared.X_PADDING, pady=shared.Y_PADDING)
        report_output_label.grid(row=2, column=0, sticky=tk.NW,
                            padx=shared.X_PADDING, pady=shared.Y_PADDING)
        report_output_entry.grid(row=2, column=1, sticky="NEW", columnspan=2,
                                 padx=shared.X_PADDING, pady=shared.Y_PADDING)

    def _svg_output_updated(self, *_):
        self.svg_output_listener(self.svg_output.get())

    def _report_output_updated(self, *_):
        self.report_output_listener(self.report_output.get())

    def update_ui(self, output_directory, svg_file, report_file):
        self.directory_frame.update_text(output_directory)
        self.svg_output.set(svg_file)
        self.report_output.set(report_file)
