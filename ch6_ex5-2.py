# among the prompted number, calculate the largest and smallest number handing the bad data
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        
        break
    
    try:
        fnum = int(num)
        if largest is  None or fnum > largest :
            largest = fnum
            
        if smallest is  None or fnum < smallest :
            smallest = fnum
        
       
    except:
        print('Invalid input')
        
print("Maximum is", largest)
print("Minimum is", smallest)
