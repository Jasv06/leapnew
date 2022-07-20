from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd



def main():
    arm = InterbotixRobot(robot_name="rx150", mrd=mrd)
    arm.go_to_home_pose()
    
    arm.set_ee_cartesian_trajectory(z=-0.2)
    
    arm.set_ee_cartesian_trajectory(x=-0.2)
    
    arm.close_gripper()
    
    arm.set_ee_cartesian_trajectory(z=0.2)
    
    arm.set_ee_cartesian_trajectory(x=0.2)
    
    arm.open_gripper()
    
    arm.go_to_sleep_pose(moving_time = 3)

if __name__=='__main__':
    main()
