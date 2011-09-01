import sf
from ..entities.entity import Entity

class Cube (Entity):
    ''' useless testing cube '''

    def __init__ (self):
        self.x = 200
        self.y = 1000

    def apply_physics (self, t, dt):
        #FIXME: implemnent verlet/rk4 integration scheme
        # for now it just moves the cube toward the top of the screen
        self.y *= 0.98

    def update (self, t, dt):
        self.apply_physics(t, dt)
