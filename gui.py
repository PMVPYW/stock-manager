import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create the label and listbox in the first column
stock_label = tk.Label(root, text="Stock")
stock_label.grid(row=0, column=0, sticky="w")

stock_listbox = tk.Listbox(root)
stock_listbox.grid(row=1, column=0, sticky="nsew")
scrollbar = tk.Scrollbar(root, command=stock_listbox.yview)
scrollbar.grid(row=1, column=0, sticky="nse")

stock_listbox.config(yscrollcommand=scrollbar.set)

# Create a container frame for the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=2, padx=10, pady=10)

# Create the buttons inside the container frame
button1 = tk.Button(button_frame, text="Button 1")
button2 = tk.Button(button_frame, text="Button 2")
button3 = tk.Button(button_frame, text="Button 3")
button4 = tk.Button(button_frame, text="Button 4")

# Add the buttons to the second column with 90% width
button1.grid(row=0, column=1, pady=10, sticky="ew", padx=5)
button2.grid(row=1, column=1, pady=10, sticky="ew", padx=5)
button3.grid(row=2, column=1, pady=10, sticky="ew", padx=5)
button4.grid(row=3, column=1, pady=10, sticky="ew", padx=5)

# Match the height of the container frame to the listbox
button_frame.configure(height=stock_listbox.winfo_height())

# Make the first column expand vertically to fill the space
root.rowconfigure(1, weight=1)

for x in range(100):
    stock_listbox.insert(tk.END, "This is line number " + str(x))

root.mainloop()
