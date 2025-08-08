import tkinter as tk
import random

COLOR_NAMES = [
    "red", "green", "blue", "orange", "purple",
    "pink", "cyan", "magenta", "yellow", "lime","crimson", "gold", "mediumseagreen", "deepskyblue",
    "orchid", "orange", "turquoise", "tomato", "slateblue", "chartreuse" "Crimson", "DarkOrchid", "DeepSkyBlue", "Gold", "HotPink",
    "MediumSeaGreen", "OrangeRed", "PaleTurquoise", "Tomato", "VioletRed",
    "SlateBlue", "SpringGreen", "SteelBlue", "Maroon", "OliveDrab",
    "Coral", "MediumPurple", "LimeGreen", "Sienna", "Turquoise"
]

def create_palette():
    for widget in frame.winfo_children():
        widget.destroy()
    for _ in range(5):
        color = random.choice(COLOR_NAMES)
        label = tk.Label(frame, bg=color, width=20, height=10)
        label.pack(side=tk.LEFT, padx=5, pady=5)
        label.bind("<Button-1>", lambda e, c=color: show_color_code(c))

def show_color_code(color):
    code_label.config(text=f"Color Name: {color}")

root = tk.Tk()
root.title("Color Palette Generator with Names")
frame = tk.Frame(root)
frame.pack(pady=10)

generate_button = tk.Button(root, text="Generate Palette", command=create_palette)
generate_button.pack(pady=5)

code_label = tk.Label(root, text="Click a color to see its name")
code_label.pack(pady=5)

root.mainloop()
