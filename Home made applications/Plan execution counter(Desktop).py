import os
import ctypes
import tkinter as tk
from tkinter import ttk
from datetime import date
from PIL import Image, ImageDraw, ImageFont

def calculate_date_difference():
    input_date = user_date.get()
    year, month, day = map(int, input_date.split('-'))
    input_date = date(year, month, day)
    current_date = date.today()
    day_difference = (current_date - input_date).days
    update_wallpaper(f"Day difference of last Daily Plan execution: {day_difference}")

def update_wallpaper(text):
    # the path of original wallpaper image
    wallpaper_path = r"C:\Users\Sean\Pictures\wallpaper\origin.jpg"
    
    # Create a new image with the result text
    img = Image.open(wallpaper_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 60)  # Change the font and size as needed
    draw.text((150, 50), text, font=font, fill=(0, 0, 0))

    # Save the message to display
    new_wallpaper_path = r"C:\Users\Sean\Pictures\wallpaper\display.jpg"
    img.save(new_wallpaper_path)

    # Set the new image as the wallpaper (Windows only)
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, new_wallpaper_path, 3)

# Create the main window
app = tk.Tk()
app.title("Plan Executioni Difference Calculator")

# Create widgets
instruction_label = ttk.Label(app, text="Enter a date (YYYY-MM-DD):")
user_date = ttk.Entry(app)
calculate_button = ttk.Button(app, text="Calculate", command=calculate_date_difference)

# Position the widgets on the window
instruction_label.grid(row=0, column=0, padx=5, pady=5)
user_date.grid(row=0, column=1, padx=5, pady=5)
calculate_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

# Run the application
app.mainloop()
