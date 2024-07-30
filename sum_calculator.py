import tkinter as tk

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"The sum is: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Sum Calculator")

# Create and place the widgets
label1 = tk.Label(root, text="Enter the first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
