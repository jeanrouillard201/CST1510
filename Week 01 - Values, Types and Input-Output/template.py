"""
RECORD CHECK  -  my version
===========================

Name  : Jean Rouillard
Lane  :  AI / Data Science 
Date  : 29/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label =input("Enter Data set name : ") 
row_load =float(input("Enter rows loaded : "))    #converts into float 
row_expect =float(input("Enter rows expected : "))    

difference = (row_expect-row_load)
percent = (row_load/row_expect)*100    


print("=" * 34) 
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"""Row load         : {row_load:>10.2f} 
Row Expect      : {row_expect:>10.2f}
Difference          : {difference:>+10.2f} 
Percentage filled   : {percent:>10.2f} %
Percentage Unused   : {100 - percent:>10.2f} %"""
)
print("=" * 34)
