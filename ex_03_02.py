# ask user to give an input and check if it's a valid answer
hours = input ('Enter Hours:')
try:
 h = float(hours)
except:
 print('Error, please enter the numeric input')
 quit()
rate = input ('Enter Rate:')
try:
  r = float(rate)
except:
 print('Error, please enter the numeric input')
 quit()
# give the employee 1.5 times the hourly rate for hours worked above 40 hours
if h > 40:
 pay = 40 * r + (h-40) * 1.5 * r
else:
 pay = h * r
print('Pay:', pay)
