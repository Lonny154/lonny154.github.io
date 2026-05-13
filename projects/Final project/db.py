import psycopg2


def get_connection():
    """
    Creates and returns a connection to the PostgreSQL DVD rental database.
    update password, that is just a placeholder not my real password 
    """
    return psycopg2.connect(
        host="localhost",
        database="DVD rental",
        user="postgres",
        password="your_password_here",
        port="5432"
    )