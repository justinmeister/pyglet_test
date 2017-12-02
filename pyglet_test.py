import pyglet as pg
import constants as c

class Game():
    def __init__(self):
        self.window = pg.window.Window(width=800, height=600)
        self.setup_resources()
        self.screen_manager = Screen_Manager(self.window)
        
    def setup_resources(self):
        pg.resource.path = ['./resources']
        pg.resource.reindex()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.screen_manager.current_screen.render_scene()

    def update(self, dt):
        self.screen_manager.update(dt)
  
    def run(self):
        pg.clock.schedule_interval(self.update, 1/60.0)
        pg.app.run()


class Screen_Manager():
    def __init__(self, window):
        self.current_screen = Level_1(window)

    def update(self, dt):
        pass

    def render_scene():
        self.current_screen.render_scene()
        

class Screen():
    def __init__(self, window):
        self.window = window

    def render_scene(self):
        self.background.draw()
        self.batch.draw()


class Level_1(Screen):
    def __init__(self, window):
        super().__init__(window)
        self.batch = pg.graphics.Batch()
        self.background = pg.sprite.Sprite(
                (pg.resource.image('stars.jpg')), x=0, y=0)
        self.player = Player(
                (pg.resource.image(c.ROCKET_IMAGE)), c.BEGINX, c.BEGINY, self.batch)


class Player(pg.sprite.Sprite):
    def __init__(self, image, x, y, batch):
        super().__init__(image, x, y, batch=batch)
        



if __name__ == '__main__':
    game = Game()
    game.run()

