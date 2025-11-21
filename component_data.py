
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
