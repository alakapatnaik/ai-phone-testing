phones= [
    {"name": "iPhone 6", "generation": "old"},
    {"name": "iPhone 6s", "generation": "old"},
    {"name": "iPhone 7", "generation": "old"},
    {"name": "iPhone 8", "generation": "old"},
    {"name": "iPhone X", "generation": "morden"},
    {"name": "iPhone XR", "generation": "morden"},
    {"name": "iPhone 11", "generation": "morden"},
    {"name": "iPhone 12", "generation": "morden"},
    {"name": "iPhone 13", "generation": "morden"},
    {"name": "iPhone 14", "generation": "morden"},
    {"name": "iPhone 15", "generation": "morden"},
    {"name": "iPhone 16", "generation": "morden"},
    {"name": "iPhone 16e", "generation": "morden"},
    {"name": "iPhone 17", "generation": "morden"}
    
]

def predict_phone_generation(phone_name):
    for phone in phones:
        if phone["name"] == phone_name:
            return phone["generation"]
    return "unknown"

import joblib
import os
os.makedirs("models", exist_ok=True)
joblib.dump(predict_phone_generation,"models/phone_model.pkl")
print(os.getcwd)
print("simple phone model saved successfully!")