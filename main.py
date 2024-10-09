import tkinter as tk

from config.database import initialize_db, close_db
from mods.entidad.service.entidad_service import EntidadService
from mods.gui.main_window import MainWindow


def main():
    # Initialize the database
    connection = initialize_db()

    if connection:
        # Create an instance of EntidadService with the existing connection
        entidad_service = EntidadService(connection)

        # Initialize the main window and pass the entidad_service
        root = tk.Tk()
        app = MainWindow(root, entidad_service)
        root.mainloop()

        # Close the database connection after the GUI is closed
        close_db(connection)


if __name__ == "__main__":
    main()
