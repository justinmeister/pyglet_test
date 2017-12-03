import pyglet as pg
import constants as c

class Game():
    def __init__(self):
        self.window = pg.window.Window(width=800, height=600)
        self.setup_resources()
        self.keys = pg.window.key.KeyStateHandler()
        self.window.push_handlers(self.keys)
        self.screen_manager = Screen_Manager(self.window, self.keys)
        
        
    def setup_resources(self):
        pg.resource.path = ['./resources']
        pg.resource.reindex()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.screen_manager.current_screen.render_scene()

    def update(self, dt):
        keys = pg.window.key.KeyStateHandler()
        self.screen_manager.update(dt)
  
    def run(self):
        pg.clock.schedule_interval(self.update, 1/60.0)
        pg.app.run()


class Screen_Manager():
    def __init__(self, window, keys):
        self.keys = keys
        self.current_screen = Level_1(window, keys)

    def update(self, dt):
        self.current_screen.update(dt)

    def render_scene():
        self.current_screen.render_scene()
        

class Screen():
    def __init__(self, window, keys):
        self.window = window
        self.keys = keys
        self.batch = pg.graphics.Batch()

    def render_scene(self):
        self.background.draw()
        self.batch.draw()

    def update(self, dt):
        self.check_user_input()
        self.update_sprite_position()
        
    def check_user_input(self):
        if self.keys[pg.window.key.SPACE]:
            self.player.y += 3

        elif self.keys[pg.window.key.K]:
            self.player.y -= 3

        if self.keys[pg.window.key.J]:
            self.player.x -= 3

        elif self.keys[pg.window.key.L]:
            self.player.x += 3

    def update_sprite_position(self):
        pass




class Level_1(Screen):
    def __init__(self, window, keys):
        super().__init__(window, keys)
        self.background = pg.sprite.Sprite(
                (pg.resource.image('stars.jpg')), x=0, y=0)
        self.player = Player(
                (pg.resource.image(c.ROCKET_IMAGE)), c.BEGINX, c.BEGINY, self.batch)




class Player(pg.sprite.Sprite):
    def __init__(self, image, x, y, batch):
        super().__init__(image, x, y, batch=batch)
        self.x_vel = 0
        self.y_vel = 0
        self.state = c.IDLING

    def update(self, dt, keys):
        if self.state == c.IDLING:
            self.idling(dt, keys)
        elif self.state == c.MOVING:
            self.moving(dt, keys)

    def idling(self, dt, keys):
        y_accel = 0
        x_accel = 0
        
        if keys[pg.window.key.I]:
            if keys[pg.window.key.K]:
                pass
            else:
                y_accel = c.Y_ACCEL
        
        elif keys[pg.window.key.K]:
            y_accel = Y_ACCEL * -1

        if keys[pg.window.key.J]:
            if keys[pg.window.key.L]:
                pass
            else:
                x_accel = c.X_ACCEL * -1
        elif keys[pg.window.key.L]:
            x_accel = c.X_ACCEL

        if (y_accel and x_accel) != 0:
            self.enter_moving(x_accel, y_accel)

    def enter_moving(self, x_accel, y_accel):
        self.state = c.MOVING
        self.x_accel = x_accel
        self.y_accel = y_accel

    def moving(self, dt, keys):
        pass


    
            
        

    def moving(self, dt, keys):
        pass

    
        



if __name__ == '__main__':
    game = Game()
    game.run()

