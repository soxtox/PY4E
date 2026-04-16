#strings manipulation and slicing the required data
text = "X-DSPAM-Confidence:    0.8475"
tab = text.find(' ')
req = text[19:]
r= req.lstrip()
r_float = float(r)
print(r_float)
