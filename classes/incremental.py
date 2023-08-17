class Incrimental:

    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def increment(self, more=1):
        if(self._count == 5):
            raise ValueError("count can not be more than 5")
        elif self._count==3:
            self._count -= 1
        else:
            self._count += more
