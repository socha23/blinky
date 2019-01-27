from gpiozero.mixins import SourceMixin


class ProgressBar:
    def __init__(self, *args, **kwargs):
        self.__length = kwargs['length']
        self.__value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = max(0, min(1, val))
        self.update()

    def update(self):
        filled = int(self.__value * self.__length)
        print("\r[%s%s] %.2f" % ("=" * filled, " " * (self.__length - filled), self.__value), end="\r")

    def end(self):
        print()


class ProgressBarOutput(SourceMixin, ProgressBar):
    def __init__(self, *args, **kwargs):
        SourceMixin.__init__(self, *args, **kwargs)
        ProgressBar.__init__(self, *args, **kwargs)
