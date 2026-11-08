"""
RECORD CHECK  -  my version
===========================

Name  : Jean Rouillard 
Lane  :  AI / Data science
Date  :  14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
 

def check_record(value, limit):
    """Calculate difference, percentage and status."""

    if limit <= 0:
        raise ValueError("Limit must be greater than zero.")

    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Display the record report."""

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Rows loaded   : {value:>10.2f}")
    print(f"Rows expected : {limit:>10.2f}")
    print(f"Free          : {difference:>10.2f}")
    print(f"Percentage    : {percent:>10.2f}%")
    print(f"Status        : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Read records from the input file."""

    file_data = []

    with open(path, "r") as f:
        for line in f:
            ln = line.strip()

            if not ln:
                continue

            label, value, limit = ln.split(",")

            value = float(value)
            limit = float(limit)

            difference, percent, status = check_record(value, limit)

            file_data.append({
                "label": label.strip(),
                "value": value,
                "limit": limit,
                "difference": difference,
                "percent": percent,
                "status": status
            })

    return file_data


# MAIN PROGRAM

overlimit = 0

try:
    records = load_records("templaterecords.txt")

    with open("templateresults.txt", "w") as f:

        for line in records:

            label = line["label"]
            value = line["value"]
            limit = line["limit"]
            difference = line["difference"]
            percent = line["percent"]
            status = line["status"]

            # Display report
            print_report(
                label, value, limit,
                difference, percent, status
            )

            # Count over-limit records
            if status == "OVER LIMIT":
                overlimit += 1

            # Save individual result
            f.write(f"{label} - {status}\n")

        # Save total count in text file
        f.write("\n")
        f.write(f"Total Overlimit = {overlimit}\n")

    # Display saved results
    with open("templateresults.txt", "r") as results:
        print("\nFINAL RESULTS")
        print(results.read())

except FileNotFoundError:
    print("File does not exist. Check your input filename.")

except ValueError as error:
    print("Invalid data:", error)
