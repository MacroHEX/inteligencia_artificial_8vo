from config.database import setup_database
from mods.gui.main_window import launch_gui

# Setup the database
setup_database()

# Launch the GUI
launch_gui()
