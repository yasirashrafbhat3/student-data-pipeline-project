# Student Data Pipeline

A beginner-friendly Data Engineering project that demonstrates the ETL (Extract, Transform, Load) process using Python and CSV files.

## Project Overview

This project processes student records by extracting data from a CSV file, cleaning duplicate records, handling missing values, converting data types, and saving the cleaned data into a new CSV file.

## Technologies Used

- Python
- CSV module
- Git and GitHub

## Project Structure

```text
student-data-pipeline/
├── data/
│   ├── students.csv
│   └── cleaned_students.csv
├── extract.py
├── transform.py
├── load.py
├── queries.sql
└── README.md
```

## ETL Process

### 1. Extract
- Read student records from `students.csv`.
- Used Python's `csv.DictReader()` to read the data.

### 2. Transform
- Removed duplicate records.
- Identified missing marks.
- Represented missing values using `None`.
- Converted valid marks from strings into integers.

### 3. Load
- Used Python's `csv.DictWriter()` to save cleaned records.
- Generated `cleaned_students.csv`.

## Results

- Original records: 30
- Cleaned records: 28
- Duplicate records removed: 2
- Missing marks identified: 2

## Key Learnings

- Understanding the ETL process.
- Reading and writing CSV files using Python.
- Removing duplicate records.
- Handling missing values.
- Converting data types.
- Understanding basic data pipeline workflows.

## Future Improvements

- Load cleaned data into an SQL database.
- Perform SQL queries on student records.
- Automate the ETL pipeline.
- Add data validation and error handling.

## Author

Yasir Ashraf Bhat

B.Tech Artificial Intelligence and Machine Learning Student