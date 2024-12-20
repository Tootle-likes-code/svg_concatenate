from tkinter import ttk
from abc import ABC, abstractmethod


class CreateFilterFrame(ttk.Frame, ABC):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

    @abstractmethod
    def create_filter(self):
        pass

    @abstractmethod
    def paste(self):
        pass
