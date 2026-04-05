import sqlite3
from datetime import datetime

# Create database
def init_db():

    conn = sqlite3.connect("pose_data.db")

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pose TEXT,
            confidence REAL,
            timestamp TEXT

        )

    """)

    conn.commit()
    conn.close()


# Save prediction
def save_prediction(pose, confidence):

    conn = sqlite3.connect("pose_data.db")

    cursor = conn.cursor()

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""

        INSERT INTO predictions (pose, confidence, timestamp)

        VALUES (?, ?, ?)

    """, (pose, confidence, time_now))

    conn.commit()
    conn.close()