import csv
import os
import sys

print (sys.argv) 
print(sys.argv[1])
input_file_name = sys.argv[1]
output_file_name = sys.argv [2]
changes = sys.argv[3:]


files_in_our_folder = os.listdir()
file_name = sys.argv[1]
file_name_csv = sys.argv[2]

if file_name in files_in_our_folder:  
    all_products = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            all_products.append(row)
    for change in changes:
        split_content = change.split(",")
        column_int = int(split_content[0])
        row_int = int(split_content[1])
        change_cell = split_content[2]


        if 0 <= column_int <= len(all_products[0]) and 0 <= row_int <= len(all_products):
            all_products[row_int ][column_int] = change_cell
        else:
         print("Invalid row or column index. Change and save failed.")

    with open(file_name_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(all_products)

        print("Changes saved successfully.")

else:
    print("The file does not exist. Files:", os.listdir())