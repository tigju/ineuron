class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print(f'I can {self.laser.does()}, I can {self.claw.does()}, and I can {self.smartphone.does()}')


robot = Robot()

robot.does()