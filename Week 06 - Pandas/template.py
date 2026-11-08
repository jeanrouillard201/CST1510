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

import pandas as pd
import matplotlib.pyplot as plt

# Reads the CSV file (change the name if your file is called differently)
df = pd.read_csv("templa_records.csv")

# Cleans column names: "Rows Loaded" -> "rows_loaded"
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Shows the real column names (remove this line once it works)
print(df.columns.tolist())

# Calculate the percentage of rows loaded
df["percent"] = (df["rows_load"] / df["rows_expect"]) * 100

# Creates column "status" based on the "percent"
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else
    "WARNING" if p >= 90 else "OK"
)

# OUTPUT

# Prints the full dataframe
print("ALL RECORDS")
print(df)

print()
print()

# Prints records that are not "OK"
print("RECORDS THAT NEED ATTENTION")
print(df[df["status"] != "OK"])

print()
print()

# Counts how much each "status" has occurred
count_status = df.groupby("status").size()
print("COUNT PER STATUS")
print(count_status)

# Loads the whole dataframe into a new CSV file
df.to_csv("temp_report.csv", index=False)

# Creates and saves a bar chart of the status counts
count_status.plot(
    kind="bar",
    title="Status Counter",
    xlabel="Status",
    ylabel="Occurrence (count)"
)

plt.tight_layout()

# Saves the bar chart as a PNG
plt.savefig("Count_Of_Status.png")
plt.close()
