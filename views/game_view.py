import arcade
import pymunk

from base.settings import Settings
from base.view_manager import ViewManager, ViewTypes


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.view_manager = ViewManager()
        self.time_taken = 0

        self.circle1_name = Settings.PLAYER1_NAME
        self.circle2_name = Settings.PLAYER2_NAME

        self.shapes_ids = {
            'circle 1': 1,
            'circle 2': 2,
            'left border': 3,
            'right border': 4,
            'floor': 5
        }

        self.game_ended = False

        self.moves = {
            97: (1, -5000, 0),
            100: (1, 5000, 0),

            65361: (2, -5000, 0),
            65363: (2, 5000, 0)
        }

        self.jumps = {
            32: (1, 0, 20000),

            65421: (2, 0, 20000),
            65293: (2, 0, 20000)
        }

        self.block_jump1 = False
        self.block_jump2 = False

        self.space = pymunk.Space()
        self.space.gravity = 0, -500

        self.circle_mass = 1
        self.circle_radius = 20

        circle1_body = pymunk.Body(self.circle_mass, 1)
        circle2_body = pymunk.Body(self.circle_mass, 1)
        self.circle1 = pymunk.Circle(circle1_body, self.circle_radius)
        self.circle2 = pymunk.Circle(circle2_body, self.circle_radius)

        self.floor = pymunk.Poly.create_box(self.space.static_body, (5000, 10))
        self.left_border = pymunk.Poly.create_box(pymunk.Body(body_type=pymunk.Body.STATIC), (10, 5000))
        self.right_border = pymunk.Poly.create_box(pymunk.Body(body_type=pymunk.Body.STATIC), (10, 5000))

        handler = self.space.add_default_collision_handler()
        handler.begin = self.begin_collision

        self.space.add(circle1_body, circle2_body)

        arcade.set_background_color(arcade.color.BLACK_BEAN)

    def setup(self):
        self.circle1.elasticity = 0.8
        self.circle1.friction = 0.5
        self.circle1.body.position = 100, 700
        self.circle1.id = self.shapes_ids['circle 1']
        self.circle2.elasticity = 0.8
        self.circle2.friction = 0.5
        self.circle2.body.position = 500, 700
        self.circle2.id = self.shapes_ids['circle 2']

        self.floor.elasticity = 0.01
        self.floor.friction = 1.0
        self.floor.body.position = -200, 0
        self.floor.id = self.shapes_ids['floor']

        self.left_border.elasticity = 0.01
        self.left_border.body.position = 0, 0
        self.left_border.id = self.shapes_ids['left border']

        self.right_border.elasticity = 0.01
        self.right_border.body.position = self.window.width, 0
        self.right_border.id = self.shapes_ids['right border']

        self.space.add(self.circle1, self.circle2)
        self.space.add(self.floor)
        self.space.add(self.left_border)
        self.space.add(self.right_border)

    def end_game_handle(self, winner_id):
        self.game_ended = True
        self.view_manager.show_view(ViewTypes.GameOver, time_taken=self.time_taken, winner_id=winner_id)

    def begin_collision(self, arbiter, space, data):
        if arbiter.shapes[1].id in [self.shapes_ids['left border'], self.shapes_ids['right border']]:
            space.remove(arbiter.shapes[0], arbiter.shapes[0].body)

            self.end_game_handle(
                self.circle2_name if arbiter.shapes[0].id == self.shapes_ids['circle 1'] else self.circle1_name
            )

            return False

        if arbiter.shapes[1].id == self.shapes_ids['floor']:
            if arbiter.shapes[0].id == self.shapes_ids['circle 1']:
                self.block_jump1 = False
            else:
                self.block_jump2 = False

        return True

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol in self.moves.keys():
            circle = self.circle1 if self.moves[symbol][0] == 1 else self.circle2

            circle.body.apply_force_at_world_point(
                self.moves[symbol][1:],
                circle.body.position
            )
        elif symbol in self.jumps.keys():
            if self.jumps[symbol][0] == 1:
                if self.block_jump1:
                    return
                else:
                    self.block_jump1 = True
            else:
                if self.block_jump2:
                    return
                else:
                    self.block_jump2 = True

            circle = self.circle1 if self.jumps[symbol][0] == 1 else self.circle2

            circle.body.apply_force_at_world_point(
                self.jumps[symbol][1:],
                circle.body.position
            )

    def on_update(self, delta):
        if not self.game_ended:
            self.time_taken += delta
            self.space.step(delta)

    def on_draw(self):
        arcade.start_render()

        if self.circle1 in self.space.shapes:
            arcade.draw_circle_filled(self.circle1.body.position.x,
                                      self.circle1.body.position.y,
                                      self.circle_radius,
                                      arcade.color.GOLD)

        if self.circle2 in self.space.shapes:
            arcade.draw_circle_filled(self.circle2.body.position.x,
                                      self.circle2.body.position.y,
                                      self.circle_radius,
                                      arcade.color.APPLE_GREEN)

        arcade.draw_polygon_filled(self.floor.get_vertices(), arcade.color.GOLD)
