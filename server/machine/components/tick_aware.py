import threading
import time

TICK_AWARES = []


def tick():
    while True:
        for a in TICK_AWARES:
            a.tick()
        time.sleep(0.01)


TICK_THREAD = threading.Thread(target=tick, daemon=True, name="TICK_THREAD")
TICK_THREAD.start()


class TickAware:
    def __init__(self):
        TICK_AWARES.append(self)

    def tick(self):
        pass


class SourceConsumerMixin(TickAware):
    def __init__(self):
        TickAware.__init__(self)
        self.__source = None

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, val):
        self.__source = val

    def tick(self):
        if self.__source is not None:
            self.value = next(self.__source)

