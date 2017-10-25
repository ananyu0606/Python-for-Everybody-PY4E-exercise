text = "X-DSPAM-Confidence:    0.8475";
ipos = text.find('0')
#print(ipos)
string = text[ipos:]
#print(string)
value = float(string)
print(value)
