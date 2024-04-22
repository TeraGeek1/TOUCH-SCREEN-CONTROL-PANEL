from tkinter import *
from tkinter import Misc, ttk
from tkdial import Meter
import threading as thrd
import time

import random


class Dial(Meter):
    def __init__(
        self,
        master,
        start: float = 0,
        end: float = 100,
        radius: int = 250,
        width: int = None,
        height: int = None,
        text: str = " ",
        text_color: str = "black",
        text_font: str = None,
        border_width: int = 1,
        border_color: int = "grey40",
        major_divisions: int = 10,
        minor_divisions: int = 1,
        start_angle: int = 240,
        end_angle: int = -295,
        axis_color: str = "grey80",
        bg: str = None,
        fg: str = "white",
        scroll: bool = False,
        scroll_steps: float = 1,
        scale_color: str = "black",
        needle_color: str = "grey30",
        integer: bool = False,
        state: str = "normal",
        command=None,
    ):
        super().__init__(
            master,
            start,
            end,
            radius,
            width,
            height,
            text,
            text_color,
            text_font,
            border_width,
            border_color,
            major_divisions,
            minor_divisions,
            start_angle,
            end_angle,
            axis_color,
            bg,
            fg,
            scroll,
            scroll_steps,
            scale_color,
            needle_color,
            integer,
            state,
            command,
        )
        self.target_value = 0
        self.min = start
        self.dead = False
        self.ani_thread: thrd.Thread

    def animated_move(self):
        factor = 0.1  # Smoothing factor
        threshold = 0.5  # Minimum movement threshold to stop animation
        if abs(self.target_value - self.value) > threshold:
            move = (self.target_value - self.value) * factor
            new_value = self.value + move
            self.set(round(new_value, 1))
            self.master.after(25, self.animated_move)
            return
        self.set(self.target_value)  # Ensure it ends exactly at the target

    def move_to(self, target):
        self.target_value = target
        self.animated_move()
