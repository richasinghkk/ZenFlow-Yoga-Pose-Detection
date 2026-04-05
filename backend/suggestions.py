# Pose correction suggestions

pose_suggestions = {

    "Vrksasana": [
        "Keep your back straight",
        "Focus your gaze forward",
        "Balance your weight evenly"
    ],

    "Balasana": [
        "Relax your shoulders",
        "Keep your hips touching heels",
        "Stretch your arms forward"
    ],

    "Bakasana": [
        "Engage your core muscles",
        "Keep elbows slightly bent",
        "Shift weight forward slowly"
    ],

    "Bhujangasana": [
        "Lift chest gently",
        "Keep shoulders relaxed",
        "Avoid locking elbows"
    ],

    "Navasana": [
        "Keep spine straight",
        "Engage abdominal muscles",
        "Balance evenly"
    ]

}


def get_suggestions(pose):

    return pose_suggestions.get(
        pose,
        ["Maintain correct posture"]
    )