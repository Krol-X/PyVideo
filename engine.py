import cv2 as cv


def to_number(x, y=None):
    try:
        x = int(x)
    except ValueError:
        return to_number(y) if y else y
    except TypeError:
        return to_number(y) if y else y
    return x


class VideoFeed(object):
    def __init__(self, filename=None, resize=False):
        self.open(filename, resize)

    def open(self, filename=None, resize=False):
        self.video = cv.VideoCapture(filename if filename else 0)
        self.resize = resize

    def opened(self):
        return self.video.isOpened()

    def next_frame(self, w = None, h = None):
        ret, frame = self.video.read()
        if ret and self.resize and w and h:
            frame = cv.resize(frame, (w, h))
        return frame if ret else None

    def length(self):
        return self.video.get(cv.CAP_PROP_FRAME_COUNT)

    def get_frame_size(self):
        v = self.video
        return v.get(cv.CAP_PROP_FRAME_WIDTH), v.get(cv.CAP_PROP_FRAME_HEIGHT)

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
