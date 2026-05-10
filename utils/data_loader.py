import pandas as pd

def load_data():
    df = pd.DataFrame({
        "City": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "Sales": [250, 400, 180, 300],
        "Profit": [50, 120, 30, 80]
    })
    return df