hostname = input("Enter hostname: ")
used_gb = float(input("Enter GB used: "))
total_gb = float(input("Enter GB total: "))
net_variance_gb = used_gb - total_gb
percent_used = (used_gb / total_gb) * 100.0
megabytes_used = used_gb * 1024.0
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used          : {used_gb:>10.2f}")
print(f"  Total         : {total_gb:>10.2f}")
print(f"  Net Variance  : {net_variance_gb:>+10.2f}")
print(f"  Percent Used  : {percent_used:>10.2f} %")
print(f"  MB Used       : {megabytes_used:>10.2f}")
print("=" * 34)
