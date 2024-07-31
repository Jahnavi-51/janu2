'''import json

file_path = "C:\\Users\\LENOVO\\Documents\\json.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)

    for key, value in data.items():
        print(f"{key}: {value}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")'''
"""import json
def read_json(file_path):
    with open(file_path,"r") as f:
        data = json.load(f)
        return data
file_path ="C:\\Users\\LENOVO\\Documents\\json.json"

json_data = read_json(file_path)
print(json_data)"""

