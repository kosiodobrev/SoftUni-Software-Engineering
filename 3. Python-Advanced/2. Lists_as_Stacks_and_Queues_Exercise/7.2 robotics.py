from collections import deque

robots_data = input().split(";")
robots_list = []
for robot in robots_data:
    robot_name, process_time = robot.split('-')
