from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd



def main():
    arm = InterbotixRobot(robot_name="rx150", mrd=mrd)
    arm.go_to_home_pose()
    arm.set_ee_pose_components(x=0.2, y=0.1, z=0.2, roll=1.0, pitch=1.5)
    arm.go_to_home_pose()
    arm.go_to_sleep_pose()

if __name__=='__main__':
    main()
