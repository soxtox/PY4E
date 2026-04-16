#use function for calculating the previous chapter exercise for pay with overtime
def computepay(h, r):
    if h > 40:
        return 40 * r +(h-40)*(1.5 * r)
    else:
        return h * r

hrs = input("Enter Hours:")
rts = input("Enter Rates:")
p = computepay(float(hrs), float(rts))
print("Pay", p)
