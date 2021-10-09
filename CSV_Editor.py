import tkinter as tk
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv

# Python learning
# Funktion - open a file for editing/reading
def open_file():

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title("Super Text-Editor 1.0 -- " + filepath)


# Funktion - save the current file as a new file.
def save_file():

    filepath = asksaveasfilename(
        defaultextension="csv",
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        s = csv.writer(output_file)
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title("Super Text-Editor 1.0 -- " + filepath)


# Funktion - close the Editor
def close_window():
    window.destroy()


# Funktion - show the graphic
def open_graphic():

    xs = []
    ys = []

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "r") as input_file:

        for line in input_file:

            data = line.strip().split(";")
            
            xs.append(int(data[0]))
            ys.append(float(data[1]))
        
        plt.plot(xs, ys)
        plt.show()

    window.title("Super Text-Editor 1.0 -- " + filepath)    



window = tk.Tk()
window.title("Super Text-Editor 1.0")
window.config(background = "cyan")


window.rowconfigure(0, minsize = 500, weight = 1)
window.columnconfigure(1, minsize = 500, weight = 1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window,  bg = "cyan")

# Buttons 
button_open = tk.Button(fr_buttons, text = "Open", command = open_file)
button_save = tk.Button(fr_buttons, text = "Save", command = save_file)
button_delete_1 = tk.Button(fr_buttons, text = "Close", command = close_window)
button_delete_2 = tk.Button(fr_buttons, text = "Graphic", command = open_graphic)
button_delete_3 = tk.Button(fr_buttons, text = "Button 2")

# Grid
button_open.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
button_save.grid(row = 1, column = 0, sticky = "ew", padx = 5, pady = 5)
button_delete_1.grid(row = 2, column = 0, sticky = "ew", padx = 5, pady = 5)
button_delete_2.grid(row = 3, column = 0, sticky = "ew", padx = 5, pady = 5)
button_delete_3.grid(row = 4, column = 0, sticky = "ew", padx = 5, pady = 5)

fr_buttons.grid(row = 0, column = 0, sticky = "ns", padx = 15, pady = 15)
txt_edit.grid(row = 0, column = 1, sticky = "nsew", padx = 15, pady = 15)

window.mainloop()