import sqlite3
import os
from datetime import datetime


# 📁 Get project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# 📌 Correct database path
db_path = os.path.join(
    BASE_DIR,
    "pose_data.db"
)


# 🧱 Initialize Database
def init_db():

    conn = sqlite3.connect(db_path)

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


# 💾 Save Prediction
def save_prediction(pose, confidence):

    # Ensure table exists
    init_db()

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    time_now = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""

        INSERT INTO predictions
        (pose, confidence, timestamp)

        VALUES (?, ?, ?)

    """, (pose, confidence, time_now))

    conn.commit()

    conn.close()