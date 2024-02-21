from tkinter import *

def convert_cm_to_feet():
    try:
        cm_value = float(cm_entry.get())
        feet_value = cm_value / 30.48
        feet_label.config(text=f"{feet_value:.2f} feet")
        print(f"{feet_value:.2f} feet", end=' ')
    except ValueError:
        feet_label.config(text="Invalid input. Please enter a number.")
def convert_feet_to_inches():
  try:
    feet_value = float(feet_entry.get())
    inches_value = feet_value * 12
    inches_label.config(text=f"{inches_value:.2f} inches")
  except ValueError:
    inches_label.config(text="Invalid input. Please enter a number.")

def convert_sqft_to_sqmtrs():
  try:
    sqft_value = float(sqft_entry1.get())
    sqmtrs_value = sqft_value * 0.0929
    sqmtrs_label.config(text=f"{sqmtrs_value:.2f} square meters")
  except ValueError:
    sqmtrs_label.config(text="Invalid input. Please enter a number.")

def convert_sqft_to_hectare_acre():
  try:
    sqft_value = float(sqft_entry2.get())
    hectare_value = sqft_value / 107639.104
    acre_value = sqft_value / 43560
    hectare_label.config(text=f"{hectare_value:.6f} hectares")
    acre_label.config(text=f"{acre_value:.6f} acres")
  except ValueError:
    hectare_label.config(text="Invalid input. Please enter a number.")

root = Tk()
root.title("Unit Converter")

# Centimeter to Feet
cm_label = Label(root, text="Centimeter:")
cm_label.grid(row=0, column=0)
cm_entry = Entry(root)
cm_entry.grid(row=0, column=1)
feet_label = Label(root, text="Feet:")
feet_label.grid(row=0, column=2)
cm_button = Button(root, text="Convert", command=convert_cm_to_feet)
cm_button.grid(row=0, column=3)

# Feet to Inches
feet_label = Label(root, text="Feet:")
feet_label.grid(row=1, column=0)
feet_entry = Entry(root)
feet_entry.grid(row=1, column=1)
inches_label = Label(root, text="Inches:")
inches_label.grid(row=1, column=2)
feet_button = Button(root, text="Convert", command=convert_feet_to_inches)
feet_button.grid(row=1, column=3)

# Sqft to Sqmtrs
sqft_label = Label(root, text="Square Feet:")
sqft_label.grid(row=2, column=0)
sqft_entry1 = Entry(root)
sqft_entry1.grid(row=2, column=1)
sqmtrs_label = Label(root, text="Square Meters:")
sqmtrs_label.grid(row=2, column=2)
sqft_button1 = Button(root, text="Convert", command=convert_sqft_to_sqmtrs)
sqft_button1.grid(row=2, column=3)

# Sqft to Hectre / Acre
sqft_label = Label(root, text="Square Feet:")
sqft_label.grid(row=3, column=0)
sqft_entry2 = Entry(root)
sqft_entry2.grid(row=3, column=1)
hectare_label = Label(root, text="Hectares:")
hectare_label.grid(row=3, column=2)
acre_label = Label(root, text="Acres:")
acre_label.grid(row=3, column=3)
sqft_button2 = Button(root, text="Convert", command=convert_sqft_to_hectare_acre)
sqft_button2.grid(row=3, column=4)

root.mainloop()
