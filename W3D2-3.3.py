#Mohammed Abdul Mohi

from numpy import *
from matplotlib.pyplot import *
import copy

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

Y_sat = copy.copy(y)
Y_sat[Y_sat>0.5] = 0.5
Y_sat[Y_sat<-0.5] = -0.5
		

figure(1)
clf()

plot(t,y, 'r--')
plot(t,Y_sat)
title("Mohi.plot")
xlabel("Time(sec)")
ylabel("Y(t)")

show()