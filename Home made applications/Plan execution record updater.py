import tkinter as tk
from tkinter import ttk
import pandas as pd
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import ctypes


def update_date():
    if var.get():
        record = pd.read_csv('D:/github/Projects/Home made applications/daily_plan_execution_record.csv')
        
        current_date= datetime.now().strftime('%Y-%m-%d')
        
        if record.iloc[-1]['execution_date'] < current_date:

            last_execution_date = record.iloc[-1]['execution_date']
            last_execution_date
            df_date = pd.DataFrame({'execution_date' : [current_date] , 'last_execution_date' : [last_execution_date]})
            df_date['day_diff_last_execution_date'] = (pd.to_datetime(df_date['execution_date']) - pd.to_datetime(df_date['last_execution_date'])).dt.days - 1

            record_2 = pd.concat([record, df_date], axis= 0)
            
            record_2.to_csv('D:/github/Projects/Home made applications/daily_plan_execution_record.csv', index=False)
            var.set(False)
            
            # Update the wallpaper
            update_wallpaper(f"Day difference from last Daily Plan execution: {df_date.iloc[-1]['day_diff_last_execution_date']}")
            
            app.destroy()
        
        else:
            var.set(False)
            app.destroy()
                

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
app.title('Daily Plan Checker')

# Create widgets
instruction_label = ttk.Label(app, text="Click the checkbox for updating the execution date:")

var = tk.BooleanVar()

check_button = ttk.Checkbutton(app, text="Yes! I made it!", variable=var, command=update_date)
check_button.grid(column=0, row=0, padx=10, pady=10)

# Position the widgets on the window
instruction_label.grid(row=0, column=0, padx=5, pady=5)
check_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)


# Run the application
app.mainloop()