import tkinter as tk
from tkinter import ttk

class tinker_helper(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.create_widgets()
        self.pack(fill="both", expand=True)
        
    def create_widgets(self):
        if self.master:
            self.master.title("tinker helper")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(padx=10, pady=10, fill="both", expand=True)

        # TAB 1 -> RESISTOR
        self.resistor_tab_frame = tk.Frame(self.notebook, padx=20, pady=20)
        self.create_resistor_tab(self.resistor_tab_frame)
        self.notebook.add(self.resistor_tab_frame, text="Resistors")

        # TAB 2 -> CAPACITOR
        self.capacitor_tab_frame = tk.Frame(self.notebook, padx=20, pady=20)
        self.create_capacitor_tab(self.capacitor_tab_frame)
        self.notebook.add(self.capacitor_tab_frame, text="Capacitors")

        # TAB 3 -> MISC NOTES
        self.misc_tab_frame = tk.Frame(self.notebook, padx=20, pady=20)
        self.create_misc_tab(self.misc_tab_frame)
        self.notebook.add(self.misc_tab_frame, text="Misc")

        # self.test_button = tk.Button(self, text="test")
        # self.test_button.pack()
        # self.entry_box = tk.Entry(self, textvariable=self.entry_str)
        # self.entry_box.pack()

    
    def create_resistor_tab(self, parent):
        """
        content of the resistor tab
        """
        tk.Label(parent, text="Resistors").pack()
        self.resistor_value_entry = tk.Entry(parent)


    def create_capacitor_tab(self, parent):
        """
        content of the capacitor tab
        """
        tk.Label(parent, text="Capacitors").pack()

    def create_misc_tab(self, parent):
        """
        content of the misc tab, LED and stuff
        """
        tk.Label(parent, text="MISC").pack()

if __name__ == "__main__":
    root = tk.Tk() 
    root.geometry("600x400")
    app = tinker_helper(master=root)
    app.mainloop()