import sqlite3
import matplotlib.pyplot as plt
from collections import Counter
import os

# Ensure chart folder exists
os.makedirs("frontend/static/images", exist_ok=True)

# Connect database
conn = sqlite3.connect("pose_data.db")

cursor = conn.cursor()

cursor.execute("SELECT pose, confidence FROM predictions")

rows = cursor.fetchall()

conn.close()

if len(rows) == 0:
    print("No data available")
    exit()

# Extract data
poses = [row[0] for row in rows]
confidences = [row[1] for row in rows]

# Pose Frequency Chart
pose_counts = Counter(poses)

plt.figure()

plt.bar(
    list(pose_counts.keys()),
    list(pose_counts.values())
)

plt.xticks(rotation=45)

plt.title("Pose Frequency")

plt.tight_layout()

plt.savefig(
    "frontend/static/images/pose_chart.png"
)

plt.close()


# Confidence Chart
plt.figure()

plt.plot(confidences)

plt.title("Confidence Trend")

plt.xlabel("Prediction Number")

plt.ylabel("Confidence")

plt.tight_layout()

plt.savefig(
    "frontend/static/images/confidence_chart.png"
)

plt.close()

print("Charts generated successfully ✅")