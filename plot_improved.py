#Mohammed Abdul Mohi

import numpy as np
import matplotlib.pyplot as plt

courses = np.genfromtxt('courses.txt',dtype = 'str',delimiter=',')
grades = np.fromfile('grades.txt',dtype=int,sep=',')

x = np.arange(len(courses))
 
plt.figure(1)
plt.clf
plt.bar(x,grades)
plt.xticks(x,courses)
plt.ylabel('Grades')
plt.xlabel('Course Names')
plt.title('Grades for last 5 courses')
plt.ylim(0,4)
plt.show()
 
 