import math


class Hit:
    __slots__ = ['hit', 'entity', 'point', 'world_point', 'distance', 'normal', 'world_normal']


    def __init__(self, **kwargs):

        self.hit = None
        self.entity = None
        self.point = None
        self.world_point = None
        self.distance = math.inf
        self.normal = None
        self.world_normal = None

        for key, value in kwargs.items():
            setattr(self, key, value)
