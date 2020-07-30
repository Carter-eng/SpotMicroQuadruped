from pynput import keyboard
import numpy as np
import time
from src.State import BehaviorState, State
from src.Command import Command
from src.Utilities import deadband, clipped_first_order_filter


class JoystickInterface:
    def __init__(
        self, config):
        self.config = config
        self.previous_gait_toggle = 0
        self.previous_state = BehaviorState.REST
        self.previous_hop_toggle = 0
        self.previous_activate_toggle = 0

    #    self.message_rate = 50
    #    self.udp_handle = UDPComms.Subscriber(udp_port, timeout=0.3)
    #    self.udp_publisher = UDPComms.Publisher(udp_publisher_port)


    def on_press(key):
        if key == keyboard.Key.esc:
        return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if k in ['t']:
            command.trot_event = (gait_toggle == 1 and self.previous_gait_toggle == 0)
        if k in ['space']:
            command.hop_event = (hop_toggle == 1 and self.previous_hop_toggle == 0)
        if k in ['b']:
            command.activate_event = (activate_toggle == 1 and self.previous_activate_toggle == 0)
        self.previous_gait_toggle = gait_toggle
        self.previous_hop_toggle = hop_toggle
        self.previous_activate_toggle = activate_toggle
        if k in ['right']:
            x_vel = .5 * self.config.max_x_velocity
        elif k in ['left']:
            x_vel = -.5 * self.config.max_x_velocity
        else:
            x_vel = 0

        if k in ['up']:
            y_vel = .5 *  self.config.max_y_velocity
        elif k in ['down']:
            y_vel = -.5 *  self.config.max_y_velocity
        else:
            y_vel = 0
        command.horizontal_velocity = np.array([x_vel, y_vel])
        if k in ['d']:
            command.yaw_rate = .5 * -self.config.max_yaw_rate
        if k in ['a']:
            command.yaw_rate = .5 * self.config.max_yaw_rate
        message_dt = 1.0 / 50
        if k in ['w']:
            pitch = .5 * self.config.max_pitch
        elif k in ['s']:
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
        if k in ['i']:
            command.height = state.height - message_dt * self.config.z_speed * height_movement
        elif k in ['k']:
            command.height = state.height - message_dt * self.config.z_speed * -height_movement
        else:
            command.height = state.height
        if k in ['l']:
            command.roll = state.roll + message_dt * self.config.roll_speed * roll_movement
        elif k in ['k']:
            command.roll = state.roll + message_dt * self.config.roll_speed * -roll_movement
        else:
            command.roll = state.roll
        return command
        
