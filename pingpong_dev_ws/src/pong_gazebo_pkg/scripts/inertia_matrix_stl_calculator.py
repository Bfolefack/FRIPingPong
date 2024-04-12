'''
-   This file is intended to be able to calculate the inertial
    matrix of an inputted stl file.
-   This is very useful when defining the intertial tags of
    our URDF files for Gazebo simulation.
-   EDIT: NOT ACCURATE AT THE MOMENT
'''

import numpy
from stl.mesh import Mesh
import rospkg
# from os import path

rospack = rospkg.RosPack()
paddle_stl_path = rospack.get_path('pong_gazebo_pkg') + '/models/paddle/paddle.stl'
#with open(paddle_stl_path, 'rb') as paddle_stl_file:
# paddle_mesh = Mesh.from_file(paddle_stl_path)
paddle_mesh = Mesh.from_file('/home/agalvan-admin/Documents/pong_ws/src/pong_gazebo_pkg/models/paddle/paddle.stl')



# Using an existing closed stl file:


volume, cog, inertia = paddle_mesh.get_mass_properties()
print("Volume                                  = {0}".format(volume))
print("Position of the center of gravity (COG) = {0}".format(cog))
print(inertia)
# print("Inertia matrix at expressed at the COG  = {0}".format(inertia[0,:]))
# print("                                          {0}".format(inertia[1,:]))
# print("                                          {0}".format(inertia[2,:]))

#paddle_stl_file.close()