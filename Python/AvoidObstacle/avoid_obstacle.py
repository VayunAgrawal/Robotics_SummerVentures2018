from __future__ import print_function
from math import atan2, cos, sin, sqrt, pi
import sys
import os

cwd = os.getcwd()
sys.path.append('/'.join(cwd.split('/')[0:-1]))

from SummerVentures import SimpleVehicle, ang_diff

def avoid_obstacle():
	Kv = 3
	Kh = 6
	Ki = 0.00001
	d = 2
	dt = 0.1

	x = 0.0
	y = 0.0
	theta = 0.0

	x_obstacle = 10.0
	y_obstacle = 0.0

	x_waypoint = 10.0
	y_waypoint = 5.0

	x_goal = 20.0
	y_goal = 0.0

	m1 = (y_waypoint-y)/(x_waypoint-x)
	b1 = y_waypoint-m1*x_waypoint

	m2 = (y_goal-y_waypoint)/(x_goal-x_waypoint)
	b2 = y_goal-m2*x_goal

	x_pursuit = x
	y_pursuit = y

	vehicle = SimpleVehicle(x, y, theta, 1)

	x_diff = x_pursuit-x
	y_diff = y_pursuit-y
	
	error = sqrt(x_diff**2 + y_diff**2)-d
	totalError = 0
	T = 0

	while sqrt((x-x_goal)**2+(y-y_goal**2)**2) > 1:
		#############YOUR CODE GOES HERE#############

                while x<=10:
                        x_pursuit = x_pursuit+ 0.1
                        y_pursuit = m1*x_pursuit+b1
                        v = Kv*error + Ki*totalError*T
                        x_diff = x_pursuit-x
	                y_diff = y_pursuit-y
                        theta_goal = atan2(y_diff, x_diff)
	                distance = sqrt(x_diff**2 + y_diff**2)
                        v = Kv*distance
                        v_x = v*cos(theta)
                        v_y = v*sin(theta)
                        x = x + v_x*dt
                        y = y + v_y*dt
                        theta = theta + Kh*ang_diff(theta_goal, theta)*dt
                        vehicle.update_pose(x, y, theta)
                        theta = theta + Kh*ang_diff(theta_goal, theta)*dt
                        vehicle.update_pose(x, y, theta)
                        vehicle.plot(goal = [x_goal,y_goal], xlims = [0,20], ylims = [-10, 10], obstacles =[[x_obstacle,y_obstacle,150]])
                        error = sqrt(x_diff**2 + y_diff**2)-d
                        T = T + dt

                while x>10:
                        x_pursuit = x_pursuit+ 0.1
                        y_pursuit = m2*x_pursuit+b2
                        v = Kv*error + Ki*totalError*T
                        x_diff = x_pursuit-x
	                y_diff = y_pursuit-y
                        theta_goal = atan2(y_diff, x_diff)
	                distance = sqrt(x_diff**2 + y_diff**2)
                        v = Kv*distance
                        v_x = v*cos(theta)
                        v_y = v*sin(theta)
                        x = x + v_x*dt
                        y = y + v_y*dt
                        theta = theta + Kh*ang_diff(theta_goal, theta)*dt
                        vehicle.update_pose(x, y, theta)
                        theta = theta + Kh*ang_diff(theta_goal, theta)*dt
                        vehicle.update_pose(x, y, theta)
                        vehicle.plot(goal = [x_goal,y_goal], xlims = [0,20], ylims = [-10, 10], obstacles = [[x_obstacle,y_obstacle,150]])
                       	error = sqrt(x_diff**2 + y_diff**2)-d
                        T = T + dt
                        
		#############################################

if __name__ == '__main__':
	avoid_obstacle()
