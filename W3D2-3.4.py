#Mohammed Abdul Mohi

from matplotlib.pyplot import *
from numpy import *
import copy

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

Y_sat = copy.copy(y)
inds = where(y>0.5)[0]
Y_sat[inds] = 0.5
inds = where(y<-0.5)[0]
Y_sat[inds] = -0.5
		

figure(1)
clf()

plot(t,y, 'r--')
plot(t,Y_sat)
title("Mohi.lot")
xlabel("Time(sec)")
ylabel("Y(t)")

show()