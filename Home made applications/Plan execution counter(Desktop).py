import tkinter as tk
from tkinter import ttk
from datetime import date
from PIL import Image, ImageDraw, ImageFont
import ctypes

def calculate_date_difference():
    input_date = user_date.get()
    year, month, day = map(int, input_date.split('-'))
    input_date = date(year, month, day)
    current_date = date.today()
    day_difference = (current_date - input_date).days
    result_label.config(text=f"Day difference from last Daily Plan execution: {day_difference}")
    # Update the wallpaper
    update_wallpaper(f"Day difference from last Daily Plan execution: {day_difference}")
    # Close the application
    app.destroy()  

def update_date_input():
    if use_today.get():
        today = date.today()
        user_date.delete(0, tk.END)
        user_date.insert(0, today.isoformat())
    else:
        user_date.delete(0, tk.END)

def update_wallpaper(text):
    # Change this to the path of your current wallpaper image
    wallpaper_path = r"C:\Users\Sean\Pictures\wallpaper\origin.jpg"
    
    # Create a new image with the result text
    img = Image.open(wallpaper_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 50)  # Change the font and size as needed
    draw.text((170, 50), text, font=font, fill=(0, 0, 0))

    # Save the new image
    new_wallpaper_path = r"C:\Users\Sean\Pictures\wallpaper\display.jpg"
    img.save(new_wallpaper_path)

    # Set the new image as the wallpaper (Windows only)
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, new_wallpaper_path, 3)



# Create the main window
app = tk.Tk()
app.title("Date Difference Calculator")

# Create widgets
instruction_label = ttk.Label(app, text="Enter a date (YYYY-MM-DD):")
user_date = ttk.Entry(app)
calculate_button = ttk.Button(app, text="Calculate", command=calculate_date_difference)
result_label = ttk.Label(app, text="Day difference:")

# Checkbox
use_today = tk.BooleanVar()
checkbox = ttk.Checkbutton(app, text="Use today's date", variable=use_today, command=update_date_input)

# Position the widgets on the window
instruction_label.grid(row=0, column=0, padx=5, pady=5)
user_date.grid(row=0, column=1, padx=5, pady=5)
calculate_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
result_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
checkbox.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

# Run the application
app.mainloop()
