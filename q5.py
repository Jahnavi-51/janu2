import csv

file_path = "C:\\Users\\LENOVO\\Documents\\data.csv"


# Function to get user input and write it to the CSV file
def add_row_to_csv(file_path):
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")

    with open(file_path, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, city])
    print("Row added successfully!")


# Run the function to add a row
add_row_to_csv(file_path)