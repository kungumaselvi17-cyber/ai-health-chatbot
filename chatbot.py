import pandas as pd

data = pd.read_csv("model/health_data.csv")

def get_ai_response(message):

    msg = message.lower()

    for i,row in data.iterrows():
        if row["symptom"] in msg:
            return f"Possible condition: {row['disease']}. Advice: {row['advice']}"

    return "Please consult a healthcare professional."
