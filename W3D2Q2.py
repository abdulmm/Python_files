#Mohammed Abdul Mohi
hours = int(input("Please enter the number of hours: "))
RPH = int(input("Please enter the rate per hour: "))

def computepay(hours,RPH):
  if hours > 40:
    pay = (RPH*40)+(RPH*1.5*(hours-40))
  else :
    pay = RPH * 40
  return pay
print ('Your Gross Pay is: ')  
print (computepay(hours,RPH))
