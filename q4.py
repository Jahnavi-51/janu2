'''import csv

file_path = "C:\\Users\\LENOVO\\Documents\\data.csv"

with open(file_path, "r", newline='') as file:
    reader = csv.reader(file)

    headers = next(reader)

    file.seek(0)
    next(reader)

    column_widths = [max(len(header), max(len(row[i]) for row in reader)) for i, header in enumerate(headers)]

    file.seek(0)
    next(reader)

    for i, header in enumerate(headers):
        print(f"{header.ljust(column_widths[i])}", end=' | ')
    print()
    print('-' * (sum(column_widths) + len(column_widths) - 1))

    for row in reader:
        for i, data in enumerate(row):
            print(f"{data.ljust(column_widths[i])}", end=' | ')
        print()
import pandas as pd

# Read the CSV file
data = pd.read_csv('sample.csv')

# Display the dataframe
print(data)

import csv

file_path = "C:\\Users\\LENOVO\\Documents\\data.csv"

with open(file_path, "r", newline='') as file:
    reader = csv.reader(file)

    headers = next(reader)
    rows = list(reader)

    column_widths = [max(len(header), max(len(row[i]) for row in rows)) for i, header in enumerate(headers)]

    for i, header in enumerate(headers):
        print(f"{header.ljust(column_widths[i])}", end=' | ')
    print()
    print('-' * (sum(column_widths) + len(column_widths) - 1))

    for row in rows:
        for i, data in enumerate(row):
            print(f"{data.ljust(column_widths[i])}", end=' | ')
        print()'''
import pandas as pd
from tabulate import tabulate

file_path = "C:\\Users\\LENOVO\\Documents\\data.csv"

df = pd.read_csv(file_path)

print(tabulate(df, headers='keys', tablefmt='grid'))