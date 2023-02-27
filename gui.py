import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Create the label and listbox in the first column
        self.stock_label = tk.Label(self.root, text="self.stock")
        self.stock_label.grid(row=0, column=0, sticky="w")

        self.stock_listbox = tk.Listbox(self.root)
        self.stock_listbox.grid(row=1, column=0, sticky="nsew")
        self.scrollbar = tk.Scrollbar(self.root, command=self.stock_listbox.yview)
        self.scrollbar.grid(row=1, column=0, sticky="nse")

        self.stock_listbox.config(yscrollcommand=self.scrollbar.set)

        # Create a container frame for the self.buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=2, padx=10, pady=10)

        # Create the self.buttons inside the container frame
        self.button1 = tk.Button(self.button_frame, text="self.button 1")
        self.button2 = tk.Button(self.button_frame, text="self.button 2")
        self.button3 = tk.Button(self.button_frame, text="self.button 3")
        self.button4 = tk.Button(self.button_frame, text="self.button 4")

        # Add the self.buttons to the second column with 90% width
        self.button1.grid(row=0, column=1, pady=10, sticky="ew", padx=5)
        self.button2.grid(row=1, column=1, pady=10, sticky="ew", padx=5)
        self.button3.grid(row=2, column=1, pady=10, sticky="ew", padx=5)
        self.button4.grid(row=3, column=1, pady=10, sticky="ew", padx=5)

        # Match the height of the container frame to the listbox
        self.button_frame.configure(height=self.stock_listbox.winfo_height())

        # Make the first column expand vertically to fill the space
        self.root.rowconfigure(1, weight=1)
        self.names = []

        self.root.mainloop()

    def Add(self, name: str, quantity: int):
        self.stock_listbox.insert(tk.END, f"{name}\t{quantity}")
        self.names.append(name)
    
    def Remove(self, name: str):
        self.stock_listbox.delete(self.names.index(name))

    def edit(self, name: str, quantity: int):
        index = self.names.index(name)
        self.stock_listbox.delete(index)
        self.stock_listbox.insert(index, f"{name}\t{quantity}")
App()
