from abc import ABC, abstractmethod


class TVBase(ABC):
    """Абстрактный телевизор"""

    @abstractmethod
    def tune_channel(self, channel):
        raise NotImplementedError()


class SonyTV(TVBase):
    """Телевизор Sony"""

    def tune_channel(self, channel):
        print('Sony TV: выбран %d канал' % channel)


class SharpTV(TVBase):
    """Телевизор Sharp"""

    def tune_channel(self, channel):
        print('Sharp TV: выбран %d канал' % channel)


class RemoteControlBase(ABC):
    """Абстрактный пульт управления"""

    def __init__(self):
        self._tv = self.get_tv()

    @abstractmethod
    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    """Пульт управления"""

    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0  # текущий канал

    def get_tv(self):
        return SharpTV()

    def tune_channel(self, channel):
        # super(RemoteControl, self).tune_channel(channel)
        self._channel = channel
        self._tv.tune_channel(channel)

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


if __name__ == "__main__":
    remote_control = RemoteControl()
    remote_control.tune_channel(5)
