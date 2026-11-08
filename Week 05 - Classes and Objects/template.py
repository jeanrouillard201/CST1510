"""
RECORD CHECK  -  my version
===========================

Name  : Jean Rouillard
Lane  :  AI / Data Science
Date  : 04/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Assigns label, value, limit to local variables"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns status deduced from value and limit"""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"

        elif percent >= 90:
            return "WARNING"

        else:
            return "OK"


def load_records(path):
    """Reads and converts a file into a list of Record"""
    records = []

    with open(path) as f:
        for line in f:
            ln = line.strip()
            label, value, limit = ln.split(",")

            value = float(value)
            limit = float(limit)

            records.append(Record(label, value, limit))

    return records



records = load_records("templaterecords.txt")

for record in records:

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"Rows loaded   : {record.value}")
    print(f"Rows expected : {record.limit}")
    print(f"Status        : {record.status()}")

    print("=" * 34)


print(f"Overlimit : {Record.over_limit_count}")
