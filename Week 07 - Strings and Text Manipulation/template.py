"""
RECORD CHECK  -  my version
===========================

Name  : Jean Rouillard
Lane  :  AI / Data Science
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
from pathlib import Path

def parse_line(raw_line):
    """Converts raw data into a structured dictionary"""

    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)

    survey = survey_part.strip().lower()
    record = {"survey": survey}

    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip().lower()] = float(value.strip())

    return record


def status_of(record):
    """Classify surveys based on rating"""

    rating = record["rating"]

    if rating <= 2:
        return "FLAGGED"
    else:
        return "OK"

# Load raw records from file

from pathlib import Path

path = Path(__file__).parent / "tempmessy.txt"
print("Looking for:", path)

raw_records = []

with open(path) as f:
    for line in f:
        if line.strip():
            raw_records.append(line)
# Process records and print status

tot_records = 0
flagged = 0

print()
print()

for raw_record in raw_records:

    record = parse_line(raw_record)
    status = status_of(record)

    print(f"{record} : {status}")

    tot_records += 1

    if status == "FLAGGED":
        flagged += 1

# Summary of records

print()
print()

print(f"Summary : {tot_records} records\n"
      f"Flagged : {flagged} records")

# Error Testing

print()
print()

try:
    parse_line("Survey_2222, rating=abc,age=def")

except ValueError as err:
    print("Error:", err)


print()
print()
