from config.database import setup_database
from mods.gui.main_window import launch_main_window

# Setup the database
setup_database()

# Launch the main GUI window
launch_main_window()
