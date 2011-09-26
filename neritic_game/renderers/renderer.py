import sf
from ..entities.entity import Entity

#FIXME: this whole file is pretty bad

#FIXME: do we really need interface classes like this
class Renderer (object):
    def __init__ (self):
        pass

    #FIXME: It may be beneficial to have render return a sprite for drawing externally
    def render (self, rendertarget):
        pass

#FIXME: this might make more sense in generic.py
#FIXME: who was material?
class EntityRenderer (Renderer):
    ''' renders a game entity '''
    
    def __init__ (self, entity, scene):
        self.entity = entity
        self.scene = scene

    def interpolate (self):
        ''' interpolates the previous state for smoother rendering '''
        pass

    def render (self, rendertarget):
        #FIXME: implement rudimentiary static image draw
        pass

#FIXME: does this belong here?
#FIXME: moreover does it need to subclass renderer?
class SceneRenderer (Renderer):
    ''' 
        manages and renders a (the) game scene 
        in this case "scene" refers to the graphical scene
    '''
    
    # >passing in a big hash of classes and associated rendering classes
    # >2011
    def __init__ (self, world):
        self.world = world
        self.resourcemanaager = None

        self.renderers = {}
        self.rendermap = {}

    def render (self, rendertarget): 
        for entity in self.world.entities:
            if (entity not in self.renderers or self.renderers[entity] == None):
                if entity.name in self.renderermap:
                    self.renderers[entity] = self.renderermap[entity.name](entity, self)
            
            self.renderers[entity].render(rendertarget)
