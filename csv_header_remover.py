import os
import csv

os.makedirs("header_removed", exist_ok=True)

for file in os.listdir("."):
    if file.endswith(".csv"):
        print("Removing header from: " + file + "...")

        csv_rows = []
        csv_file_obj = open(file)
        csv_reader = csv.reader(csv_file_obj)

        for row in csv_reader:
            if csv_reader.line_num != 1:
                csv_rows.append(row)

        csv_file_obj.close()
        csv_file_obj.open(os.path.join("header_removed", file), "w", newLine="")
        csv_writer = csv.writer(csv_file_obj)

        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()
