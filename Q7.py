import json

file_path = "C:\\Users\\LENOVO\\Documents\\yaml.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)

    # Display data
    for key, value in data.items():
        print(f"{key}: {value}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}. Make sure '{file_path}' contains valid JSON data.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")