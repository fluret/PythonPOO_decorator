from robot import IndustrialRobot

robot = IndustrialRobot()
robot.rotate_body_left()
robot.move_arm_up(15)
robot.weld()

robot.rotate_body_right(20)
robot.move_arm_down(5)
robot.weld()