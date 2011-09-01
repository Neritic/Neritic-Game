import sys
import time

import sf

class Main:
    def __init__ (self):
        self.title = 'Neritic Game'
        self.video_mode = sf.VideoMode(640, 480, 32)
        self.is_running = False
    
    def run (self):
        ''' main entry point for game '''

        self.window = sf.RenderWindow(self.video_mode, self.title, sf.Style.CLOSE)
        self.window.framerate_limit = 60

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
            deltatime = min((0.25, newtime - curtime))
            curtime   = newtime

            accumulator += deltatime
            while accumulator >= dt:
                accumulator -= dt
                # do physics here
                t += dt

            # display update
            self.window.clear(sf.Color.WHITE)
            self.window.display()

            t += dt

        self.window.close()
