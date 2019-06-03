# Mohammed Abdul Mohi
hours = int(input('Please enter the number of hours:'))
RPH = int(input('Please enter the rate per hour:'))
  
Otime_rate = RPH * 1.5
Otime_hours = hours-40

if hours > 40:
  over_pay = Otime_rate * Otime_hours
  pay = 40 * RPH
  total_pay = over_pay + pay
  print('Total Gross Pay:')
  print(total_pay)
else:
  pay = 40 * RPH
  print('Total Gross Pay:')
  print(pay)