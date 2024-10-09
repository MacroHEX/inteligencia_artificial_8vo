from config.database import initialize_db, close_db


def main():
    # Initialize the database (tables are created inside initialize_db)
    connection = initialize_db()

    if connection:
        # Close the database connection after initialization
        close_db(connection)


if __name__ == "__main__":
    main()
