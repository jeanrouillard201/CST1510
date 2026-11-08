"""
RECORD CHECK  -  my version
===========================

Name  : Jean Rouillard
Lane  :  AI / Data Science
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Return OVER LIMIT, WARNING or OK based on the failure percentage."""
    if percent >= 100.0:
        return "OVER LIMIT"
    elif percent >= 90.0:
        return "WARNING"
    else:
        return "OK"
 
 
def check(value, limit):
    """Return the difference and percentage"""
    difference = limit - value
    percent = (value / limit) * 100.0
    return difference, percent
 
 
def print_report(label, value, limit, difference, percent, status):
    """Print The Data"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Rows loaded    : {value:10.2f}")
    print(f"  Rows expected  : {limit:10.2f}")
    print(f"  Rows passed    : {difference:10.2f}")           # outputs are fully operational
    print(f"  Percent         : {percent:10.2f} %")
    print(f"  Status          : {status:>10}")
    print("=" * 34)
 
label = ""
over_limit_count = 0



while True:
    label = input("Enter Data set name : ")
    if label.lower() == "quit":
        break
    value = float(input("Enter rows loaded : "))
    limit = float(input("Enter rows expected : "))
    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count += 1
    # calling print report for the outputs
    print_report(value=value, label=label, limit=limit, difference=difference, percent=percent, status=status)
     # calling print report for the outputs 
 
print()
print(f"Amounts over limit: {over_limit_count}")


