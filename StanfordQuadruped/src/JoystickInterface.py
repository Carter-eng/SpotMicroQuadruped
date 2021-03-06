from pynput import keyboard
import numpy as np
import time
from src.State import BehaviorState, State
from src.Command import Command
from src.Utilities import deadband, clipped_first_order_filter
from pupper.Config import Configuration
config = Configuration()
command = Command()
state = State()

class JoystickInterface:
    def __init__(
        self, config):
        self.config = config
        self.previous_gait_toggle = 0
        self.previous_state = BehaviorState.REST
        self.previous_hop_toggle = 0
        self.previous_activate_toggle = 0
        self.gait_toggle = 0
       
    #    self.message_rate = 50
    #    self.udp_handle = UDPComms.Subscriber(udp_port, timeout=0.3)
    #    self.udp_publisher = UDPComms.Publisher(udp_publisher_port)
    

    def get_command(self, chosenKey):
        global command, state, config
        while True:
            keytest = str(chosenKey)
            print(type(keytest))
            print(keytest)
            if keytest == 't':
                self.gait_toggle = 1
                print('PASS')
            else:
                print('FAIL')
            print(self.gait_toggle)
            command.trot_event = (self.gait_toggle == 1 and self.previous_gait_toggle == 0)
            hop_toggle = 0
            if chosenKey == 'Key.space':
                hop_toggle = 1
            command.hop_event = (hop_toggle == 1 and self.previous_hop_toggle == 0)
            activate_toggle = 1
            if chosenKey == 'b':
                activate_toggle = 1
            command.activate_event = (activate_toggle == 1 and self.previous_activate_toggle == 0)
            self.previous_gait_toggle = self.gait_toggle
            self.previous_hop_toggle = hop_toggle
            self.previous_activate_toggle = activate_toggle
            if chosenKey == 'Key.right':
                x_vel = .5 * self.config.max_x_velocity
            elif chosenKey == 'Key.left':
                x_vel = -.5 * self.config.max_x_velocity
            else:
                x_vel = 0

            if str(chosenKey) == 'p':
                y_vel = config.max_y_velocity
                print('test')
            elif chosenKey == 'o':
                y_vel = -config.max_y_velocity
            else:
                y_vel = 0
            command.horizontal_velocity = np.array([x_vel, .4])
#             print(command.horizontal_velocity)
            
            if chosenKey == 'd':
                command.yaw_rate = .5 * -self.config.max_yaw_rate
            if chosenKey == 'a':
                command.yaw_rate = .5 * self.config.max_yaw_rate
            message_dt = 1.0 / 50
            if chosenKey == 'w':
                pitch = .5 * self.config.max_pitch
            elif chosenKey == 's':
                pitch = .5 * -self.config.max_pitch
            else:
                pitch = 0
            deadbanded_pitch = deadband(
                pitch, self.config.pitch_deadband
            )
            pitch_rate = clipped_first_order_filter(
                state.pitch,
                deadbanded_pitch,
                self.config.max_pitch_rate,
                self.config.pitch_time_constant,
            )
            command.pitch = state.pitch + message_dt * pitch_rate
            if chosenKey == 'i':
                command.height = state.height - message_dt * self.config.z_speed * height_movement
            elif chosenKey == 'k':
                command.height = state.height - message_dt * self.config.z_speed * -height_movement
            else:
                command.height = state.height
            if chosenKey == 'l':
                command.roll = state.roll + message_dt * self.config.roll_speed * roll_movement
            elif chosenKey == 'k':
                command.roll = state.roll + message_dt * self.config.roll_speed * -roll_movement
            else:
                command.roll = state.roll
            return command

