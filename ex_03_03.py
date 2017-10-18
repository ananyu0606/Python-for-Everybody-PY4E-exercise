score = input("Enter Score: ")
# If entering score is not numeric or is not a valid number, end the program
try:
 score = float(score)
except:
 print('Bad score')
 quit()
#grading with the following table
if score <= 0 or score >= 1.0:
 print('error')
elif score >= 0.9:
 print('A')
elif score >= 0.8:
 print('B')
elif score >= 0.7:
 print('C')
elif score >= 0.6:
 print('D')
else:
 print('F')
