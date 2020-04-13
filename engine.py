import wx
import cv2 as cv


def to_number(x, y=None):
    try:
        x = int(x)
    except ValueError:
        return to_number(y)
    return x


class VideoFeed(object):
    def __init__(self, filename=None, resize=False):
        self.open(filename, resize)

    def open(self, filename=None, resize=False):
        self.video = cv.VideoCapture(filename if filename else 0)
        self.resize = resize
        self.set_default_size()

    def opened(self):
        return self.video.isOpened()

    def next_frame(self):
        ret, frame = self.video.read()
        if ret and self.resize:
            cv.resize(frame, (self._width, self._height))
        return frame if ret else None

    def length(self):
        return self.video.get(cv.CAP_PROP_FRAME_COUNT)

    # <frame_size>
    def get_frame_width(self):
        return self.video.get(cv.CAP_PROP_FRAME_WIDTH)

    def get_frame_height(self):
        return self.video.get(cv.CAP_PROP_FRAME_HEIGHT)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_width(self, w=None):
        self._width = to_number(w, self._width)

    def set_height(self, h=None):
        self._height = to_number(h, self._height)

    def set_default_size(self):
        self.set_size(self.get_frame_width(), self.get_frame_height())

    def set_size(self, w=None, h=None):
        self.set_width(w)
        self.set_height(h)

    # </frame_size>

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

    def __del__(self):
        self.video.release()
