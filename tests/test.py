'''
Author: Yiting CHEN
Date: 2021-10-22 09:56:45
LastEditTime: 2021-10-22 11:39:24
contact me through chenyiting716@gmail.com
'''

import os
import time
import pybullet as p
import pybullet_data
from urdf_models import models_data
import random

# Open GUI and set pybullet_data in the path
p.connect(p.GUI)
p.resetDebugVisualizerCamera(3, 90, -30, [0.0, -0.0, -0.0])
p.setTimeStep(1 / 240.)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


# load urdf data
models = models_data.model_list()

# load model list
namelist = models.model_name_list
print("Look at what we have {}".format(namelist))


# randomly get a model
random_model = namelist[random.randint(0, len(namelist))] 

# Load table and plane
p.loadURDF("plane.urdf")
p.loadURDF("table/table.urdf")

flags = p.URDF_USE_INERTIA_FROM_FILE
obj_id = p.loadURDF(models[random_model], [0., 0., 0.8], flags=flags)

p.setGravity(0, 0, -9.8)

while 1:
    p.stepSimulation()
    time.sleep(1./240)
