import tkinter as tk
from tkinter import ttk

from svg_concat.ui import shared


class ReportSectionFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.status = tk.StringVar()
        self.status.set("Not Run")

        label = ttk.Label(self, text="Report")
        state_label = ttk.Label(self, text="Run State:")
        status_label = ttk.Label(self, textvariable=self.status)
        self.text_area = tk.Text(self, wrap=tk.WORD)
        y_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.text_area.yview)
        self.text_area['yscrollcommand'] = y_scrollbar.set

        label.grid(row=0, column=0, sticky=tk.NW, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        state_label.grid(row=1, column=0, sticky=tk.EW, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        status_label.grid(row=1, column=1, sticky=tk.EW, padx=shared.X_PADDING, pady=shared.Y_PADDING)
        self.text_area.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, padx=shared.X_PADDING, pady=shared.Y_PADDING)

    def update_report(self, is_success, is_fatal, message: str | list[str]):
        if is_success:
            self.status.set("Success")
        elif is_fatal:
            self.status.set("Fatal Error")
        else:
            self.status.set("Failed")

        if isinstance(message, str):
            self.text_area.insert(tk.END, message)
            return

        self.text_area.insert(tk.END, "\n".join(message))
