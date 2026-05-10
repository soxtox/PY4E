name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle:
    if line.startswith("From "):
        email = line.split(" ")[1]
        
        d[email]=d.get(email, 0) + 1
            
big_word = None
big_value = None
for word, c  in d.items():
    
    if  big_value is None or c > big_value:
        
        big_value = c
        big_word = email

print(big_word, big_value)
       
