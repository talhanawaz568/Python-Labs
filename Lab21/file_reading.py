import csv
file_path = 'data.csv'

with open(file_path, mode='r') as file:
	pass	#File opened in read mode
### SKIPPING THE HEADER
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next (csv_reader)
    for row in csv_reader:
       print(row)  

### STORING CSV DATA N LIST OF DICTINARIES
data_list = []
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_list.append(row)

# Print the list of dictionaries
for item in data_list:
    print(item)
