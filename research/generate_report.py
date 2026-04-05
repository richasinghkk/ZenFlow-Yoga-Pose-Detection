import sqlite3
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Connect database
conn = sqlite3.connect("pose_data.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT pose, confidence, timestamp FROM predictions"
)

rows = cursor.fetchall()

conn.close()

# PDF setup
doc = SimpleDocTemplate("Yoga_Report.pdf")

elements = []

styles = getSampleStyleSheet()

# Title
title = Paragraph(
    "ZenFlow Yoga Session Report",
    styles['Title']
)

elements.append(title)

elements.append(Spacer(1, 12))

# Table data
data = [["Pose", "Confidence", "Timestamp"]]

for row in rows:

    pose = row[0]

    confidence = f"{round(row[1]*100,2)}%"

    timestamp = row[2]

    data.append([
        pose,
        confidence,
        timestamp
    ])

# Create table
table = Table(data)

table.setStyle(TableStyle([

    ("BACKGROUND", (0,0), (-1,0), colors.grey),

    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),

    ("GRID", (0,0), (-1,-1), 1, colors.black)

]))

elements.append(table)

# Build PDF
doc.build(elements)

print("Yoga_Report.pdf generated successfully ✅")