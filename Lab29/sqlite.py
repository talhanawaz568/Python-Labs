import sqlite3
connection = sqlite3.connect(":memory:")

#CREATING THE TABLE AND CONNECTION WITH DATABASE
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE students (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	grade REAL
)
""")

#INSERTING THE DATA TO TABLE
students_data = [
    (1, 'Alice', 85.5),
    (2, 'Bob', 78.0),
    (3, 'Charlie', 92.0)
]

#Adding the values to table
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students_data)
connection.commit()

#Fetching the results
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()

#Show each row result
for row in results:
    print(row)
