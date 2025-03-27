import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', "db")
DB_PORT = os.getenv('DB_PORT', "5432")

def connect_db():
    return psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        port=DB_PORT
    )

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            predicted_digit INTEGER NOT NULL,
            true_label INTEGER
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def insert_prediction(predicted_digit, true_label=None):
    """Insert a new prediction into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO predictions (predicted_digit, true_label) VALUES (%s, %s)",
        (predicted_digit, true_label)
    )
    
    conn.commit()
    cursor.close()
    conn.close()


def fetch_predictions():
    """Retrieve all past predictions from the database."""
    conn = connect_db()
    cursor = conn.cursor()

    print('connected')

    cursor.execute("SELECT timestamp, predicted_digit, true_label FROM predictions ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()

    # Get column names from cursor.description
    column_names = [desc[0] for desc in cursor.description]

    # Combine column names and data into a dictionary format
    result = [dict(zip(column_names, row)) for row in data]

    # Print result (Optional)
    print(result)

    cursor.close()
    conn.close()
    return result  # Returns list of tuples (timestamp, predicted_digit, true_label)

