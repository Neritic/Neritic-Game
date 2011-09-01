from ..world.world import World
from cube import Cube

class TestWorld (World):
    def load (self):
        cube = Cube()
        self.add_entity(cube)
