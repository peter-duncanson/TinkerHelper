import tkinter as tk
from tkinter import ttk

components_data = {
    "resistor": {
        "color_codes": {
            "black": {"digit": 0, "multiplier": 1, "temp_coeff": "250 ppm/K"},
            "brown": {"digit": 1, "multiplier": 10, "tolerance": "±1%", "temp_coeff": "100 ppm/K"},
            "red": {"digit": 2, "multiplier": 100, "tolerance": "±2%", "temp_coeff": "50 ppm/K"},
            "orange": {"digit": 3, "multiplier": 1000, "temp_coeff": "15 ppm/K"},
            "yellow": {"digit": 4, "multiplier": 10000, "temp_coeff": "25 ppm/K"},
            "green": {"digit": 5, "multiplier": 100000, "tolerance": "±0.5%"},
            "blue": {"digit": 6, "multiplier": 1000000, "tolerance": "±0.25%"},
            "violet": {"digit": 7, "multiplier": 10000000, "tolerance": "±0.1%"},
            "gray": {"digit": 8, "multiplier": 100000000, "tolerance": "±0.05%"},
            "white": {"digit": 9, "multiplier": 1000000000},
            "gold": {"digit": None, "multiplier": 0.1, "tolerance": "±5%"},
            "silver": {"digit": None, "multiplier": 0.01, "tolerance": "±10%"},
            "none": {"digit": None, "multiplier": None, "tolerance": "±20%"},
        },
    },
    "capacitor": {
        "code_guide": {
            "1st_digit": "First significant figure of the capacitance value.",
            "2nd_digit": "Second significant figure of the capacitance value.",
            "3rd_digit": "Multiplier (power of 10) in Picofarads (pF).",
            "units": "Capacitance is read in Picofarads (pF) before conversion.",
        },
        "tolerance_codes": {
            "B": "±0.1 pF", "C": "±0.25 pF", "D": "±0.5 pF", "F": "±1%",
            "G": "±2%", "H": "±3%", "J": "±5%", "K": "±10%", "M": "±20%",
            "Z": "+80%/-20%"
        }
    },
    "LED": {
        "forward_voltage_guide": {
            "red": "1.8V - 2.2V",
            "green": "2.0V - 3.5V",
            "blue": "3.0V - 3.7V",
            "white": "3.0V - 3.7V",
        }
    }
}


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