#Mohammed Abdul Mohi

from numpy import *
from matplotlib.pyplot import *

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

Y_sat = zeros(len(y))

for i, item in enumerate(y):
	if item > 0.5:
		Y_sat[i] = 0.5
	elif item < -0.5:
		Y_sat[i] = -0.5
	else:
		Y_sat[i] = item
		

figure(1)
clf()

plot(t,y, 'r--')
plot(t,Y_sat)
title("Mohi.plot")
xlabel("Time(sec)")
ylabel("Y(t)")

show()