import sys
import time

import sf

from testworld import TestWorld
from testrenderer import TestSceneRenderer
''' this is a test game, put test code here '''

class Main:
    def __init__ (self):
        self.title = 'Neritic Game'
        self.video_mode = sf.VideoMode(640, 480, 32)
        self.is_running = False
    
    def run (self):
        ''' main entry point for game '''

        self.window = sf.RenderWindow(self.video_mode, self.title, sf.Style.CLOSE)
        self.window.framerate_limit = 60

        world = TestWorld()
        scene = TestSceneRenderer(world)

        world.load()

        # physics time variables
        t = 0.0
        dt = 0.01
        curtime = 0.0
        accumulator = 0.0

        self.is_running = True
        while self.is_running:
            # process events
            for event in self.window.iter_events():
                if event.type == sf.Event.CLOSED:
                    self.is_running = False

            # physics updates
            newtime   = time.time()
            deltatime = min((0.1, newtime - curtime))
            curtime   = newtime

            accumulator += deltatime
            while accumulator >= dt:
                accumulator -= dt
                world.update(t, dt)
                t += dt

            # display update
            self.window.clear(sf.Color.WHITE)
            scene.render(self.window)
            self.window.display()

            t += dt

        self.window.close()
