import sf
from cube import Cube
from ..renderers.renderer import EntityRenderer, SceneRenderer

class CubeRenderer (EntityRenderer):
    '''
        renders a cube
        please remember this is just for testing and 
        NOT how a cube should be rendered in production 
    '''

    def __init__ (self, entity = None):
        #FIXME: image loading should be centralized
        self.sprite = sf.Shape.rectangle(0, 0, 100, 100, sf.Color.RED)

        super(CubeRenderer, self).__init__(entity)

    def render (self, rendertarget):
        self.sprite.x = self.entity.x
        self.sprite.y = self.entity.y

        rendertarget.draw(self.sprite)

class TestSceneRenderer (SceneRenderer):
    ''' as above remember this is for testing '''

    def __init__ (self, world):
        self.renderers = {}
        self.renderers['cube'] = CubeRenderer()
        super(TestSceneRenderer, self).__init__(world)

    def render (self, rendertarget):
        #FIXME: THIS IS VERY BAD DO NOT DO THIS
        # ideally we would magically understand that our cube needs a CubeRenderer
        # as well with knowing that our cube had a cuberenderer already instanced
        # this could be achieved with IDs of some sort

        for entity in self.world.entities:
            if isinstance(entity, Cube):
                self.renderers['cube'].entity = entity
                self.renderers['cube'].render(rendertarget)
