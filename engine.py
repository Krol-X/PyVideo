import cv2 as cv
import os
import sys


def resource_path(relative):
    return (sys._MEIPASS+"/" if getattr(sys, 'frozen', False) else "")+relative

def to_number(x, y=None):
    try:
        x = int(x)
    except ValueError:
        return to_number(y) if y else y
    except TypeError:
        return to_number(y) if y else y
    return x


def apply_effect(frame, eff: list):
    if len(eff) < 1:
        return frame
    eff_n = eff[0]
    if eff_n == 1:
        return cv.blur(frame, (eff[1], eff[2]))
    elif eff_n == 2:
        return cv.GaussianBlur(frame, (eff[1], eff[2]))
    elif eff_n == 3:
        return cv.medianBlur(frame, eff[1])
    elif eff_n == 4:
        return cv.bilateralFilter(frame, eff[1], eff[2], eff[3])
    else:
        return frame


class VideoFeed(object):
    def __init__(self, filename=None, resize=False):
        self.effect = [0]
        self.open(filename, resize)

    def open(self, filename=None, resize=False):
        self.video = cv.VideoCapture(filename if filename else 0)
        print(self.video.isOpened())
        self.resize = resize

    def opened(self):
        return self.video.isOpened()

    def saveto(self, name):
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter(name,
                             fourcc,
                             self.get_fps(),
                             (self.get_frame_size())
                             )
        pos = self.get_position()
        self.set_position(0)
        while True:
            frame = self.next_frame()
            if frame is None:
                break
            out.write(frame)
        self.set_position(pos)
        out.release()

    def next_frame(self, w=None, h=None):
        ret, frame = self.video.read()
        if ret and self.effect[0] != 0:
            frame = apply_effect(frame, self.effect)
        if ret and self.resize and w and h:
            frame = cv.resize(frame, (w, h))
        return frame if ret else None

    def length(self):
        return self.video.get(cv.CAP_PROP_FRAME_COUNT)

    def get_frame_size(self):
        v = self.video
        return int(v.get(cv.CAP_PROP_FRAME_WIDTH)), int(v.get(cv.CAP_PROP_FRAME_HEIGHT))

    # <position>
    def get_position(self):
        return self.video.get(cv.CAP_PROP_POS_FRAMES)

    def get_position_ms(self):
        return self.video.get(cv.CAP_PROP_POS_MSEC)

    def set_position(self, frame):
        return self.video.set(cv.CAP_PROP_POS_FRAMES, frame)

    def set_position_ms(self, ms):
        return self.video.set(cv.CAP_PROP_POS_MSEC, ms)
    # </position>

    def get_fps(self):
        return self.video.get(cv.CAP_PROP_FPS)

    def __del__(self):
        self.video.release()
