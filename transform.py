import csv

with open("data/students.csv", "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

print("Original records:", len(students))

# Remove duplicates
unique_students = []
seen = set()

for student in students:
    key = (
        student["name"],
        student["department"],
        student["marks"],
        student["city"]
    )

    if key not in seen:
        seen.add(key)
        unique_students.append(student)

# Handle missing marks and convert valid marks
for student in unique_students:
    if student["marks"] == "":
        student["marks"] = None
    else:
        student["marks"] = int(student["marks"])

print("Clean records:", len(unique_students))
print("Missing marks:", sum(
    1 for student in unique_students
    if student["marks"] is None
))

with open("data/cleaned_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["student_id", "name", "department", "marks", "city"]
    )

    writer.writeheader()
    writer.writerows(unique_students)

print("Cleaned data saved successfully!")