import sf
from ..entities.entity import Entity

#FIXME: do we really need interface classes like this
class Renderer (object):
    def __init__ (self):
        pass

    #FIXME: It may be beneficial to have render return a sprite for drawing externally
    def render (self, rendertarget):
        pass

#FIXME: this might make more sense in generic.py
class EntityRenderer (Renderer):
    ''' renders a game entity '''
    
    def __init__ (self, entity):
        self.entity = entity

    def interpolate (self):
        ''' interpolates the previous state for smoother rendering '''
        pass

    def render (self, rendertarget):
        #FIXME: implement rudimentiary static image draw
        pass

#FIXME: does this belong here?
class SceneRenderer (Renderer):
    ''' 
        manages and renders the game scene 
        in this case "scene" refers to the graphical scene
    '''

    def __init__ (self, world):
        self.world = world

    def render (self, rendertarget):
        pass
