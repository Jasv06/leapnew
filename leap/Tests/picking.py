from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np



def main():
    #defines which robot arm we are using 
    #Note: if a different robot name is used other than the one connected the robot wont perfom any action 
    bot = InterbotixManipulatorXS("rx150", "arm", "gripper")
    
    #makes arm leave sleep position 
    bot.arm.set_ee_pose_components(x=0.4, y=0.0,z=0.3, moving_time=2)
    
    #turn the arm 90 degrees counterclockwise
    #bot.arm.set_single_joint_position("waist", np.pi/2.0,moving_time=2)
    #opens the gripper
    #arm.open_gripper()
    #bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.1)
    #bot.gripper.close_gripper()
    #bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.1)
    #bot.arm.set_single_joint_position("waist", -np.pi/2.0,moving_time=3)
    #arm.set_ee_pose_components(x=0.1,z=-0.5)
    #bot.gripper.open_gripper()
    #arm.set_ee_cartesian_trajectory(x=-0.1,z=0.5)
    #bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    #bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    #bot.arm.set_single_joint_position("waist", np.pi/2.0)
    #bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.10)
    #bot.gripper.close_gripper()
    #bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.10)
    #bot.gripper.open_gripper()
    #bot.arm.go_to_home_pose()
    #bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()
