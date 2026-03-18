def get_ai_response(message):

    msg = message.lower()

    if "fever" in msg:
        return "You may take rest and stay hydrated. Consult doctor if persistent."

    elif "headache" in msg:
        return "Reduce screen time and drink water."

    elif "cold" in msg:
        return "Warm fluids and rest can help relieve symptoms."

    elif "hello" in msg:
        return "Hello! I am your AI Health Assistant."

    return "Please consult a healthcare professional for medical advice."
