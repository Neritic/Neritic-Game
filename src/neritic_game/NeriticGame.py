import sys
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

        self.is_running = True
        while self.is_running:
            for event in self.window.iter_events():
                if event.type == sf.Event.CLOSED:
                    self.is_running = False

            self.window.clear(sf.Color.WHITE)
            self.window.display()

        self.window.close()
