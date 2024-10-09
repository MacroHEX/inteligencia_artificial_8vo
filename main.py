import tkinter as tk

from config.database import initialize_db, close_db
from mods.gui.main_window import MainWindow


def main():
    # Initialize the database (tables are created inside initialize_db)
    connection = initialize_db()

    if connection:
        # Initialize the main window for the GUI
        root = tk.Tk()
        app = MainWindow(root)
        root.mainloop()

        # Close the database connection after the GUI is closed
        close_db(connection)


if __name__ == "__main__":
    main()
