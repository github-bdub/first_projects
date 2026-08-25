import tkinter as tk
from tkinter import ttk, messagebox
import math

# ---------- Logic ----------

def calculate():
    try:
        radius = float(radius_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for the radius.")
        return

    if radius < 0:
        messagebox.showerror("Invalid input", "Radius cannot be negative.")
        return

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    result_text = (
        f"Radius:         {radius:.2f}\n"
        f"Area:           {area:.2f}\n"
        f"Circumference:  {circumference:.2f}"
    )
    result_label.config(text=result_text)


# ---------- Window setup ----------

root = tk.Tk()
root.title("Circle Calculator")
root.geometry("360x320")
root.resizable(False, False)
root.configure(bg="#f5f6fa")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 11, "bold"), padding=8)
style.configure("TLabel", background="#f5f6fa")

# ---------- Layout ----------

title_label = tk.Label(
    root,
    text="Circle Calculator",
    font=("Helvetica", 18, "bold"),
    bg="#f5f6fa",
    fg="#2c3e50",
)
title_label.pack(pady=(20, 10))

input_frame = tk.Frame(root, bg="#f5f6fa")
input_frame.pack(pady=5)

radius_label = tk.Label(
    input_frame, text="Radius:", font=("Helvetica", 12), bg="#f5f6fa"
)
radius_label.grid(row=0, column=0, padx=(0, 8))

radius_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=12, justify="center")
radius_entry.grid(row=0, column=1)
radius_entry.focus()

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=15)

result_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
result_frame.pack(padx=30, pady=10, fill="both", expand=True)

result_label = tk.Label(
    result_frame,
    text="Radius:\nArea:\nCircumference:",
    font=("Courier New", 12),
    bg="#ffffff",
    fg="#2c3e50",
    justify="left",
    anchor="nw",
    padx=15,
    pady=15,
)
result_label.pack(fill="both", expand=True)

# Allow pressing Enter in the entry box to trigger calculation
radius_entry.bind("<Return>", lambda event: calculate())

root.mainloop()
