class Animal():
    """docstring for Animal."""

    def __init__(self, ):
        self.num_eyes = 2
        super(Animal, self).__init__()

    def breathe(self):
        print('exhale')


class Fish(Animal):
    """docstring for Fish."""

    def __init__(self):
        super(Fish, self).__init__()

    def breathe(self, ):
        super().breathe()
        print('doing underwater')


fish = Fish()

fish.breathe()
