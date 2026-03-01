employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "skills": ["Python", "Django", "Machine Learning"]
}

import json 
employee_data_json = json.dumps(employee_data, indent=4)
print(employee_data_json)

with open ("employee_data_json", 'w') as json_file:
	json_file.write(employee_data_json)

with open("employee_data_json", "r") as json_file:
    data = json.load(json_file)
    print(data)
