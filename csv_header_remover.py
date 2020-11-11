import os
import csv

os.makedirs("header_removed", exist_ok=True)

for file in os.listdir("."):
    if file.endswith(".csv"):
        print("Removing header from: " + file + "...")

        csv_rows = []
        csv_file_obj = open(file)
        reader_obj = csv.reader(csv_file_obj)

        for row in reader_obj:
            if reader_obj.line_num != 1:
                csv_rows.append(row)

        csv_file_obj.close()
