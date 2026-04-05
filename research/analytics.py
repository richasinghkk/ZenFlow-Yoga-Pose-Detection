import sqlite3
import matplotlib.pyplot as plt
from collections import Counter

# Connect to database
conn = sqlite3.connect("pose_data.db")

cursor = conn.cursor()

cursor.execute("SELECT pose, confidence FROM predictions")

rows = cursor.fetchall()

conn.close()

# Separate data
poses = [row[0] for row in rows]
confidences = [row[1] for row in rows]

# Count pose frequency
pose_counts = Counter(poses)

pose_names = list(pose_counts.keys())
pose_values = list(pose_counts.values())

# 📊 Bar Chart — Pose Frequency

plt.figure()

plt.bar(pose_names, pose_values)

plt.title("Yoga Pose Frequency")

plt.xlabel("Pose")

plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# 📈 Line Chart — Confidence Trend

plt.figure()

plt.plot(confidences)

plt.title("Confidence Trend")

plt.xlabel("Prediction Number")

plt.ylabel("Confidence")

plt.tight_layout()

plt.show()