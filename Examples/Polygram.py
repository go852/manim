from manim import *
import numpy as np

class PolygramExample(Scene):
    def construct(self):
        # hexagram = Polygram(
        #     [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
        #     [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],
        # )

        # hexagram = Circle(3, color=BLUE)
        hexagram = Square(side_length=2)
        hexagram.shift(DOWN*2)
        self.add(hexagram)

        dot = Dot(color=ORANGE)
        self.play(MoveAlongPath(dot, hexagram), run_time=10, rate_func=linear)
        self.remove(dot)
        self.wait(1)
        self.clear()

        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)
        self.wait(2)