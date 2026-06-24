import json
import os

def load_data(file_path):
    """
    Load JSON data from the specified file path.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
        
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    return data

def save_data(data, file_path):
    """
    Save JSON data to the specified file path.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
