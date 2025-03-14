# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 10:22:22 2025

@author: maxime
"""

import tkinter as tk
from tkinter import ttk
import math
import webbrowser

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
       
        self.frame = ttk.Frame(root, padding="20")
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
       
        self.create_category_menu()
        self.create_conversion_section()
   
    def create_category_menu(self):
        ttk.Label(self.frame, text="Select Category 1:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self.frame, text="Select Category 2:").grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
       
        self.category_options = ["Temperature", "Pressure", "Length", "Mass", "Volume"]
        self.selected_category1 = tk.StringVar(value=self.category_options[0])
        self.selected_category2 = tk.StringVar(value=self.category_options[0])
       
        self.category_menu1 = ttk.Combobox(self.frame, textvariable=self.selected_category1, values=self.category_options, state="readonly")
        self.category_menu2 = ttk.Combobox(self.frame, textvariable=self.selected_category2, values=self.category_options, state="readonly")
       
        self.category_menu1.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.category_menu2.grid(row=0, column=4, padx=5, pady=5, sticky=(tk.W, tk.E))
       
        self.category_menu1.bind("<<ComboboxSelected>>", self.update_conversion_options)
        self.category_menu2.bind("<<ComboboxSelected>>", self.update_conversion_options)
       
        self.conversion_options = {
            "Temperature": ["PT100: Celsius to Ohm", "PT100: Ohm to Celsius", "Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"],
            "Pressure": ["Pascal to Bar", "Bar to Pascal", "Pascal to PSI", "PSI to Pascal",
                         "Pascal to dB_SPL", "dB_SPL to Pascal"],
            "Length": ["Meters to Feet", "Feet to Meters", "Inches to Centimeters", "Centimeters to Inches", "Kilometers to Miles", "Miles to Kilometers"],
            "Mass": ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams"],
            "Volume": ["Liters to Gallons", "Gallons to Liters", "Milliliters to Fluid Ounces", "Fluid Ounces to Milliliters"]
        }
       
        self.selected_conversion1 = tk.StringVar(value=self.conversion_options[self.selected_category1.get()][0])
        self.selected_conversion2 = tk.StringVar(value=self.conversion_options[self.selected_category2.get()][0])
       
        self.dropdown_menu1 = ttk.Combobox(self.frame, textvariable=self.selected_conversion1, values=self.conversion_options[self.selected_category1.get()], state="readonly")
        self.dropdown_menu2 = ttk.Combobox(self.frame, textvariable=self.selected_conversion2, values=self.conversion_options[self.selected_category2.get()], state="readonly")
       
        self.dropdown_menu1.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.dropdown_menu2.grid(row=1, column=4, padx=5, pady=5, sticky=(tk.W, tk.E))
   
    def update_conversion_options(self, event):
        category1 = self.selected_category1.get()
        category2 = self.selected_category2.get()
       
        self.dropdown_menu1.config(values=self.conversion_options[category1])
        self.dropdown_menu2.config(values=self.conversion_options[category2])
       
        self.selected_conversion1.set(self.conversion_options[category1][0])
        self.selected_conversion2.set(self.conversion_options[category2][0])
   
    def show_help(self, conversion_type): # for Help buttons
        help_text = ""
        reference_url = None  # Default is None
    
        if conversion_type == "PT100: Celsius to Ohm":
            help_text = (
                "PT100 sensors follow the IEC 60751 standard.\n"
                "Formula: R = R0 * (1 + A*T + B*T²) \n"
                "For T < 0°C, an extra term C*(T-100)*T³ is used.\n"
            )
            reference_url = "https://webstore.iec.ch/publication/63753"
    
        elif conversion_type == "PT100: Ohm to Celsius":
            help_text = (
                "The PT100 resistance is converted to temperature using a polynomial approximation.\n"
                "T = a0 + a1*R + a2*R² + a3*R³ + a4*R⁴\n"
                "Different coefficients apply for R < 100 Ω and R ≥ 100 Ω.\n"
            )
            reference_url = "https://webstore.iec.ch/publication/63753"
    
        elif conversion_type == "Celsius to Fahrenheit":
            help_text = "Formula: F = (C × 9/5) + 32"
    
        elif conversion_type == "Fahrenheit to Celsius":
            help_text = "Formula: C = (F - 32) × 5/9"
    
        elif conversion_type == "Celsius to Kelvin":
            help_text = "Formula: K = C + 273.15"
    
        elif conversion_type == "Kelvin to Celsius":
            help_text = "Formula: C = K - 273.15"
    
        elif conversion_type == "Pascal to Bar":
            help_text = "Formula: Bar = Pascal / 100000"
    
        elif conversion_type == "Bar to Pascal":
            help_text = "Formula: Pascal = Bar × 100000"
    
        elif conversion_type == "Pascal to PSI":
            help_text = "Formula: PSI = Pascal / 6894.757"
    
        elif conversion_type == "PSI to Pascal":
            help_text = "Formula: Pascal = PSI × 6894.757"
    
        elif conversion_type == "Pascal to dB_SPL":
            help_text = "Formula: dB SPL = 20 × log10(P / 20µPa)"
    
        elif conversion_type == "dB_SPL to Pascal":
            help_text = "Formula: P = 10^(dB SPL / 20) × 20µPa"
    
        else:
            help_text = "No additional information available for this conversion."
    
        # Create the Help popup window
        help_window = tk.Toplevel(self.root) 
        """
        In Tkinter, Toplevel creates a new window, whereas Frame is a container within the main window.
        Pop-up Help Window => Toplevel
        Organizing Widgets Inside a Window => Frame
        Simple Alerts (Info, Error, Warning) => messagebox
        Completely New App Window => Tk()
        """
        help_window.title(f"Help - {conversion_type}")
    
        # **Calculate optimal window size**
        base_height = 100  # Minimum height
        text_lines = help_text.count("\n") + 2  # Count lines in the text
        if reference_url:
            text_lines += 2  # Add space for the link
        dynamic_height = base_height + (text_lines * 15)  # Adjust based on text length
    
        help_window.geometry(f"400x{dynamic_height}")  # Adjusted height dynamically
        help_window.resizable(False, False)  # Fixed size
    
        # Ensure proper column width handling
        help_window.columnconfigure(0, weight=1)
    
        # Create and pack the help label (Reduces spacing)
        help_label = tk.Label(help_window, text=help_text, wraplength=380, justify="left", padx=5, pady=5)
        help_label.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 2))  # Keeps text closer to link
    
        # If a reference URL exists, add a clickable link with minimal spacing
        if reference_url:
            def open_link(url=reference_url):
                webbrowser.open(url)
    
            link_label = tk.Label(help_window, text=f"Reference: {reference_url}", fg="blue", cursor="hand2")
            link_label.grid(row=1, column=0, sticky="w", padx=10, pady=2)  # Reduced spacing
            link_label.bind("<Button-1>", lambda e: open_link())
    
        # Close button (Positioned correctly without extra space)
        close_button = ttk.Button(help_window, text="Close", command=help_window.destroy)
        close_button.grid(row=2, column=0, pady=(40,0))
        
    def create_conversion_section(self):
            
        ttk.Label(self.frame, text="Select Conversion Type 1:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self.frame, text="Select Conversion Type 2:").grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
       
        ttk.Label(self.frame, text="Enter value 1:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self.frame, text="Enter value 2:").grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        
        self.explanation_label1 = ttk.Label(self.frame, text="", wraplength=400, style="Gray.TLabel")
        self.explanation_label1.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.explanation_label2 = ttk.Label(self.frame, text="", wraplength=400, style="Gray.TLabel")
        self.explanation_label2.grid(row=4, column=3, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
       
        self.value_entry1 = ttk.Entry(self.frame, width=15)
        self.value_entry2 = ttk.Entry(self.frame, width=15)
       
        self.value_entry1.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.value_entry2.grid(row=2, column=4, padx=5, pady=5, sticky=(tk.W, tk.E))
       
        self.result_label1 = ttk.Label(self.frame, text="Result 1:", style="Result.TLabel")
        self.result_label2 = ttk.Label(self.frame, text="Result 2:", style="Result.TLabel")
       
        self.result_label1.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.result_label2.grid(row=3, column=3, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Add Help Buttons for both conversions
        self.help_button1 = ttk.Button(self.frame, text="?", width=3, command=lambda: self.show_help(self.selected_conversion1.get()))
        self.help_button1.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        
        self.help_button2 = ttk.Button(self.frame, text="?", width=3, command=lambda: self.show_help(self.selected_conversion2.get()))
        self.help_button2.grid(row=1, column=5, padx=5, pady=5, sticky=tk.W)
       
        # Convert button
        convert_button = ttk.Button(self.frame, text="Convert", command=self.convert)
        convert_button.grid(row=4, column=2, columnspan=1, padx=5, pady=(20, 0), sticky=tk.N)
   
        # Define styles
        style = ttk.Style()
        style.configure("Result.TLabel", foreground="black")
        style.configure("Blue.TLabel", foreground="blue")
        style.configure("Gray.TLabel", foreground="gray")
        style.configure("Red.TLabel", foreground="red")
   
    def convert(self):
   
        def perform_conversion(value, conversion_type, result_label, explanation_label):
            try:
                value = float(value)
                explanation_text = ""
                
                if conversion_type == "PT100: Celsius to Ohm":
                    result = self.celsius_to_ohms(value)
                    explanation_text = (
                    "Formula: R = R0 * (1 + A*T + B*T²) \n"
                    "For T < 0°C, an extra term C*(T-100)*T³ is used."
                    )
                    result_label.config(text=f"Result: {value} °C => {result:.3f} ohm", style="Blue.TLabel")
                    
                elif conversion_type == "PT100: Ohm to Celsius":
                    result = self.ohms_to_celsius(value)
                    explanation_text = (
                    "Polynomial Approximation:\n"
                    "T = a0 + a1*R + a2*R² + a3*R³ + a4*R⁴\n"
                    "Different coefficients are used for R < 100 Ω and R ≥ 100 Ω."
                    )
                    result_label.config(text=f"Result: {value} ohm => {result:.3f} °C", style="Blue.TLabel")
                    
                elif conversion_type == "Celsius to Fahrenheit":
                    result = self.celsius_to_fahr(value)
                    explanation_text = "Formula: F = (C × 9/5) + 32"
                    result_label.config(text=f"Result: {value} °C => {result:.3f} Fahrenheit", style="Blue.TLabel")
                    
                elif conversion_type == "Fahrenheit to Celsius":
                    result = self.fahr_to_celsius(value)
                    explanation_text = "Formula: C = (F - 32) × 5/9"
                    result_label.config(text=f"Result: {value} Fahrenheit => {result:.3f} °C", style="Blue.TLabel")
                    
                elif conversion_type == "Celsius to Kelvin":
                    result = self.celsius_to_kelvin(value)
                    explanation_text = "Formula: K = C + 273.15"
                    result_label.config(text=f"Result: {value} °C => {result:.3f} Kelvin", style="Blue.TLabel")
                    
                elif conversion_type == "Kelvin to Celsius":
                    result = self.kelvin_to_celsius(value)
                    explanation_text = "Formula: C = K - 273.15"
                    result_label.config(text=f"Result: {value} Kelvin => {result:.3f} °C", style="Blue.TLabel")
                    
                elif conversion_type == "Pascal to Bar":
                    result = self.pascal_to_bar(value)
                    explanation_text = "Formula: Bar = Pascal / 100000"
                    result_label.config(text=f"Result: {value} Pascal => {result:.6f} Bar", style="Blue.TLabel")
                    
                elif conversion_type == "Bar to Pascal":
                    result = self.bar_to_pascal(value)
                    explanation_text = "Formula: Pascal = Bar × 100000"
                    result_label.config(text=f"Result: {value} Bar => {result:.3f} Pascal", style="Blue.TLabel")
                    
                elif conversion_type == "Pascal to PSI":
                    result = self.pascal_to_psi(value)
                    explanation_text = "Formula: PSI = Pascal / 6894.757"
                    result_label.config(text=f"Result: {value} Pascal => {result:.6f} PSI", style="Blue.TLabel")
                    
                elif conversion_type == "PSI to Pascal":
                    result = self.psi_to_pascal(value)
                    explanation_text = "Formula: Pascal = PSI × 6894.757"
                    result_label.config(text=f"Result: {value} PSI => {result:.3f} Pascal", style="Blue.TLabel")
                    
                elif conversion_type == "Pascal to dB_SPL":
                    result = self.pascal_to_dB_SPL(value)
                    explanation_text = "Formula: dB SPL = 20 × log10(P / 20µPa)"
                    result_label.config(text=f"Result: {value} Pascal => {result:.3f} dB SPL", style="Blue.TLabel")
                    
                elif conversion_type == "dB_SPL to Pascal":
                    result = self.dB_SPL_to_pascal(value)
                    explanation_text = "Formula: P = 10^(dB SPL / 20) × 20µPa"
                    result_label.config(text=f"Result: {value} dB SPL => {result:.3f} Pascal", style="Blue.TLabel")
                
                elif conversion_type == "Meters to Feet":
                    result = self.meters_to_feet(value)
                    explanation_text = "Formula: ft = m × 3.28084"
                    result_label.config(text=f"Result: {value} m => {result:.3f} ft", style="Blue.TLabel")
                    
                elif conversion_type == "Feet to Meters":
                    result = self.feet_to_meters(value)
                    explanation_text = "Formula: m = ft / 3.28084"
                    result_label.config(text=f"Result: {value} ft => {result:.3f} m", style="Blue.TLabel")
                    
                elif conversion_type == "Inches to Centimeters":
                    result = self.inches_to_centimeters(value)
                    explanation_text = "Formula: cm = in × 2.54"
                    result_label.config(text=f"Result: {value} in => {result:.3f} cm", style="Blue.TLabel")
                    
                elif conversion_type == "Centimeters to Inches":
                    result = self.centimeters_to_inches(value)
                    explanation_text = "Formula: in = cm / 2.54"
                    result_label.config(text=f"Result: {value} cm => {result:.3f} in", style="Blue.TLabel")
                    
                elif conversion_type == "Kilometers to Miles":
                    result = self.kilometers_to_miles(value)
                    explanation_text = "Formula: mi = km × 0.621371"
                    result_label.config(text=f"Result: {value} km => {result:.3f} mi", style="Blue.TLabel")
                    
                elif conversion_type == "Miles to Kilometers":
                    result = self.miles_to_kilometers(value)
                    explanation_text = "Formula: km = mi / 0.621371"
                    result_label.config(text=f"Result: {value} mi => {result:.3f} km", style="Blue.TLabel")
                    
                elif conversion_type == "Kilograms to Pounds":
                    result = self.kilograms_to_pounds(value)
                    explanation_text = "Formula: lb = kg × 2.20462"
                    result_label.config(text=f"Result: {value} kg => {result:.3f} lb", style="Blue.TLabel")
                    
                elif conversion_type == "Pounds to Kilograms":
                    result = self.pounds_to_kilograms(value)
                    explanation_text = "Formula: kg = lb / 2.20462"
                    result_label.config(text=f"Result: {value} lb => {result:.3f} kg", style="Blue.TLabel")
                    
                elif conversion_type == "Grams to Ounces":
                    result = self.grams_to_ounces(value)
                    explanation_text = "Formula: oz = g / 28.3495"
                    result_label.config(text=f"Result: {value} g => {result:.3f} oz", style="Blue.TLabel")
                    
                elif conversion_type == "Ounces to Grams":
                    result = self.ounces_to_grams(value)
                    explanation_text = "Formula: g = oz × 28.3495"
                    result_label.config(text=f"Result: {value} oz => {result:.3f} g", style="Blue.TLabel")
                    
                elif conversion_type == "Liters to Gallons":
                    result = self.liters_to_gallons(value)
                    explanation_text = "Formula: gal = L / 3.78541"
                    result_label.config(text=f"Result: {value} L => {result:.3f} gal", style="Blue.TLabel")
                    
                elif conversion_type == "Gallons to Liters":
                    result = self.gallons_to_liters(value)
                    explanation_text = "Formula: L = gal × 3.78541"
                    result_label.config(text=f"Result: {value} gal => {result:.3f} L", style="Blue.TLabel")
                    
                elif conversion_type == "Milliliters to Fluid Ounces":
                    result = self.milliliters_to_fluid_ounces(value)
                    explanation_text = "Formula: fl oz = mL / 29.5735"
                    result_label.config(text=f"Result: {value} mL => {result:.3f} fl oz", style="Blue.TLabel")
                    
                elif conversion_type == "Fluid Ounces to Milliliters":
                    result = self.fluid_ounces_to_milliliters(value)
                    explanation_text = "Formula: mL = fl oz × 29.5735"
                    result_label.config(text=f"Result: {value} fl oz => {result:.3f} mL", style="Blue.TLabel")
                    
                explanation_label.config(text=explanation_text, style="Gray.TLabel")
                    
            except ValueError:
                result_label.config(text="Invalid input. Please enter a numeric value.", style="Red.TLabel")
                explanation_label.config(text="")
                
        value1 = self.value_entry1.get()
        value2 = self.value_entry2.get()
        conversion_type1 = self.selected_conversion1.get()
        conversion_type2 = self.selected_conversion2.get()
   
        if value1:
            perform_conversion(value1, conversion_type1, self.result_label1, self.explanation_label1)
        else:
            self.result_label1.config(text="Input 1 is blank. Please enter a value.", style="Gray.TLabel")
            self.explanation_label1.config(text="")
   
        if value2:
            perform_conversion(value2, conversion_type2, self.result_label2, self.explanation_label2)
        else:
            self.result_label2.config(text="Input 2 is blank. Please enter a value.", style="Gray.TLabel")
            self.explanation_label2.config(text="")
       
   
    @staticmethod
    def celsius_to_fahr(c):
        return c * (9/5) + 32
   
    @staticmethod
    def fahr_to_celsius(f):
        return (f - 32) * (5/9)
   
    @staticmethod
    def celsius_to_ohms(t):
        R0 = 100
        A = 3.90802 * 10**-3
        B = -5.802 * 10**-7
        C = -4.2735 * 10**-12
       
        if t < 0:
            return R0 * (1 + A * t + B * t**2 + C * (t - 100) * t**3)
        else:
            return R0 * (1 + A * t + B * t**2)
   
    @staticmethod
    def ohms_to_celsius(Ω):
        Low0 = -305.8070
        Low1 = 5.066819
        Low2 = -0.04478043
        Low3 = 0.0003431833
        Low4 = -9.625786 * 10**-7
        High0 = -247.9258
        High1 = 2.422223
        High2 = 0.0003046477
        High3 = 3.134762 * 10**-6
        High4 = -4.726854 * 10**-9
       
        if Ω < 100:
            return Low0 + Low1 * Ω + Low2 * Ω**2 + Low3 * Ω**3 + Low4 * Ω**4
        else:
            return High0 + High1 * Ω + High2 * Ω**2 + High3 * Ω**3 + High4 * Ω**4
   
    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15
   
    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15
   
    @staticmethod
    def pascal_to_bar(p):
        return p / 100000
   
    @staticmethod
    def bar_to_pascal(b):
        return b * 100000
   
    @staticmethod
    def pascal_to_psi(p):
        return p / 6894.757
   
    @staticmethod
    def psi_to_pascal(psi):
        return psi * 6894.757
   
    @staticmethod
    def pascal_to_dB_SPL(p):
        return 20 * math.log10(p / 2e-5)
   
    @staticmethod
    def dB_SPL_to_pascal(dB):
        return 10**(dB / 20) * 2e-5
    
    @staticmethod
    def meters_to_feet(m):
        return m * 3.28084
    
    @staticmethod
    def feet_to_meters(f):
        return f / 3.28084
    
    @staticmethod
    def inches_to_centimeters(inch):
        return inch * 2.54
    
    @staticmethod
    def centimeters_to_inches(cm):
        return cm / 2.54
    
    @staticmethod
    def kilometers_to_miles(x):
        return x * 0.621371
    
    @staticmethod
    def miles_to_kilometers(x):
        return x / 0.621371
    
    @staticmethod
    def kilograms_to_pounds(x):
        return x * 2.20462
    
    @staticmethod
    def pounds_to_kilograms(x):
        return x / 2.20462
    
    @staticmethod
    def grams_to_ounces(x):
        return x / 28.3495
    
    @staticmethod
    def ounces_to_grams(x):
        return x * 28.3495
    
    @staticmethod
    def liters_to_gallons(x):
        return x / 3.78541
    
    @staticmethod
    def gallons_to_liters(x):
        return x * 3.78541
    
    @staticmethod
    def milliliters_to_fluid_ounces(x):
        return x / 29.5735
    
    @staticmethod
    def fluid_ounces_to_milliliters(x):
        return x * 29.5735
    
    
   
# Run the application
root = tk.Tk()
app = UnitConverterApp(root)
root.mainloop()