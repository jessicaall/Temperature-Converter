# Temperature Convertor/Export Gui
from tkinter import *
from functools import partial  # To prevent unwanted windows

import random

class Converter:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold",),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # export Button (row 1)
        self.export_button = Button(self.converter_frame, text="Export",
                                  font=("Arial", "14"),
                                  highlightbackground="light blue",
                                  padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):

        background = "lavender"

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at the top, close export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                          font=("Arial", "18", "bold",),
                                          bg=background,
                                          padx=10, pady=10)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below "
                                         "and press the save button to save your "
                                         "calculation history to a text file.",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(column=0, row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you enter below "
                                 "already exists, "
                                 "its contents will "
                                 "be replaced with "
                                 "your calculation "
                                 "history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put help button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
