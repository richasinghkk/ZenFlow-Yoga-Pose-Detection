import sqlite3
from datetime import datetime
from collections import Counter

conn = sqlite3.connect("pose_data.db")

cursor = conn.cursor()

today = datetime.now().strftime("%Y-%m-%d")

cursor.execute(
    "SELECT pose, confidence, timestamp FROM predictions"
)

rows = cursor.fetchall()

conn.close()

today_poses = []
today_conf = []

for row in rows:

    if today in row[2]:

        today_poses.append(row[0])
        today_conf.append(row[1])

if len(today_poses) == 0:

    summary = {
        "total": 0,
        "most_pose": "None",
        "avg_conf": 0
    }

else:

    pose_counts = Counter(today_poses)

    most_pose = pose_counts.most_common(1)[0][0]

    avg_conf = sum(today_conf) / len(today_conf)

    summary = {
        "total": len(today_poses),
        "most_pose": most_pose,
        "avg_conf": round(avg_conf*100,2)
    }

print(summary)