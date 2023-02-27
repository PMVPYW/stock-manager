import tkinter as tk
import tkinter.messagebox as messagebox
from Manager import *

def validate_number_input(new_value):
    try:
        float(new_value)
        return True
    except ValueError:
        return False


class App:
    def __init__(self):
        self.manager = Manager()
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
        self.button1 = tk.Button(self.button_frame, text="Novo", command=self.new_menu)
        self.button2 = tk.Button(self.button_frame, text="Incrementar", command=self.inc_window)
        self.button3 = tk.Button(self.button_frame, text="Decrementar", command=self.dec_window)
        self.button4 = tk.Button(self.button_frame, text="Remover", command=self.rem)

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

    def new_menu(self):
        # Create a new top-level self.window
        self.window = tk.Toplevel()
        self.window.geometry('200x100')
        
        # Create the labels and text boxes in the two columns
        label1 = tk.Label(self.window, text='Nome')
        label1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry1 = tk.Entry(self.window)
        self.entry1.grid(row=0, column=1, padx=5, pady=5, sticky='we')
        
        label2 = tk.Label(self.window, text='Quantidade')
        label2.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry2 = tk.Entry(self.window)
        self.entry2.grid(row=1, column=1, padx=5, pady=5, sticky='we')
         # Add a button to close the self.window
        button = tk.Button(self.window, text='Adicionar', command=self.Add_Close)
        button.grid(row=2, column=0, columnspan=2, pady=5)
    
        # Set column 1 to expand horizontally
        self.window.columnconfigure(1, weight=1)

    def rem(self):
        try:
            index = int(str(self.stock_listbox.curselection()).replace(",", "").replace(")", "").replace("(", ""))
        except:
            messagebox.showwarning(title="Aviso", message="Selecione um elemento na janela principal")
            return
        name = self.names[index]
        to_remove = messagebox.askyesno(title="Remover Item", message=f"Tem a certeza que pretende remover o item {name}?")
        if not to_remove:
            return
        self.remove(name)

    def inc_window(self):
        self.window = tk.Toplevel()
        self.window.geometry('200x100')
                
        label2 = tk.Label(self.window, text='Quantidade')
        label2.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry2 = tk.Entry(self.window)
        self.entry2.grid(row=0, column=1, padx=5, pady=5, sticky='we')
         # Add a button to close the self.window
        button = tk.Button(self.window, text='Incrementar', command=self.inc)
        button.grid(row=2, column=0, columnspan=2, pady=5)
    
        # Set column 1 to expand horizontally
        self.window.columnconfigure(1, weight=1)

    def dec_window(self):
        self.window = tk.Toplevel()
        self.window.geometry('200x100')
                
        label2 = tk.Label(self.window, text='Quantidade')
        label2.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry2 = tk.Entry(self.window)
        self.entry2.grid(row=0, column=1, padx=5, pady=5, sticky='we')
         # Add a button to close the self.window
        button = tk.Button(self.window, text='Decrementar', command=self.dec)
        button.grid(row=2, column=0, columnspan=2, pady=5)
    
        # Set column 1 to expand horizontally
        self.window.columnconfigure(1, weight=1)

    def inc(self):
        n = self.entry2.get()
        if not validate_number_input(n):
            return
        value = int(n)
        try:
            index = int(str(self.stock_listbox.curselection()).replace(",", "").replace(")", "").replace("(", ""))
        except:
            messagebox.showwarning(title="Aviso", message="Selecione um elemento na janela principal")
            return
        name = self.names[index]
        self.increment(name, value)
        self.window.destroy()

    def dec(self):
        n = self.entry2.get()
        if not validate_number_input(n):
            return
        value = int(n)
        try:
            index = int(str(self.stock_listbox.curselection()).replace(",", "").replace(")", "").replace("(", ""))
        except:
            messagebox.showwarning(title="Aviso", message="Selecione um elemento na janela principal")
            return
        name = self.names[index]
        self.decrement(name, value)
        self.window.destroy()


    def Add_Close(self):
        n = self.entry2.get()
        if not validate_number_input(n):
            return
        self.Add(self.entry1.get(), int(self.entry2.get()))
        self.window.destroy()


    def Add(self, name: str, quantity: int):
        if self.manager.add(name, quantity) != False:
            self.stock_listbox.insert(tk.END, f"{name}  --  {quantity}")
            self.names.append(name)
    
    def remove(self, name: str):
        self.manager.remove(name)
        self.stock_listbox.delete(self.names.index(name))
        self.names.remove(name)

    def increment(self, name: str, i: int):
        ind = self.manager.index(name)
        if (ind != -1):
            self.manager.list[ind].increment(i)
            self.update_value(self.manager.list[ind].name, self.manager.list[ind].quantity)
        

    def decrement(self, name: str,  i: int):
        ind = self.manager.index(name)
        if (ind != -1):
            self.manager.list[ind].decrement(i)
            self.update_value(self.manager.list[ind].name, self.manager.list[ind].quantity)

    def update_value(self, name: str, quantity: int):
        index = self.names.index(name)
        self.stock_listbox.delete(index)
        self.stock_listbox.insert(index, f"{name}  --  {quantity}")


if __name__ == "__main__":
    App()
