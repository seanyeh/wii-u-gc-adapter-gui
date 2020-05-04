#!/usr/bin/env python3

import subprocess
import tkinter
from tkinter import Button, Label

WII_MESSAGE = "Make sure the adapter is set to \"Wii\" mode"
PC_MESSAGE = "Make sure the adapter is set to \"PC\" mode"

class Gui(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("wii-u-gc-adapter gui")

        # Background process for wii-u-gc-adapter
        self.process = None

        # UI
        config = {
            "height": 20,
            "width": 20
        }

        self.wii_button = Button(self, text="GC / Wii / Dolphin", **config)
        self.wii_button.config(command=lambda: self.select_button(self.wii_button))
        self.wii_button.grid(row=0, column=0)

        self.pc_button = Button(self, text="PC (wii-u-gc-adapter)", **config)
        self.pc_button.config(command=lambda: self.select_button(self.pc_button))
        self.pc_button.grid(row=0, column=1)

        self.label = Label(self, text=WII_MESSAGE)
        self.label.grid(row=1, column=0, columnspan=2)

        # Default: set wii_button as selected
        self.selected_button = self.wii_button
        self.wii_button.config(relief=tkinter.SUNKEN)

    def select_button(self, button):
        if button == self.selected_button:
            return

        # Run/kill wii-u-gc-adapter and update label
        if button == self.pc_button:
            self.label.config(text=PC_MESSAGE)
            self.process = subprocess.Popen("wii-u-gc-adapter")
        else:
            self.label.config(text=WII_MESSAGE)
            if self.process:
                self.process.kill()

        # Update buttons
        self.selected_button.config(relief=tkinter.RAISED)
        button.config(relief=tkinter.SUNKEN)

        self.selected_button = button

app = Gui()
app.mainloop()
