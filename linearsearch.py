parts=["Gear","Bolt","Shaft","Washer"]
key="Shaft"
found=False
for part in parts:
    if part==key:
        found=True
        break
if found:
    print("Part found")
else:
    print("Part not found")