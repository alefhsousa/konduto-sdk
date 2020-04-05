from abc import abstractmethod


class Either(object):
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    @property
    def value(self):
        return self.get_value()

    @property
    @abstractmethod
    def is_right(self):
        return NotImplemented

    @property
    @abstractmethod
    def is_left(self):
        return NotImplemented

    @abstractmethod
    def __eq__(self, other):
        return NotImplemented


class Right(Either):

    """Represents a successful computation."""
    @property
    def is_left(self):
        return False

    @property
    def is_right(self):
        return True

    def __eq__(self, other):
        """Returns True if all values are equals."""
        return isinstance(other, Right) and self._value == other._value

    def __repr__(self):
        """Returns state of the class."""
        return "Right %s" % self._value


class Left(Either):

    """Represents a computation that has failed."""
    @property
    def is_left(self):
        return True

    @property
    def is_right(self):
        return False

    def __eq__(self, other):
        """Returns True if all values are equals."""
        return isinstance(other, Left) and self._value == other._value

    def __repr__(self):
        """Returns state of the class."""
        return "Left %s" % self._value
