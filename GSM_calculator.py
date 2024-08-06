import tkinter as tk

# GSM Calculator Function
def calculate_gsm():
    try:
        length_cm = float(entry_length.get())
        width_cm = float(entry_width.get())
        weight_g = float(entry_weight.get())
        gsm = (weight_g / ((length_cm * width_cm) / 10000))
        length_in = length_cm * 0.393701
        width_in = width_cm * 0.393701
        result_label.config(
            text=f"The GSM is: {gsm:.2f}\nLength (in): {length_in:.2f}\", Width (in): {width_in:.2f}\"",
            font=(None, 16, 'bold')
        )
    except ValueError:
        result_label.config(
            text="Please enter valid numbers",
            font=(None, 16, 'bold')
        )

# Function to bind Enter key to the Calculate GSM button
def on_enter_key(event):
    calculate_gsm()

# Create the main window
root = tk.Tk()
root.title("Grams Per Square Meter Calculator")

# Center the window on the screen
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Configure the grid to expand
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

# Labels and Entries for Length, Width, and Weight
label_title_fabric = tk.Label(root, text="Fabric Size", font=(None, 14, 'bold'))
label_title_fabric.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label_length = tk.Label(root, text="Length (cm):")
label_length.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
entry_length = tk.Entry(root, width=9)
entry_length.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

label_width = tk.Label(root, text="Width (cm):")
label_width.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
entry_width = tk.Entry(root, width=9)
entry_width.grid(row=1, column=3, padx=3, pady=3, sticky="ew")

label_title_weight = tk.Label(root, text="Weight", font=(None, 14, 'bold'))
label_title_weight.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

label_weight = tk.Label(root, text="Weight (g):")
label_weight.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
entry_weight = tk.Entry(root, width=9)
entry_weight.grid(row=4, column=1, padx=3, pady=3, sticky="ew")

# Button to Calculate GSM
calculate_button = tk.Button(root, text="Calculate GSM", command=calculate_gsm)
calculate_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Label to display the result
result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Bind the Enter key to the on_enter_key function
root.bind('<Return>', on_enter_key)

# Start the Tkinter event loop
root.mainloop()
