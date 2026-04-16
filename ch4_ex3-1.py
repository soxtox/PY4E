# prompt hour and rate and calculate the pay with overtime
hrs = input("Enter Hours:")
h = float(hrs)
rts = input("Enter Rates:")
r = float(rts)

if h <= 40:
    gross = h * r
    
if h > 40:
    gross = 40 * r + (h-40) *(r * 1.5)
    
print (gross)
