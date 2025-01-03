from manim import *

class LineExample(Scene):
    def construct(self):
        l = Line(LEFT, RIGHT)
        p1 = l.get_start()
        p2 = l.get_end()
        d0 = Dot(UP)
        d1 = Dot(p1)
        d2 = Dot(p2)
        # d3 = Dot(l.get_projection(UP), color=RED)
        d3 = Dot((p1+p2)/2)

        self.add(l, d0, d1, d2)
        self.play(Create(Line(d0.get_center(), d1.get_center())))
        self.play(Create(Line(d0.get_center(), d2.get_center())))
        self.play(Create(Line(d0.get_center(), d3.get_center())))
        self.play(Create(d3))
        self.wait()