"""
MicoROSRobot module defines the MicoROSRobot type

MicoROSRobot provides robot-specific callbacks for state

.. codeauthor:: Gavin Suddreys
"""
import rospy
import actionlib
import roboticstoolbox as rtb

from armer.robots import ROSRobot

from kinova_msgs.msg import JointVelocity

class MicoROSRobot(ROSRobot):
    def __init__(self,
                 robot: rtb.robot.Robot,
                 *args, 
                 **kwargs):

        super().__init__(robot, *args, **kwargs)

        self.joint_publisher = rospy.Publisher(
            '/m1n4s200_driver/in/joint_velocity',
            JointVelocity,
            queue_size=1
        )
        rate=rospy.Rate(100)
    

    def publish(self):
        mico_msg=JointVelocity()
        mico_msg.joint1=self.qd[0]
        mico_msg.joint2=self.qd[1]
        mico_msg.joint3=self.qd[2]
        mico_msg.joint4=self.qd[3]
        mico_msg.joint5=self.qd[0]
        mico_msg.joint6=0
        mico_msg.joint7=0
        
        self.joint_publisher.publish(mico_msg)

