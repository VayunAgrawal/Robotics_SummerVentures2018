from __future__ import print_function
from random import random 
from math import atan2, cos, sin, sqrt, pi
import sys
import os

cwd = os.getcwd()
sys.path.append('/'.join(cwd.split('/')[0:-1]))

from SummerVentures import SimpleVehicle, ang_diff

def pure_pursuit(x_start, y_start, theta_start):
	Kv = 3
	Kh = 6
	Ki = 0.00001
	d = 1
	dt = 0.1
	A = 5

	vehicle = SimpleVehicle(x_start, y_start, theta_start, 1.0)
	
	x = x_start
	y = y_start
	theta = theta_start

	x_goal = -10
	y_goal = A*sin(x_goal)

	x_diff = x_goal-x
	y_diff = y_goal-y
	
	error = sqrt(x_diff**2 + y_diff**2)-d
	totalError = 0
	T = 0

	while True:
		#############YOUR CODE GOES HERE#############
                x_goal = x_goal+ 0.1
                y_goal = A * sin(x_goal)
                v = Kv*error + Ki*totalError*T
                x_diff = x_goal-x
	        y_diff = y_goal-y
                theta_goal = atan2(y_diff, x_diff)
	        distance = sqrt(x_diff**2 + y_diff**2)
                v = Kv*distance
                v_x = v*cos(theta)
                v_y = v*sin(theta)
                x = x + v_x*dt
                y = y + v_y*dt
                theta = theta + Kh*ang_diff(theta_goal, theta)*dt
                vehicle.update_pose(x, y, theta)
                vehicle.plot(xlims = [-10,10], ylims = [-10, 10])
                theta = theta + Kh*ang_diff(theta_goal, theta)*dt
                vehicle.update_pose(x, y, theta)
                vehicle.plot(goal = [x_goal,y_goal], xlims = [-10,10], ylims = [-10, 10])
                error = sqrt(x_diff**2 + y_diff**2) -d
                totalError = totalError + error
		T = T + dt
		#############################################

if __name__ == '__main__':
	if len(sys.argv) == 6:
		try:
			x_start = int(sys.argv[1])
			y_start = int(sys.argv[2])
			theta_start = int(sys.argv[3])
		except ValueError:
			print('Invalid value. Using random values instead')
	else:
		x_start = 20*random()-10
		y_start = 20*random()-10
		theta_start = 2*pi*random()-pi

	print('Starting position: (%f m, %f m)' % (x_start, y_start))
	print('Starting orientation: %f rad' % (theta_start))

	pure_pursuit(x_start, y_start, theta_start)
