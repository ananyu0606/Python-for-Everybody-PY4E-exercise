hours = input ('Enter Hours:')
rate = input ('Enter Rate:')
h = float(hours)
r = float(rate)
# give the employee 1.5 times the hourly rate for hours worked above 40 hours
if h > 40:
 pay = 40 * r + (h-40) * 1.5 * r
else:
 pay = h * r
print('Pay:', pay)
