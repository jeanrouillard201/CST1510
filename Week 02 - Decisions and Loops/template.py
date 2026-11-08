"""
RECORD CHECK  -  my version
===========================

Name  : Jean Rouillrd
Lane  :  AI / Data Science
Date  : 30/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label =input("Enter Data set name : ") 
value_load = float(input("Enter the value: ")) #data load (entry)
limit_except = float(input("Enter the limit: ")) 


difference = limit_except - value_load
percent = (value_load / limit_except) * 100 #calculates percentage of value and limit

if percent >= 100:
    status = "OVER THE LIMIT" #Status based on percentage
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"



print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Failed      : {value_load:>10.2f}")
print(f"  Total       : {limit_except:>10.2f}")
print(f"  Remaining   : {difference:>10.2f}")
print(f"  Percent     : {percent:>9.2f} %")
print(f"  Status      : {status:>10}")
print("=" * 34)
print()
