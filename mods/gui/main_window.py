import tkinter as tk
from mods.gui.entity_window import launch_entity_window
from mods.gui.invoice_window import launch_invoice_window
from mods.gui.item_window import launch_item_window


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Facturación Digital")
        self.root.geometry("400x300")

        # Buttons to open other windows
        self.entity_button = tk.Button(self.root, text="Administrar Entidades}", command=launch_entity_window)
        self.entity_button.pack(pady=10)

        self.invoice_button = tk.Button(self.root, text="Administrar Facturas", command=launch_invoice_window)
        self.invoice_button.pack(pady=10)


def launch_main_window():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
