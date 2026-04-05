def get_accuracy_status(confidence):

    if confidence >= 0.80:
        return "Excellent Pose ✅"

    elif confidence >= 0.60:
        return "Good Pose 👍"

    else:
        return "Needs Improvement ⚠"