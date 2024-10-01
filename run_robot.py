import time

import numpy as np
np.set_printoptions(suppress=True, precision=10)

from dynamixel_interface import Reacher
from absl import flags
from absl import app

flags.DEFINE_float("max_error", 5.0, "max tolerance for error in position. Ideally the steady state error should be less than this value.")
flags.DEFINE_float("max_delta_pos_error", 0.0001, "max tolerance for the joint moving after reaching the steady state")
FLAGS = flags.FLAGS

from collections import deque

def main(argv):
    # Initialize the robot interface
    reacher = Reacher()
    time.sleep(0.25)
    print("reacher: ", reacher)

    # Reset
    print("Resetting the elbow joint.")
    reacher.reset()
    time.sleep(1)

    # Move the robot to a specific positions and calculate the time it took to move
    start_time = time.time()

    target_pos = None
    if target_pos is not None:
        reacher.set_joint_position_by_id(target_pos, 3)
    else:
        raise Exception("Please set the target position for the elbow joint in the code.") 

    # The deque is used to check the values of the last 5 elbow joint positions
    fifo_queue = deque()
    last_5_pos = []
    steady = False
    current_execution_time = 0
    
    # Get the current position of the elbow joint
    current_pos = reacher.get_joint_position_by_id([3])
    joint_pos_error = np.abs(target_pos - current_pos)

    while joint_pos_error > FLAGS.max_error or not steady:

        if current_execution_time > 20.0:
            raise Exception("Timeout: stopping the script as it is taking too long to reach the target elbow joint position")

        current_pos = reacher.get_joint_position_by_id([3])
        joint_pos_error = np.abs(target_pos - current_pos)

        if len(fifo_queue) > 4: 
            fifo_queue.popleft()

        fifo_queue.append(current_pos)

        # If this condition is satisfied then the motor has reaced its steady state phase (i.e. now it is not moving)
        if len(fifo_queue) == 5 and all(x == fifo_queue[0] for x in fifo_queue):
            steady = True

        end_time = time.time()
        current_execution_time = end_time - start_time
        
    # End time
    end_time = time.time()

    # Calculate the total time taken to move the elbow joint
    execution_time = end_time - start_time
    print(f"=== Time taken to move the elbow joint: {execution_time:.5f} seconds ===")

if __name__ == "__main__":
    app.run(main)