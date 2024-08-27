import tkinter as tk

from svg_concat.ui.ui_vars import DEFAULT_PADDING, DEFAULT_PADDING_WITH_BUTTON


class CriteriaSelectionFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.selected_criteria = tk.StringVar()

        self.search_criteria_label = tk.Label(self, text="Search criteria:")
        self.search_criteria_label.grid(row=1, column=0, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING_WITH_BUTTON,
                                        sticky=tk.NW)

        self.search_criteria_list_box = tk.Listbox(self, listvariable=self.selected_criteria, selectmode=tk.MULTIPLE)
        self.search_criteria_list_box.grid(row=1, column=1, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, columnspan=2,
                                           sticky=tk.NW, rowspan=2)

        self.search_criteria_add_button = tk.Button(self, text="Add Criteria", command=self.add_criteria)
        self.search_criteria_add_button.grid(row=1, column=3, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, sticky=tk.NW)

        self.search_criteria_remove_button = tk.Button(self, text="Remove Criteria", command=self.remove_criteria)
        self.search_criteria_remove_button.grid(row=2, column=3, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING,
                                                sticky=tk.NW)

    def add_criteria(self):
        pass

    def remove_criteria(self):
        pass
