name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split(" ")[6]
        hour = time.split(":")[0]
        d[hour]=d.get(hour, 0) + 1
        
sorted_dict = sorted(d.items())
for k,v in sorted_dict:
    print (k,v)
