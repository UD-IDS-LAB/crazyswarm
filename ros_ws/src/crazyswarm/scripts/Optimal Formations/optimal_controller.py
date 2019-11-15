#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *
import uav_trajectory

#define the final position in one big list or several smaller arrays
#define our total time
time = 10 #total time in seconds

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs


    TIMESCALE = 1.0

    for cf in allcfs.crazyflies:
	#get the initial position from cf.initialPosition
	#get the final position from the variables at the top of the file

	#use the controller to get a polynomial. One for x, one for y. z and yaw can be zero
	#combine the coefficients into one big array that matches the format of figure8.csv

    	traj = uav_trajectory.Trajectory() #creates an empty trajectory object
	# use traj.buildTrajectory(COEFFICIENTS_VARIABLE_NAME)

        cf.uploadTrajectory(0, 0, traj)

    allcfs.takeoff(targetHeight=1.0, duration=2.0)
    timeHelper.sleep(2.5)
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, 1.0])
        cf.goTo(pos, 0, 2.0)
    timeHelper.sleep(2.5)

    allcfs.startTrajectory(0, timescale=TIMESCALE)
    timeHelper.sleep(time * TIMESCALE + 2.0)
  

    allcfs.land(targetHeight=0.06, duration=2.0)
    timeHelper.sleep(3.0)

