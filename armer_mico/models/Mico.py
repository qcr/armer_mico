#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from rospkg import RosPack

class Mico(ERobot):

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read("robots/m1n4s200_standalone.xacro", tld=RosPack().get_path('armer_mico') + '/data/xacro')

        super().__init__(
            links,
            name=name,
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
            manufacturer="Kinova", 
            gripper_links=links[7]
        )
        
        self.addconfiguration(
            "qr", np.array([0, 0, 0, 0])
        )

if __name__ == "__main__":  # pragma nocover
    robot = Mico()
    print(robot)