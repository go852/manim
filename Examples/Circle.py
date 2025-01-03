from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Write(Text("Draw a circle with PINK color.")))
        self.play(Create(circle))  # show the circle on screen
